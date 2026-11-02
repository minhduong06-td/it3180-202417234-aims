import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class SortTest(unittest.TestCase):
    def make_cart(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc('Zebra', cost=7))
        cart.add_dvd(DigitalVideoDisc('Alpha', cost=15))
        return cart

    def test_sort_by_title(self):
        cart = self.make_cart()
        cart.sort_by_title()
        self.assertEqual([d.title for d in cart.items], ['Alpha', 'Zebra'])

    def test_sort_by_cost(self):
        cart = self.make_cart()
        cart.sort_by_cost()
        self.assertEqual([d.cost for d in cart.items], [7, 15])
