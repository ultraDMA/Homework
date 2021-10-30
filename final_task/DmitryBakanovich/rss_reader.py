#!/usr/bin/env python3
"""Command-line RSS-Reader Utility"""
import requests
import time
from bs4 import BeautifulSoup
import json
import logging
import sys
import datetime
import dateparser
from rss_argparser import get_argparser
import rss_converter

start_time = time.time()


def get_page_xml(source):
    """
    This function receives and processes the response from the address passed to it. Implemented using the standard
    "requests" module. If an address of the None-type is passed to the function (depending on the rss_argparser.py
    module), then return None occurs. If the function does not receive the expected response code from the server,
    an empty string is returned. In case of response.status_code == 200 the function returns the response object as
    string
    :param source:
    :return: response.text
    :return: ''
    """
    if source is None:
        print('No URL has entered')
        return None
    logging.debug(f'Starting GET_PAGE_XML function.')
    attempt = 3
    while True:
        try:
            logging.debug(f'Awaiting for response from {source}')
            response = requests.get(source)
            if response.status_code == 200:
                logging.debug(f'Response status code: {response.status_code}')
                logging.debug(f'Ending GET_PAGE_XML function.')
                return response.text
            else:
                logging.debug(f'Can"t get expected response from {source}')
                logging.debug(f'Ending GET_PAGE_XML function.')
                return None
        except:
            logging.debug('Connection Error')
            print(
                f'Connection Error. Will retry after 1 sec. Attempts left: {attempt}')
            time.sleep(1)
        attempt -= 1
        if attempt < 1:
            print(f'I can\'t connect to address: {source} \nPlease, check your connection or make \
sure the requested address is correct: http://..., https://...')
            logging.debug('Program has stopped to working: Connection Error')
            return None


def parse_xml(raw_xml, limit) -> str:
    """
    The function is intended for parsing a string object as XML format. The function is implemented using the
    powerful BeautifulSoup library from the bs4 package. The input of the function is a string passed from the
    get_page_xml function and an integer (limit) passed from the rss_argparser module, which sets the number of
    processed news articles. Function returns objects: a list of dictionaries containing tags as a key and content as
    a value, and the title of a news resource.
    :param raw_xml:
    :param limit:
    :return: title_feed, items_list
    """
    logging.debug('Starting PARSE_XML function.')
    items_list = []
    logging.debug('BeautifulSoup calling')
    soup = BeautifulSoup(raw_xml, 'xml')
    logging.debug('Creating temporary object "items_temp"')
    channel = soup.find('channel')
    if not channel:
        print('This is not-RSS page')
    items_temp = soup.find_all('item')
    try:
        logging.debug('Trying to create "title_feed" object')
        title_feed = soup.find('title').text
    except:
        logging.debug('Failed to find "title" tag')
        print('Looks like it is unsupported page. Must be RSS feed')
        logging.debug(
            'Program has stopped to working: Unsupported Page Format')
        title_feed = 'Error! Try to choose a different source. Exit program'
    if limit < 0:
        limit = len(items_temp)
    for element in items_temp[:limit]:
        logging.debug(f'Starting to fill "items" dict')
        child_item = {"title": element.find("title").text.lstrip(), "link": element.find("link").text,
                      "pubDate": element.find("pubDate").string}
        try:
            """Looking at many different news feeds, it was found that they do not adhere to one standard for 
            image link tags. There are two main_func options implemented here. If none of them is executed, we will 
            assume that the image was not found. Possible to research this and fix it in future versions. """
            try:
                child_item["image"] = element.find('enclosure')["url"]
            except:
                child_item["image"] = element.find('media:content')["url"]
        except:
            child_item["image"] = 'No image found'
        """In the lines below, I tried to implement receiving a description of the news, if it is not in the 
        feed. In this case, get_page_xml function is called and a target_link from the feed is passed to it.
        Perhaps not the best implementation. The program may stop prematurely if the link to the news
        does not work"""
        try:
            child_item["description"] = element.find("description").text
        except:
            description = parse_news_content(element.find('link').text)
            if description is not None:
                child_item["description"] = description
            else:
                child_item["description"] = "No description"
        logging.debug(f'Appending object {child_item} to "items" dict')
        items_list.append(child_item)
    else:
        logging.debug('Ending PARSE_XML function.')
        return title_feed, items_list


