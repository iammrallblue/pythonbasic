# coding:utf-8
# 4/7/21 11:40 AM

"""
    Guessing Number
"""

import random

random_number = random.randint(0, 100)
counter = 0
print(random_number)
while True:
    counter += 1
    guessing_number = int(input("Guessing Number: "))
    if guessing_number > random_number:
        print("Guessing Number is too large.")
        pass
    elif guessing_number < random_number:
        print("Guessing Number is too small.")
        pass
    else:
        print("Bingo. ")
        break
        pass
print("Guessing %d times." % counter)
if counter > 7:
    print("Too many attempts")
    pass

# reverse an integer
number = int(input("input an integer: "))
reverse_number = 0
while number > 0:
    reverse_number = reverse_number * 10 + number % 10
    number //= 10
    pass
print(reverse_number)
