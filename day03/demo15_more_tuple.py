# coding:utf-8
# 3/22/21 11:37 AM

"""
    continue
        tuple type

        Key point:
            1. for loop inside of the list as an element
            2. for loop goes with if statement
"""

str_name = "Hello, Bella"
# empty list
list_l = []
# for i in str_name:
#     list_l.append(i)
#     pass
# print(list_l)

# simplest way to add all elements of str_name to the list (list_l)
list_l = [i for i in str_name]  # for loop inside the list as an element
print(list_l)

list_for = [i for i in str_name if i == "B" or i == "H"]
# if statement
print(list_for)
