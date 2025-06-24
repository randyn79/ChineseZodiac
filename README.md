# ChineseZodiac

Determines the Chinese Zodiac sign for a particular year and displays the previous ten and next ten years that have this sign, as well as the Chinese Zodiac sign for the current year.

## Notes

This is based on the solar calendar and not the lunar calendar.  Years are intended to be entered as positive integers and should raise exceptions otherwise.

## Files & Functions

### ChineseZodiac.py

#### chinese_zodiac() function

Accepts a year as an int.  Returns the corresponding Chinese Zodiac sign for the corresponding year as a str.

#### chinese_zodiac_prior() function

Accepts a year as an int.  Returns the previous 10 years that the Chinese Zodiac would have the same sign (every 12 years) as a list.

#### chinese_zodiac_future() function

Accepts a year as an int.  Returns the next 10 years that the Chinese Zodiac would have the same sign (every 12 years) as a list.


### test_ChineseZodiac.py

#### test_chinese_zodiac() function

Unittests for the ChineseZodiac.chinese_zodiac() function

### test_chinese_zodiac_prior() function

Unittests for the ChineseZodiac.chinese_zodiac_prior() function

### test_chinese_zodiac_future() function

Unittests for the ChineseZodiac.chinese_zodiac_future() function

### To Do
Clean up test cases.
