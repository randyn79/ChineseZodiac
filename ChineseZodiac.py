#!/usr/bin/env python3

import datetime

def chinese_zodiac(year: int) -> str:
    """Accepts a year as an int.  Returns the corresponding Chinese Zodiac sign for
the corresponding year as a str."""

    # Check to see if the year is a positive integer.
    if not isinstance(year, int):
        raise TypeError('Input must be an integer')
    if year < 1:
        raise ValueError('Input must be greater than zero')

    signs = ('Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox',
             'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat')

    return signs[year % 12]

def chinese_zodiac_prior(year: int) -> list:
    """Accepts a year as an int.  Returns the previous 10 years that the Chinese Zodiac
would have the same sign (every 12 years) as a list."""

    # Check to see if the year is a positive integer.
    if not isinstance(year, int):
        raise TypeError('Input must be an integer')
    if year < 1:
        raise ValueError('Input must be greater than zero')

    return [(year - (12 * i)) for i in range(1, 11)]

def chinese_zodiac_future(year: int) -> list:
    """Accepts a year as an int.  Returns the next 10 years that the Chinese Zodiac
would have the same sign (every 12 years) as a list."""

    # Check to see if the year is a positive integer.
    if not isinstance(year, int):
        raise TypeError('Input must be an integer')
    if year < 1:
        raise ValueError('Input must be greater than zero')

    return [(year + (12 * i)) for i in range(1, 11)]
    
        
if __name__ == "__main__":
    print()
    print('=' * 14)
    print('CHINESE ZODIAC')
    print('=' * 14)
    print()
    year = int(input("Enter the year:  "))
    print()
    entered_year_sign = chinese_zodiac(year)
    print(f'The Chinese Zodiac sign for {year} is the {entered_year_sign}')
    print()
    prior_years = chinese_zodiac_prior(year)
    print(f'The ten previous years of the {entered_year_sign} were {prior_years}.')
    print()
    future_years = chinese_zodiac_future(year)
    print(f'The next ten years of the {entered_year_sign} are {future_years}.')
    print()
    current_year = datetime.datetime.now().year
    current_year_sign = chinese_zodiac(current_year)
    print(f'The current year of {current_year} is the year of the {current_year_sign}.')
    
    
