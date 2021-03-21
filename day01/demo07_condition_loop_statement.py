# coding:utf-8
# 3/18/21 7:47 AM
"""
    while statement,
    if statement,
    if ... else statement,
    if ... elif ... statement
    break, ONLY inside of the loop statement
    continue


"""
while True:

    user = input("Enter user name:")
    if user == "root":
        print("root is user name")
        break
        pass
    else:
        print(type(user))  # input will always be str type
        if user == "":
            print("user name can't be EMPTY")
            continue
            pass
        elif user == " ":
            print("user name can't be SPACE")
            continue
        print("Finish")

print("out of if statement.")

print(len(" 44S$   "))  # length of the string is 8

print(not 0)  # True
print(not "0")  # False
print(0)
