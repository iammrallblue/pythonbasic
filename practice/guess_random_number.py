"""
    guessing random number
    range of number 0 ~ 10


"""
import random
# random a number then assign to ran_number variable
ran_number = random.randint(0, 10)
print(ran_number)
# check random number

user_guess = int(input("what is your guessing number: "))
if ran_number > user_guess:
    print("your guessing number is small.")
elif ran_number < user_guess:
    print("your guessing number is big.")
elif ran_number == user_guess:
    print("bingo, you won.")
else:
    print("something wrong.")
