"""
    + * in for string, list, tuple, dict, set
        +
            to joint two or more strings
        *
            copy data by the specific number.
        in
            check if object whether exists or not in the dict
"""
# + strings
str_a = "Hello"
str_b = "Bella"
print(str_a + str_b)  # HelloBella

# + list
list_a = list(range(3))
list_b = list(range(21, 25))
print(list_a + list_b)  # [0, 1, 2, 21, 22, 23, 24]

# * strings
print(str_a * 3)  # HelloHelloHello

# * lists
print(list_a * 2)

# in string
print("B" in str_a)  # False
print("0" in list_a)  # False


