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
import math

# # the sum of numbers from 0 to 100
# number = 0
# for x in range(101):
#     # print(x)
#     number += x  # accumulate numbers adding
#     pass
# print(number)
#
# # return the accumulating of ODD numbers from 0 to 100
# value = 0
# for y in range(0, 101, 2):
#     # print(y)
#     value += y
#     pass
# print(value)
#
# # return the accumulating of ODD numbers from 0 to 100 by for loop statement
# odd_number = 0
# for z in range(1, 101):
#     if z % 2 == 0:
#         odd_number += z
#         pass
# print(odd_number)
#
# # multiplication table
# for x in range(0, 10):
#     for y in (1, x + 1):
#         print("%d*%d=%d" % (x, y, x * y), end="\t")
#         pass
#     print()
#     pass
#
# # determine a number whether prime number or not
# number = int(input("input an integer: "))
# value = int(sqrt(number))
# print(value)
# is_prime = True
# for x in range(2, value + 1):
#     if number % x == 0:
#         is_prime = False
#         break
#         pass
# if is_prime and number != 1:
#     print("%d is a prime number." % number)
#     pass
# else:
#     print("%d is not a prime number." % number)
#     pass
#
# # GCD and LCM
# x = int(input("x = "))
# y = int(input("y = "))
# if x > y:
#     x, y = y, x
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print("The GCD of %d and %d is: %d" % (x, y, factor))
#         print("The LCM of %d and %d is: %d" % (x, y, factor))
#         break
#     pass
#
# # print out specified shape by for..in statement
# row = int(input("input the number of row: "))
# for i in range(row):
#     for m in range(i + 1):
#         print("*", end="")
#         pass
#     print()
#
# for x in range(row):
#     for y in range(row):
#         if y < row - x - 1:
#             print(" ", end="")
#         else:
#             print("*", end="")
#             pass
#     print()
#
# for x in range(row):
#     for n in range(row - x - 1):
#         print(" ", end=" ")
#         pass
#     for m in range(2 * x + 1):
#         print("*", end=" ")
#         pass
#     print()
#
# # A rooster is $5, A hen is %3, Three chicks is %1
# for x in range(0, 20):
#     for y in range(0, 33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z / 3 == 100:
#             print("Rooster: %d" % x)
#             print("Hen: {}".format(y))
#             print("Chick: ", z)
#             pass

# # Fibonacci Sequence
# fi_sequence = [1, 1]  # <class 'list'>
# print(type(fi_sequence))
# while len(fi_sequence) < 20:
#     fi_sequence.append(fi_sequence[-1] + fi_sequence[-2])
#     pass
# print(fi_sequence)
# print(len(fi_sequence))
#
# # Fibonacci Sequence 2
# x = 0
# y = 1
# for i in range(20):
#     x, y = y, x + y
#     print(x, end=" ")
#     pass


# Perfect number within 10000
# perfect_number = []
# # iterating from 1 to 10000
# for i in range(1, 10000):
#     number_list = []
#     for j in range(1, i):
#         if i % j == 0:
#             number_list.append(j)
#             pass
#     if sum(number_list) == i:
#         number_list.append(i)
#         print(perfect_number)

# # Perfect number list
# # define numbers function
# def numbers(number):
#     numbers_sum = 0
#     number_list = list()  # <class 'list'>
#
#     for x in range(1, number):  # range(1,6)
#         if number % x == 0:
#             number_list.append(x)
#         else:
#             continue
#     for y in number_list:
#         numbers_sum += y
#     if numbers_sum == number:
#         print(number)
#
#
# for z in range(6, 10000):
#     numbers(z)

# # find prime numbers
# value = 2
# while value < 100:
#     x = 2
#     while x <= (value / x):
#         if value % x == 0:
#             break
#             pass
#         x = x + 1
#     if x > value / x:
#         print(value, "is a prime number")
#         pass
#     value = value + 1
# print("prime numbers from 0 to 100")

# # find all prime number solution 2
# numbers = range(2, 101)  # <class 'range'>
# for x in range(2, 101):
#     for y in range(2, 101):
#         result = x * y
#         pass
#     if result < 101:
#         if numbers.count(result) > 0:
#             numbers.remove(result)
#
# temp = ""
# for z in numbers:
#     temp += " " + str(z)
#     pass
# print(temp)

# find all prime numbers solution 3
for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
