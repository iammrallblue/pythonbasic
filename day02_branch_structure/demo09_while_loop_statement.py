import random

"""
    While loop:
        format:
            while cond_expr:
                expr_1
                expr_2
                
        Key point:
            1. while loop must have an initial value, condition expression, and increment and decrement
                inside of the while loop
            1. while statement can use with else 
                else, the block of code will run once at the end.
                when the while statement condition will no longer true
            2. continue and break ONLY use inside of loop block. 
                exit()
                continue
                break
            3. while loop statement always uses in a unspecified loop, 
                for loop statement always uses in a determined loop frequency
            
                
        count number.
            (see instance)
        guessing number
            users have 5 times to input guessing number,
             if users is bingo within 5 times. the program have to exit after numbers matched.
             solution:
               1. exit()
               2. break while loop
               3. continue, stop current loop (only one time)
               the difference btw exit and break,
                exit() will close whole program, print(random number) will not execute
                break will ONLY terminate while loop. print(random number) will execute.
        dead loop:
            while True:
"""
# control while statement
x = 10
while x > 5:
    x -= 1
    print("while loop", x)
    pass
print("x = %d while loop is terminated. " % x)
pass

# # print 0 ~ 100 by while loop
# counter = 1  # counter for counting
# while counter <= 100:
#     print(counter)
#     pass
#     counter += 1

# count = 1
# while count <= 100:
#     print(count)
#     count += 1
#     # determine ODD and EVEN number
# if count % 2 == 0:
#     print("even number: ", count)
# else:
#     print("odd number", count)
# count += 1

# # set a game running 10 times by while loop
# # to improve the game rock scissors paper
# counter = 1
# while counter <= 10:
#     user = int(input("0 Rock, 1 Scissors, 2 Paper"))
#     computer = random.randint(0, 2)
#     if user == 0 and computer == 1:
#         print("You won.")
#         pass
#     elif user == 1 and computer == 2:
#         print("You won.")
#         pass
#     elif user == 2 and computer == 0:
#         print("You won.")
#         pass
#     elif user == computer:
#         print("break even, try again")
#         pass
#     else:
#         print("Computer won.")
#     print("computer got: ", computer)
#     print("you got: ", user)
#     counter += 1

# # instance of Chinese multiplication table by nested while loop statement
# row = 9
# while row >= 1:
#     column = 1
#     while column <= row:
#         print("%d * %d = %d" % (column, row, column * row), end= "  ")
#         column += 1
#         pass
#     print()
#     row -= 1
#     pass

# # instance of print out a right triangle by nested while loop statement
row = 1  # first row
while row <= 7:  # the max of row is 7
    column = 1  # first column
    while column <= row:
        print("*", end=" ")  # print row - column * for each while loop
        column += 1
        pass
    print()  # go next line to print.
    row += 1
# """
# result
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# """

# # instance of print out a reverse right triangle by nested while loop statement
row = 7  # first row
while row >= 1:
    column = 1  # first column,
    while column <= row:
        print("*", end=" ")
        column += 1
        pass
    print()
    row -= 1

# # print out an isosceles triangle by nested while loop statement
# 1. print out two kinds of symbol, one is empty space which is decrement, (empty_space <= 5 - row)
# anther is *, which is increment. (column <= 2 * row - 1)
row = 1
while row <= 10:
    empty_space = 1
    while empty_space <= 10 - row:  # print empty space on left side of isosceles triangle
        print(" ", end="")
        empty_space += 1
        pass
    column = 1
    while column <= 2 * row - 1:  # print star *
        print("*", end="")
        column += 1
        pass
    right_empty_space = 1
    while right_empty_space <= 10 - row:  # empty space on the right side.
        print(" ", end="")
        right_empty_space += 1
        pass
    print()
    row += 1

# # instance of guessing number
# # generating a random number then assign to variable ran_number
# ran_number = random.randint(0, 10)
#
# counter = 0
# # counter > 5 users have 5 chances to guess number
# while counter < 5:
#     # users input a guessing number
#     user_number = int(input("input your guessing number: "))
#
#     # determine both number are match or not.
#     if ran_number > user_number:
#         print("your guessing number is too small, try again")
#     elif ran_number < user_number:
#         print("your guessing number is too big, try again")
#     elif ran_number == user_number:
#         print("Bingo, you got it.")
#         exit()
#         # break
#     else:
#         print("Something wrong!")
#     counter += 1
# print("the random number is: ", ran_number)


# # keyword continue
# # print out number from 0 to 100, except 10 to 20
# counter = 0
# while counter < 100:
#     counter += 1
#     # using continue to skip number from 10 to 20
#     if 10 <= counter <= 20:
#         continue
#         # break
#     print(counter)
#     # result skipped 10 to 20 number
# else:
#     print("If you see me, the program terminated without errors.")
#     # when using a break in block of code, else statement will not execute
#     # at the end.
#
# # while ... else statement
# x = 0
# while x < 6:
#     print(x)
#     x += 1
# else:
#     print("while loop is no longer true")

# # dead while loop
# while True:
#     print("it's a dead loop")
