"""
    for loop statement:
        For Loop is used to repeat a block of statements until there is no items in Object
        may be String, List, Tuple or any other object.
        format:
            for temp_var in object
                expr_1
                expr_2
        Key point:
            1. function range() (usually using with for loop statement)
                The range() function returns a sequence of numbers, starting from 0 by default,
                and increments by 1 (by default), and stops before a specified number.
            2. if statement (usually using with for loop statement)

            3. break, continue keywords.
                break:
                    The break keyword is used to break out a for loop, or a while loop.
                    it terminates the whole for loop,
                continue:
                    the continue keyword is used to skip the current loop, or a while loop,
                    it ONLY skips current loop once, then keep running til finish whole program.
            4. for loop can use with else
"""

# # iterating a string by for loop statement
slogan = "Bella is my wife."  # "Bella is my wife" is the object of iteration.
for letter in slogan:
    # print(letter, end=" ") # don't change line
    print(letter, end=" ")  # keep all letters in one line
    pass
print()

# # iterating a built-in range() function by for loop statement
# range(start, end) end can't be zero
numbers = range(1, 21)  # [1,21)
for num in numbers:
    print(num, end=" ")  # print out 1 to 20
    pass

print("\n", type(range(1)))  # <class 'range'>, the object of class range.

# int can't be iterated
# for i in 11324:
#     print(i) # TypeError: 'int' object is not iterable
#     pass

# # printing the sum of numbers from 1 to 100,
# total = 0
# for number in range(1, 101):  # the end is 101, b/c [1, 101)
#     total += number  # sum 1 to 100
#     pass
#
# print("the accumulation of 1 to 100 is: %d" % total)

# # finding all even numbers from 50 to 200 by for loop and if statement
# for number in range(50, 201):  # [50,201)
#     if number % 2 == 0:
#         print("Even numbers: %d" % number)
#         pass
#     else:
#         print("Odd numbers: %d" % number)
#         pass
# pass

# keyword break in for loop statement
# # when accumulation of sum is reached to 100,
# break for loop, which means terminated for loop
accum_sum = 0
for num in range(1, 51):  # (1,51]
    if accum_sum > 100:
        print("for loop is terminated, because sum accumulated to %d" % num)  # a hint
        break  # accu_sum is reached to 100, exit for loop
        pass
    accum_sum += num
    pass
print("the accumulation is %d" % accum_sum)
pass

# a continue in for loop statement
# # skipping all even number by using continue and for loop
for numbers in range(1, 101):  # (1,101]
    if numbers % 2 == 0:  # find all even number
        continue  # skipp even numbers
        pass
    print("Odd numbers: %d" % numbers)
    pass
print("for loop ended")
pass

# skipping specified letter by using continue and for loop
for letters in "Bella is my wife":  # "Bella is my wife" is an iterating object
    if letters == 's':
        continue  # skipping letter "s", keep going
        # break # break out the whole for loop
        pass
    print(letters, end=" ")
    pass

# # printing a Chinese Multiplication table by nested for loop
# x * y = z
for x in range(1, 10):  # [1,10)
    for y in range(1, x + 1):  # [1, x+1)
        print("%d * %d = %d" % (y, x, x * y), end=" ")  # end="" keep in one line
        pass
    print()  # new line
    pass
pass

# for loop with else
# when user and password input are over 3 times, using else to inform users try again after 3 minutes
user_id = "Bella"
passwd = "999"
for i in range(3):  # 3 attempts for login
    input_userid = input("Enter your user name: ")
    input_passwd = input("Enter your password: ")
    if input_userid == user_id and input_passwd == passwd:  # if user id and password both are matched.
        print("%s, login successful" % input_userid)
        break  # if login successful, break for loop
        pass
    pass
else:
    print("you have attempted 3 times. try again 3 minutes later")
    pass

# for loop print out Even numbers
for i in range(0, 10, 2):  # [0,10), [include 0, not include 10), 2 is step by 2
    print(i)
