#!/usr/bin/env python3
"""A convertor module for rss_reader utility"""
from xhtml2pdf import pisa
import logging
import sys
import os

sys.path.append(os.getcwd())


def text_to_html(items):
    logging.debug('Called "text_to_html"')
    """
    The function converts the list of dictionaries given to it as input, obtained from the function "parse_xml" into
    a string containing HTML markup.
    :param items: list
    :return: str
    """
    main_html = ''
    style = '<head>\
                    <meta content="text/html; charset=utf-8" http-equiv="Content-Type"> \
                         <style type="text/css"> \
                            @page { size: A4; margin: 1cm; } \
                            @font-face { font-family: Arial; src: url(C:/Windows/Fonts/arial.ttf),\
                                 url(/Library/Fonts/arial.ttf); } \
                            p { color: black; font-family: Arial; } \
                         </style>\
                         </head>'
    for cache_json in items:
        title = cache_json['title']
        title = f'<p style="text-align:center"><strong>{title}</strong></p>'

        link = cache_json['link']
        link = f'<p style="text-align:center">{link}</p>'

        pubdate = cache_json['pubDate']
        pubdate = f'<p style="text-align:right">{pubdate}</p>'

        description = cache_json['description']
        description = f'<p style="text-align:center">{description}</p>'

        image = cache_json['image']
        if image == 'No image found':
            image = f'<p style="text-align:center">"NO IMAGE"</p>'
        else:
            image = f'<p style="text-align:center"><img alt="" src="{image}" /></p>'

        pre_html = f'{title}{link}{pubdate}{description}{image}'
        pre_html += '<p>============================================</p>'
        main_html += pre_html
    main_html = f'<html>{style}<body>' + main_html + '</body></html>'
    return main_html


def save_html(html, name_file):
    logging.debug('Called "save_html"')
    """
    The function saves the string passed to it, with html markup, to an .html file on disk
    :param html: str
    :param name_file: str
    :return: None
    """
    with open(f'{name_file}.html', 'w+', encoding='utf-8') as file:
        file.write(html)
    print(f'{name_file}.html has been created')


def save_pdf(html, name_file):
    logging.debug('Called "save_pdf"')
    """
    The function saves the string passed to it, with html markup, to an .pdf file on disk
    :param html:
    :param name_file:
    :return: None
    """
    result_file = open(f'{name_file}.pdf', "w+b")
    pisa.CreatePDF(html, dest=result_file, encoding='UTF-8')
    result_file.close()
    print(f'{name_file}.pdf has been created')
