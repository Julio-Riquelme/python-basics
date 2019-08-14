import unittest
from roman_numbers import roman_to_decimal


class testromannumbers(unittest.TestCase):
    def test_roman_i_to_decimal(self):
        decimal_number = roman_to_decimal('i')
        self.assertEqual(decimal_number, 1)


if __name__ == '__main__':
    unittest.main()
