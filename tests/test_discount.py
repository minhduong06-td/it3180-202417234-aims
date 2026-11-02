import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class DiscountTest(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc('Demo', cost=100))

    def test_20_percent_discount(self):
        self.assertAlmostEqual(self.cart.total_cost_with_discount(20), 80)

    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            self.cart.total_cost_with_discount(150)