def parse_news_content(target_link):
    """
    An additional function that allows you to parse links from the news feed to get a description if there is no
    description in the feed. Works the same as parse_xml, except that it parses two elements at a time for the <p> tag.
    Internally it calls the get_page_xml function to get content from a target_link. Returns a string.
    :param target_link: from function 'parse_xml'
    :return: str
    """
    logging.debug('Starting PARSE_NEWS_CONTENT function.')
    content = ''
    page_html = get_page_xml(target_link)
    if page_html is None:
        return 'No description'
    logging.debug(f'BeautifulSoup calling. {target_link}')
    soup = BeautifulSoup(page_html, 'lxml')
    p_list = soup.find_all('p')
    for element in p_list[0:2]:
        if element.text.split() != '\n':
            content += element.text
    logging.debug('Ending PARSE_NEWS_CONTENT function.')
    return content


def print_elements(title, items):
    """
    Printing function for rss_reader
    :param title:
    :param items:
    :return: None
    """
    logging.debug('Starting PRINT_ELEMENTS function.')
    print(f'\nFeed: {title}\n')
    for i in range(len(items)):
        logging.debug(f'Printing #{i + 1} element:')
        print(f'# {i + 1}')
        print(f'Title: {items[i]["title"]}')
        print(f'Date: {items[i]["pubDate"]}')
        print(f'Link: {items[i]["link"]}')
        print(f'Description: {items[i]["description"]}')
        print(f'Image: {items[i]["image"]}')
        logging.debug(f'End Printing #{i + 1} element:')
    logging.debug('Ending PRINT_ELEMENTS function.')


def print_json(title, items):
    """
    Printing function for rss_reader if --json parameter has been chosen
    :param title:
    :param items:
    :return: None
    """
    logging.debug('argument --json True')
    print(title, '\n', json.dumps(
        items, indent=2, ensure_ascii=False, sort_keys=False))
    logging.debug(
        f'Program completed, time of operating: {time.time() - start_time}')


def write_cache(parsed_title_feed, parsed_page, link_to_find):
    logging.debug('Called "write_cache"')
    """
    The function accepts a parsed news feed title, a parsed page, and a source link. Writes the requested news line
    by line to the 'news_cached.txt' file, provides the lines with tags. All cached news is expected to be unique:
    publication date, news source - for the possibility of further search by these tags
    :param parsed_title_feed: str
    :param parsed_page: list of dicts
    :param link_to_find: str
    :return: None
    """
    if not link_to_find.endswith('/'):
        link_to_find += '/'
    read_file = ''
    try:
        with open('news_cached.txt', 'r', encoding='utf-8') as file:
            read_file = file.read()
    except:
        print('Creating new: news_cached.txt')
    with open('news_cached.txt', 'a+', encoding='utf-8') as file:
        logging.debug('Creating cache file "news_cached.txt"')
        file.write('\n"Start caching at": "%s", "Feed": "%s"\n' % (
            str(datetime.datetime.now()).replace('-', ','), parsed_title_feed))
        for element in parsed_page:
            pub_date_parse = dateparser.parse(element['pubDate'])
            normalized_date = pub_date_parse.strftime('%Y%m%d')
            writable_element = json.dumps(element, ensure_ascii=False)
            writable_element_string = str(writable_element)
            if writable_element_string not in read_file:
                logging.debug('Unique element found! Adding to "news_cached.txt"')
                file.write(
                    f'{normalized_date} :: {writable_element} :: {link_to_find}\n')
            else:
                logging.debug('Article is already exist in "news_cached.txt". Skip adding')


