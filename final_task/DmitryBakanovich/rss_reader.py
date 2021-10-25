#!/usr/bin/env python3
"""Command-line RSS-Reader Utility"""
import requests
import time
from bs4 import BeautifulSoup
import json
import logging
import sys
from rss_argparser import get_argparser


def get_page_xml(source):
    """
    This function receives and processes the response from the address passed to it. Implemented using the standard
    "requests" module. If an address of the None-type is passed to the function (depending on the rss_argparser.py
    module), an exit occurs. If the function does not receive the expected response code from the server,
    an empty string is returned. In case of response.status_code == 200 the function returns the response object as
    string
    :param source:
    :return: response.text
    :return: ''
    """
    if source is None:
        exit('No URL is entered. End')
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
                return ''
        except:
            logging.debug('Connection Error')
            print(f'Connection Error. Will retry after 1 sec. Attempts left: {attempt}')
            time.sleep(1)
        attempt -= 1
        if attempt < 1:
            print(f'I can\'t connect to address: {source} \nPlease, check your connection or make \
sure the requested address is correct: http://..., https://...')
            logging.debug('Program has stopped to working: Connection Error')
            exit('End')


def parse_xml(raw_xml, limit):
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
        exit('This is not-RSS page')
    items_temp = soup.find_all('item')
    try:
        logging.debug('Trying to create "title_feed" object')
        title_feed = soup.find('title').text
    except:
        logging.debug('Failed to find "title" tag')
        print('Looks like it is unsupported page. Must be RSS feed')
        logging.debug(
            'Program has stopped to working: Unsupported Page Format')
        exit(f'Try to choose a different source {link}. Exit program')
    if limit < 0:
        limit = len(items_temp)
    for element in items_temp[:limit]:
        logging.debug(f'Starting to fill "items" dict')
        child_item = {'title': element.find('title').text, 'link': element.find('link').text,
                      'pubDate': element.find('pubDate').string}
        try:
            """Looking at many different news feeds, it was found that they do not adhere to one standard for 
            image link tags. There are two main options implemented here. If none of them is executed, we will 
            assume that the image was not found. Possible to research this and fix it in future versions. """
            try:
                child_item['image'] = element.find('enclosure')['url']
            except:
                child_item['image'] = element.find('media:content')['url']
        except:
            child_item['image'] = 'No image found'
        """In the lines below, I tried to implement receiving a description of the news, if it is not in the 
        feed. In this case, get_page_xml function is called and a target_link from the feed is passed to it.
        Perhaps not the best implementation. The program may stop prematurely if the link to the news
        does not work"""
        try:
            child_item['description'] = element.find('description').text
        except:
            child_item['description'] = parse_news_content(
                element.find('link').text)
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
    :param target_link:
    :return: str
    """
    logging.debug('Starting PARSE_NEWS_CONTENT function.')
    content = ''
    page_html = get_page_xml(target_link)
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
    exit('End')


"""Main logic"""
version = 'Iteration I'
cli_args = get_argparser()
flag_json = bool(cli_args.json)
verbose = bool(cli_args.verbose)
link, limit = cli_args.source, cli_args.limit

start_time = time.time()

if verbose:
    logging.basicConfig(
        stream=sys.stdout, format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    logging.debug(f'STARTING VERBOSE MODE')
    logging.debug(
        f'--version: {version}, --json: {flag_json}, --verbose: {verbose}, --limit: {limit}, source: {link}')

logging.debug('Calling GET_PAGE_XML function')
raw_xml = get_page_xml(link)

if raw_xml != '':
    logging.debug('Calling PARSE_XML function')
    title, items = parse_xml(raw_xml, limit)
    if not items:
        logging.debug('Empty "items" list')
        print(
            f'{title} \n {link} has no RSS content, or --limit parameter is 0. Exit...')
    if flag_json:
        print_json(title, items)
    else:
        logging.debug('Calling PRINT_ELEMENTS function')
        print_elements(title, items)
else:
    logging.debug(f'Empty raw_xml string, {raw_xml}')
    print(
        f'Wrong Page! I can not operate with it! May be {link} is non-RSS feed?')

logging.debug(
    f'Program completed, time of operating: {time.time() - start_time}')
print('\nEnd')
