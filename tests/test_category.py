import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class CategorySearchTest(unittest.TestCase):
    def test_search_by_category(self):
        discs = [DigitalVideoDisc('Lion', category='Animation'),
                 DigitalVideoDisc('Star Wars', category='Science Fiction')]
        self.assertEqual([d.title for d in search_by_category(discs, 'Animation')], ['Lion'])
