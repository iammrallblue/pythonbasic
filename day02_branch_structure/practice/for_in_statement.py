# coding:utf-8
# 4/7/21 11:22 AM

"""
    for in statement:
        Key point:
            1. range() function
                range(101)：return the number range [0,101) or (0,100)
                range(1, 101)：return the number range [1,101) of (1,100)
                range(1, 101, 2)：return the number range [1,101) by step 2, which numbers are ODD
                range(100, 0, -2)：
"""
from math import sqrt

# the sum of numbers from 0 to 100
number = 0
for x in range(101):
    # print(x)
    number += x  # accumulate numbers adding
    pass
print(number)

# return the accumulating of ODD numbers from 0 to 100
value = 0
for y in range(0, 101, 2):
    # print(y)
    value += y
    pass
print(value)

# return the accumulating of ODD numbers from 0 to 100 by for loop statement
odd_number = 0
for z in range(1, 101):
    if z % 2 == 0:
        odd_number += z
        pass
print(odd_number)

# multiplication table
for x in range(0, 10):
    for y in (1, x + 1):
        print("%d*%d=%d" % (x, y, x * y), end="\t")
        pass
    print()
    pass

# determine a number whether prime number or not
number = int(input("input an integer: "))
value = int(sqrt(number))
print(value)
is_prime = True
for x in range(2, value + 1):
    if number % x == 0:
        is_prime = False
        break
        pass
if is_prime and number != 1:
    print("%d is a prime number." % number)
    pass
else:
    print("%d is not a prime number." % number)
    pass

# GCD and LCM
x = int(input("x = "))
y = int(input("y = "))
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print("The GCD of %d and %d is: %d" % (x, y, factor))
        print("The LCM of %d and %d is: %d" % (x, y, factor))
        break
    pass
