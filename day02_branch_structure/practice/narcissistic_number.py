# coding:utf-8
# 4/8/21 1:49 PM

"""
    narcissistic number:

"""

for number in range(100, 2001):
    low = number % 10
    mid = number // 10 % 10
    high = number // 100
    # print(low)
    if number == low ** 3 + mid ** 3 + high ** 3: # low ** 3 (low^3)
        print(number)
        pass
