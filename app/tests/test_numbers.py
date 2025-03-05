# -*- coding: utf-8 -*-

import unittest
from app.models.numbers import Numbers

class TestNumbersClass(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(Numbers([1, 2, 3, 4, 5]).sum(), 15)
        self.assertEqual(Numbers([-1, -2, -3]).sum(), -6)
        self.assertEqual(Numbers([]).sum(), 0)

    def test_average(self):
        self.assertEqual(Numbers([1, 2, 3, 4, 5]).average(), 3)
        self.assertEqual(Numbers([-10, 0, 10]).average(), 0)
        with self.assertRaises(ValueError):
            Numbers([]).average()

if __name__ == '__main__':
    unittest.main()