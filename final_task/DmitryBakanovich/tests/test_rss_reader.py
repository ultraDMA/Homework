import unittest
from rss_reader import *

test_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:media="http://search.yahoo.com/mrss/" ' \
           'xmlns:atom="http://www.w3.org/2005/Atom">\n  <channel>\n    <title>dev.by: Все о работе в IT</title>\n    ' \
           '<description>dev.by: Все о работе в IT</description>\n    <link>https://dev.by/rss</link>\n    <atom:link ' \
           'href="https://dev.by/rss" rel="self"/>\n    <pubDate>Tue, 26 Oct 2021 18:10:39 GMT</pubDate>\n    ' \
           '<generator>Dev.by RSS Generator</generator>\n    <item>\n      <title>Роскомнадзор внес Telegram и ' \
           'LiveJournal в реестр соцсетей</title>\n      <id>tag:dev.by,2021-10-26:17083795</id>\n      <pubDate>Tue, ' \
           '26 Oct 2021 16:25:00 GMT</pubDate>\n      <lastBuildUpdate>Tue, 26 Oct 2021 16:25:34 ' \
           'GMT</lastBuildUpdate>\n      <category/>\n      <format>news</format>\n      <description>\r\nРегулятор ' \
           'дополнил реестр в\xa0рамках закона о\xa0самоконтроле соцсетей.\r\n</description>\n      <author>Николай ' \
           'Чикишев</author>\n      <link>https://dev.by/news/roskomnadzor-vnes-telegram-i-livejournal-v-reestr' \
           '-sotssetei</link>\n      <guid>https://dev.by/news/roskomnadzor-vnes-telegram-i-livejournal-v-reestr' \
           '-sotssetei</guid>\n      <enclosure ' \
           'url="https://dev.by/storage/images/13/43/60/19/derived/417ec3d8e36de5a5f2cd5c39a7176c8e.jpg" ' \
           'type="image/jpeg"/>\n    </item>\n    <item>\n      <title>Каждый пятый читатель dev.by потерял коллег ' \
           'из-за ковида</title>\n      <id>tag:dev.by,2021-10-26:21933222</id>\n      <pubDate>Tue, 26 Oct 2021 ' \
           '15:09:00 GMT</pubDate>\n      <lastBuildUpdate>Tue, 26 Oct 2021 15:10:17 GMT</lastBuildUpdate>\n      ' \
           '<category>Четвёртая волна</category>\n      <format>news</format>\n      <description>\r\ndev.by спросил ' \
           'в\xa0телеграме, есть\xa0ли среди сотрудников ИТ-компаний, в\xa0которых работают наши читатели, ' \
           'умершие от\xa0ковида. Цифры впечатляют: почти 20% ответивших (а\xa0их\xa0на\xa0момент публикации\xa0— ' \
           '2350 человек) потеряли коллег. Как минимум одного, но\xa0некоторые указывают, что у\xa0них в\xa0окружении ' \
           'умерло уже более 5 человек.\r\n</description>\n      <author>Отдел новостей</author>\n      ' \
           '<link>https://dev.by/news/umerli-v-kompaniyah-ot-kovida</link>\n      ' \
           '<guid>https://dev.by/news/umerli-v-kompaniyah-ot-kovida</guid>\n      <enclosure ' \
           'url="https://dev.by/storage/images/24/72/81/13/derived/514c2a3f10179da11530877e2d34a3e1.jpg" ' \
           'type="image/jpeg"/>\n    </item></channel>\n</rss>\n '
test_link = 'hps://dev.by/rss/'
test_items = [{'description': '\n'
                              'Регулятор дополнил реестр в\xa0рамках закона о\xa0'
                              'самоконтроле соцсетей.\n',
               'image': 'https://dev.by/storage/images/13/43/60/19/derived'
                        '/417ec3d8e36de5a5f2cd5c39a7176c8e.jpg',
               'link': 'https://dev.by/news/roskomnadzor-vnes-telegram-i-livejournal-v-reestr-sotssetei',
               'pubDate': 'Tue, 26 Oct 2021 16:25:00 GMT',
               'title': 'Роскомнадзор внес Telegram и LiveJournal в реестр соцсетей'}]
test_title = 'dev.by: Все о работе в IT'
test_news_link = 'https://dev.by/news/roskomnadzor-vnes-telegram-i-livejournal-v-reestr-sotssetei'
test_news_broken_link = 'h://dev.by/news/roskomnadzor-vnes-telegram-i-livejournal-v-reestr-sotssetei'


class RssTest(unittest.TestCase):
    def test_parse_xml_no_title(self):
        self.assertEqual(parse_xml('', 1), ('Error! Try to choose a different source. Exit program', []))

    def test_parse_xml(self):
        self.assertEqual(parse_xml(test_xml, 1),
                         ('dev.by: Все о работе в IT',
                          [{'description': '\n'
                                           'Регулятор дополнил реестр в\xa0рамках закона о\xa0'
                                           'самоконтроле соцсетей.\n',
                            'image': 'https://dev.by/storage/images/13/43/60/19/derived'
                                     '/417ec3d8e36de5a5f2cd5c39a7176c8e.jpg',
                            'link': 'https://dev.by/news/roskomnadzor-vnes-telegram-i-livejournal-v-reestr-sotssetei',
                            'pubDate': 'Tue, 26 Oct 2021 16:25:00 GMT',
                            'title': 'Роскомнадзор внес Telegram и LiveJournal в реестр соцсетей'}]))

    def test_parse_xml_0_limit(self):
        self.assertEqual(parse_xml(test_xml, 0), ('dev.by: Все о работе в IT', []))

    def test_get_page_xml(self):
        self.assertEqual(get_page_xml(''), None)

    def test_get_page_xml(self):
        self.assertEqual(get_page_xml(test_link), None)

    def test_parse_news_content(self):
        self.assertEqual(parse_news_content(test_news_link), ('\n\
Регулятор дополнил реестр в рамках закона о самоконтроле соцсетей.'))

    def test_parse_news_content(self):
        self.assertEqual(parse_news_content(test_news_broken_link), 'No description')

# def test_print(self):
#     #self.assertEqual(print_elements(test_title, test_items), None)
