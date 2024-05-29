import unittest

from .sorted_squared_array import sorted_squared_array


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        actual = sorted_squared_array(input)
        self.assertEqual(actual, expected)
