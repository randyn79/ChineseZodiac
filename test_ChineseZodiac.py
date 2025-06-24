#!/usr/bin/env python3

import unittest
import ChineseZodiac

class TestChineseZodiac(unittest.TestCase):

    def test_chinese_zodiac(self):
        """Tests the ChineseZodiac.chinese_zodiac function."""
        # Exception raised if a year is not a positive integer
        self.assertRaises(TypeError, ChineseZodiac.chinese_zodiac, 2.3)
        self.assertRaises(TypeError, ChineseZodiac.chinese_zodiac, 'hello')
        self.assertRaises(ValueError, ChineseZodiac.chinese_zodiac, -1)
        self.assertRaises(ValueError, ChineseZodiac.chinese_zodiac, 0)

        # Test correct output datatype
        self.assertIsInstance(ChineseZodiac.chinese_zodiac(1900), str)

        # Test correct output based on input
        self.assertEqual(ChineseZodiac.chinese_zodiac(2022), 'Tiger')
        self.assertEqual(ChineseZodiac.chinese_zodiac(2021), 'Ox')
        self.assertEqual(ChineseZodiac.chinese_zodiac(2020), 'Rat')
        self.assertEqual(ChineseZodiac.chinese_zodiac(2019), 'Pig')
        self.assertEqual(ChineseZodiac.chinese_zodiac(2018), 'Dog')
        self.assertEqual(ChineseZodiac.chinese_zodiac(2017), 'Rooster')
        self.assertEqual(ChineseZodiac.chinese_zodiac(2016), 'Monkey')
        self.assertEqual(ChineseZodiac.chinese_zodiac(2015), 'Goat')
        self.assertEqual(ChineseZodiac.chinese_zodiac(2014), 'Horse')
        self.assertEqual(ChineseZodiac.chinese_zodiac(2013), 'Snake')
        self.assertEqual(ChineseZodiac.chinese_zodiac(2012), 'Dragon')
        self.assertEqual(ChineseZodiac.chinese_zodiac(2011), 'Rabbit')

    def test_chinese_zodiac_prior(self):
        """Tests the ChineseZodiac.chinese_zodiac_prior function."""
        # Exception raised if a year is not a positive integer
        self.assertRaises(TypeError, ChineseZodiac.chinese_zodiac, 2.3)
        self.assertRaises(TypeError, ChineseZodiac.chinese_zodiac, 'hello')
        self.assertRaises(ValueError, ChineseZodiac.chinese_zodiac, -1)
        self.assertRaises(ValueError, ChineseZodiac.chinese_zodiac, 0)

        # Test correct output datatype
        self.assertIsInstance(ChineseZodiac.chinese_zodiac_prior(1900), list)

        # Test correct output based on input
        self.assertEqual(ChineseZodiac.chinese_zodiac_prior(2022),
                         [2010, 1998, 1986, 1974, 1962, 1950, 1938, 1926, 1914, 1902])
        self.assertEqual(ChineseZodiac.chinese_zodiac_prior(1900),
                         [1888, 1876, 1864, 1852, 1840, 1828, 1816, 1804, 1792, 1780])
        

    def test_chinese_zodiac_future(self):
        """Tests the ChineseZodiac.chinese_zodiac_future function."""
        # Exception raised if a year is not a positive integer
        self.assertRaises(TypeError, ChineseZodiac.chinese_zodiac, 2.3)
        self.assertRaises(TypeError, ChineseZodiac.chinese_zodiac, 'hello')
        self.assertRaises(ValueError, ChineseZodiac.chinese_zodiac, -1)
        self.assertRaises(ValueError, ChineseZodiac.chinese_zodiac, 0)

        # Test correct output datatype
        self.assertIsInstance(ChineseZodiac.chinese_zodiac_future(1900), list)

        # Test correct output based on input
        self.assertEqual(ChineseZodiac.chinese_zodiac_future(2022),
                         [2034, 2046, 2058, 2070, 2082, 2094, 2106, 2118, 2130, 2142])
        self.assertEqual(ChineseZodiac.chinese_zodiac_future(1900),
                         [1912, 1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020])

if __name__ == "__main__":
    unittest.main()
