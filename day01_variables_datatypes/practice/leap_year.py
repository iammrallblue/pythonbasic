# coding:utf-8
# 3/31/21 11:56 AM

"""
    Leap year Determination
"""

leap_year = int(input("Input a particular year: "))
is_year = leap_year % 4 == 0 and leap_year % 100 != 0 or leap_year % 400 == 0
print(is_year)