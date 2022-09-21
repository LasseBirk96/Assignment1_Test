import numpy as np
import pandas as pd

map_of_numbers = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def convert_arabic_to_roman(arabic_number):
    roman_number = ''
    while arabic_number > 0:
        for i, r in map_of_numbers:
            while arabic_number >= i:
                roman_number = roman_number +  r
                arabic_number = arabic_number - i
    return roman_number