def read_cache(target_date, link_stamp, limit):
    logging.debug('Called "read_cache"')
    """
    The function of reading data from the cache 'news_cached.txt': works if it was previously created by the
    'write_cache' function. Receives a date, a link and a limit on the number of news. Prints search result in
    std.out, returns a list of dictionaries with strings of news articles for possible further processing by
    converter
    :param target_date: str
    :param link_stamp: str
    :param limit: int
    :return: list
    """
    flag_not_found = True
    if link_stamp is not None and not link_stamp.endswith('/'):
        link_stamp += '/'
    link_header = link_stamp if link_stamp is not None else ''
    try:
        with open('news_cached.txt', 'r', encoding='utf-8') as file:
            logging.debug(f'Opening cache file "news_cached.txt" for read. {target_date}, {link_stamp}, {limit}')
            print('Start Reading..')
            lines = file.readlines()
            read_limit = 0
            wrapped_strings = []
            for line in lines:
                if line[0:8].isdigit() and int(line[0:8]) >= int(target_date) and line.endswith(link_header + '\n'):
                    out = line[line.find('{'): line.rfind(' :: ')]
                    converted_in_dict = json.loads(out)
                    print(read_limit + 1, '=' * 64)
                    print(json.dumps(converted_in_dict, indent=2, ensure_ascii=False))
                    flag_not_found = False
                    read_limit += 1
                    print('-' * 67)
                    wrapped_strings.append(converted_in_dict)
                if read_limit == limit:
                    break
            if flag_not_found:
                logging.debug(f'Date: {target_date}, Feed: {link_stamp} Nothing found')
                print(
                    f'Error! Date: {target_date}, Feed: {link_stamp} Nothing found')
            return wrapped_strings
    except FileNotFoundError as e:
        logging.debug(f'{e} no cache file found')
        print(
            f'Error: {e} \nPlease, start rss-reader without --date argument at first')


def main_func():
    global start_time
    """
    Main logic of RSS-reader
    """
    version = '0.4.0'
    name_of_converted_file = str(datetime.datetime.now()).replace(':', '\'') + ' -RSS-Reader'
    cli_args = get_argparser()
    flag_json = bool(cli_args.json)
    verbose = bool(cli_args.verbose)
    link, limit = cli_args.source, cli_args.limit

    if verbose:
        logging.basicConfig(
            stream=sys.stdout, format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
        logging.debug(f'STARTING VERBOSE MODE')
        logging.debug(
            f'--version: {version}, --json: {flag_json}, --verbose: {verbose}, --limit: {limit}, source: {link}')
    logging.debug('Calling GET_PAGE_XML function')
    raw_xml = get_page_xml(link) if link else None
    """Caching, iteration 3"""
    date_to_find = cli_args.date
    """Convert, iteration 4"""
    to_pdf = cli_args.to_pdf
    to_html = cli_args.to_html

    if raw_xml is not None and link is not None and date_to_find is None:
        logging.debug('Calling PARSE_XML function')
        title, items = parse_xml(raw_xml, limit)
        if not items:
            logging.debug('Empty "items" list')
            print(
                f'{title} \n {link} has no RSS content, or --limit parameter is 0')
        elif items:
            logging.debug('Start caching to disk')
            write_cache(title, items, link)
        if to_html or to_pdf:
            logging.debug(f'to_html = {to_html} , to_pdf = {to_pdf}')
            item_to_convert = rss_converter.text_to_html(items)
            if to_html:
                logging.debug(f'Converting to_html = {to_html}')
                rss_converter.save_html(item_to_convert, name_of_converted_file)
            if to_pdf:
                logging.debug(f'Converting to_pdf = {to_pdf}')
                rss_converter.save_pdf(item_to_convert, name_of_converted_file)

        if flag_json:
            print_json(title, items)
        else:
            logging.debug('Calling PRINT_ELEMENTS function')
            print_elements(title, items)

    elif date_to_find is not None:
        if to_html:
            logging.debug(f'Converting to_html = {to_html}')
            rss_converter.save_html(rss_converter.text_to_html(read_cache(date_to_find, link, limit)),
                                    name_of_converted_file)
        elif to_pdf:
            logging.debug(f'Converting to_pdf = {to_pdf}')
            rss_converter.save_pdf(rss_converter.text_to_html(read_cache(date_to_find, link, limit)),
                                   name_of_converted_file)
        else:
            read_cache(date_to_find, link, limit)


    elif date_to_find is None:
        logging.debug(f'Empty raw_xml string, {raw_xml}')
        print(
            f'Wrong Page! I can not operate with it! May be {link} is non-RSS feed?')
    logging.debug(
        f'Program completed, time of operating: {time.time() - start_time}')
    print('\nEnd')


if __name__ == '__main__':
    main_func()
