import unittest
from rss_reader import parse_xml


class RssTest(unittest.TestCase):

    def test_parse_xml(self):
        self.assertEqual(parse_xml(''), '')

    pass
