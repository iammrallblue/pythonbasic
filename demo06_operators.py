"""
    Operators:
      Arithmetic:
        1. +, -, *, /
        2. %
        3. **, //
      Comparison Operators:
        1. ==
        2. !=
        3. >
        4. <
        5. >=
        6. <=
      Assignment Operators:
        1. =, +=, -=, *=, /=
        2. %=, **=, //=
      Logic Operators:
        1. and
        2. or
        3. not
"""
# declare two variables x, and y.
x = 10
y = 2

# Plus, Minus, Multiple, Division.
x_plus_y = x + y
print(x_plus_y)

# Modulus
x_modulus_y = x % y
print("x modulus y: ", x_modulus_y)  # 0

# Exponentiation x ** y
x_to_y = x ** y
print(x_to_y)  # 10^2 = 100

# Floor Division
flo_div = y // x  # 2/10 = 0
print("floor division: ", flo_div)

"""
    Comparison Operators:
        1. ==
        2. !=
        3. >
        4. <
        5. >=
        6. <=
"""
# Comparison Operators:
x, y = 3, 4
print(x == y)  # False
print(x != y)  # True
print(x >= y)  # False
print(x <= y)  # True
print(x > y)  # False
print(x < y)  # True

"""
    Logic operators:
        1. and
        2. or
        3. not
"""
# Logic Operators:
x, y, z = 3, 2, 3

# logic and
print(x + y > z and z + y < x)  # False
# False and False is False

# logic or
print(x + y < z or x * z > y)  # True
# False or True is True

"""
    Assignment Operators:
        1. =, +=, -=, *=, /=
        2. %=, **=, //=
"""
# =, +=, -=, *=, /=
# x += y  # equals to x = x + y
x **= 10
print(x)  # 3^10 =59049, x = 59049
# print("x%d **= 10:" % (x), x)
