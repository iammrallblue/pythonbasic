# coding:utf-8
# 3/18/21 2:09 PM

"""
    while statement instance:
"""

# x = 10
# while x > 9:
#     x -= 1
#     print("...")
#     print(x)

count = 0
while count < 3:
    print("{} attempt(s)".format(count + 1))
    user_input = input(">:")

    if not user_input:  # input is not integer, print out warning
        print("Input is invalid, Only Numbers")
        continue
        pass
    int_val = int(user_input)

    if int_val > 18:
        print("too larger.")
        pass
    elif int_val < 18:
        print("too small.")
        pass
    else:
        print("bingo.")
        break
        pass
    if count == 3:
        print("continue, enter y, exit enter n")
        reset_count = input("input y/Y or n/N:")
        if reset_count == "y" or reset_count == "Y":
            count = 0
        else:
            exit()
    count += 1
