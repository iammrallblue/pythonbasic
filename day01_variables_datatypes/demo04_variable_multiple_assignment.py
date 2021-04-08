# coding:utf-8
# 3/17/21 2:29 PM

"""
    Variable Multiple Assignment:
        1. assign values to multiple variables in one line
        2. assign the same value to multiple variables in one line:

    Syntax:
        x, y, z = "Orange", "Banana", "Cherry"
        x = y = z = "Orange"
    Key point:
        1. the variables and the values should be equal.
            x,y = 1,2
        2. if the variables and the values are not equal
            we need to put * in front of the the first variable
            *x,y = 1,2,3
        3. *x, will come a list[]
"""

# assign different values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)

# assign same value to multiple variables
x = y = z = "Orange"
print(x, y, z)

# variable and values are not equal
*m, n = 1, 2, 3
print(type(m))  # <class 'list'>
print(type(n))  # <class 'int'>

print(*m)  # 1,2, show all elements in the list
print(m)  # [1,2] ,show whole list,
print(n)  # 3
