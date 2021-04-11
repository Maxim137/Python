import doctest
import unittest

import potentialproject

class NumbersTestCase(unittest.TestCase):
    def test_1(self):
        a1 = 5
        a2 = 4
        a3 = 3
        x_min = 5
        x_max = 10
        y_min = 4
        y_max = 9
        expect = True
        self.assertTrue(potentialproject.check(a1, a2, a3, x_min, x_max, y_min, y_max), msg='Combination: a1 = {a1}, a2 = {a2}, a3 = {a3}, x_mix = {x_min}, x_max = {x_max}, y_min = {y_min}, y_max = {y_max} should work')

    def test_2(self):
        a1 = 5
        a2 = 7
        a3 = 3
        x_min = 5
        x_max = 10
        y_min = 4
        y_max = 9
        expect = True
        self.assertEqual(potentialproject.check(a1, a2, a3, x_min, x_max, y_min, y_max), expect, f'Combination: a1 = {a1}, a2 = {a2}, a3 = {a3}, x_mix = {x_min}, x_max = {x_max}, y_min = {y_min}, y_max = {y_max} will not work')

    def test_3(self):
        a1 = 5
        a2 = 4
        a3 = 3
        x_min = 4
        x_max = 10
        y_min = 4
        y_max = 9
        expect = True
        self.assertEqual(potentialproject.check(a1, a2, a3, x_min, x_max, y_min, y_max), expect, f'Combination: a1 = {a1}, a2 = {a2}, a3 = {a3}, x_mix = {x_min}, x_max = {x_max}, y_min = {y_min}, y_max = {y_max} will not work')
        
if __name__ == '__main__':
    unittest.main()
