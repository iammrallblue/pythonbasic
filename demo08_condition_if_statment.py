import random

"""
    2. Selection Structure/Condition Control Structure
            a. if statement (single if)
                format:
                    if cond_expr:
                        expr_1
                        expr_2
                        ...
            b. if...else statement
                format:
                    if cond_expr:
                        expr_1
                        expr_2
                        ...
                    else:
                        expr_3
                        expr_4
                        ...
            c. multiple if...elif...elif...elif...else
                format:
                    if cond_expr:
                        expr_1
                        expr_2
                        ...
                    elif cond_expr_2:
                        expr_3
                        expr_4
                    elif con_expr_3:
                        expr_5
                        expr_6
                    else:
                        expr_7
                        expr_8
            d. nested if... else statement
                format:
                    if cond_expr_1:
                        expr_1
                        if nested_cond_expr_1:
                            nested_expr_1
                    elis cond_expr_2:
                        expr_2
                    
            Key point:
                1. cond_expr can be Logic, Comparison, Assignment, Operators.
                2. indentation, expressions MUST have a indent at beginning of expressions.
                (see print("x is greater than y."))
                (see if-statements in condition_if_statement.py
        pass statement:
            The pass statement is a null operation; nothing happens when it executes.
            The pass is also useful in places where your code will eventually go.
"""
# # if statement (single if)
# x = 50
# y = 20
# if x > y:
#     print("x is greater than y.")
#     pass  # empty statement, when condition is true, it will execute.
#     print("this is pass code block")
#
# # if ... else statement
# age = 40
# if age >= 40:
#     print("middle age.")
#     pass
# else:
#     print("young age.")
#     pass

# multiple if...elif...elif...else:
# score querying instance by using if...elif... else statement
score = int(input("What is your score: "))
if 90 <= score <= 100:
    print("you've got A.")
    pass
elif 80 <= score <= 89:
    print("you've got B.")
    pass
elif 70 <= score <= 79:
    print("you've got C.")
    pass
elif 60 <= score <= 69:
    print("you've got D.")
    pass
else:
    print("you failed.")
    pass
print("Query is completed.")
pass

# roshambo, paper,scissors, rock instance by using if...elif... else statement
# 0 = rock, 1 = scissors, 2 = paper.
# two players, computer and user
user = int(input("0:rock, 1:scissors, 2:paper"))
computer = random.randint(0, 2)
if user == 0 and computer == 1:  # rock smashed scissors
    print("you won!")
    pass
elif user == 1 and computer == 2:  # scissors cuts paper
    print("you won!")
    pass
elif user == 2 and computer == 0:  # paper covers rock
    print("you won!")
    pass
elif user == computer:     # break even,
    print("break even, again!")
else:
    print("computer won!")
print("Computer got: ", computer)
print("You got: ", user)

# nested if...else statement
# determine a received number whether a positive or negative
number = float(input("Enter a number: "))
if number > 0:
    if number == 0:
        print("the number is a zero")
        pass
    else:
        print("the received number is a positive number")
        pass
else:
    print("the received number is a negative number")
    pass

# nested if... if... else by satisfying two conditions
credit_hour = float(input("Enter your total credit hour: "))
if credit_hour > 128.0:
    gpa = float(input("Enter your GPA: "))
    if gpa > 2.0:
        print("Congratulation! You can graduate!")
        pass
    else:
        print("Your GPA is too low, need to fix it.")
        pass
else:
    print("Your total credit hours are not satisfied.")
    pass
