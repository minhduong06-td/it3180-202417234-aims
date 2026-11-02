import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class SearchTest(unittest.TestCase):
    def test_search_case_insensitive(self):
        discs = [DigitalVideoDisc('The Lion King')]
        self.assertEqual(len(search_by_title(discs, 'lion')), 1)

    def test_search_by_title(self):
        discs = [DigitalVideoDisc('The Lion King'), DigitalVideoDisc('Star Wars')]
        self.assertEqual([d.title for d in search_by_title(discs, 'Star')], ['Star Wars'])
