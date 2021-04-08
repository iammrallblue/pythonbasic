# coding:utf-8
# 4/7/21 11:40 AM

"""
    Guessing Number
"""

import random

random_number = random.randint(0, 100)
counter = 0
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

