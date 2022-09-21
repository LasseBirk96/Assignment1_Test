import unittest
from Temperature_converter import convert_celsius_to_fahrenheit, convert_fahrenheit_to_celsius
from Arabic_to_roman_numerals_converter import convert_arabic_to_roman
class TestSum(unittest.TestCase):

    #TEST OF TEMPERATURE CONVERTER
    def test_convert_celsius_to_fahrenheit(self):
        self.assertEqual(convert_celsius_to_fahrenheit(40), 104, "Should be 104")

    def test_convert_fahrenheit_to_celsius(self):
        self.assertEqual(convert_fahrenheit_to_celsius(90), 32.22, "Should be 32.22")

    #TEST OF ARABIC TO ROMAN CONVERTER
    def test_convert_arabic_to_roman(self):
        self.assertEqual(convert_arabic_to_roman(32), "XXXII", "Should be XXXII")
    
if __name__ == '__main__':
    unittest.main()
    