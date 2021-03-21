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


      Logic operators
        and
            return True if both statements are True
        or
            return True if one of statements is True
        not
            reverse the result, returns False if the result is True
      Identity operators:
        is
            return True if both variables are the same object
        is not
            return True if both variables are NOT the same object
      Membership operators:
        in
            returns True if a sequence with the specified value is present in the object (x in y)
        not in
            returns True if a sequence with the specified value is NOT present in the object ( x not in y)
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

#
mod_div = y / x
print("y/x:", mod_div)  # 0.2
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
# x += y  # equals to x = x + y == x++
x **= 10
print(x)  # 3^10 =59049, x = 59049
# print("x%d **= 10:" % (x), x)


# logic operators: (and, or, not)
x = 5
# print(x > 1 and x < 10)
print(1 < x < 10)  # True, both are True

y = "hello"
print(y and 1 == 2)
print(y or 1 == 2)

print(x > 1 or x < 1)  # True, one of both is True

print(not (x > 1 or x < 0))  # False, because reverse the True result

# identity operators: (is, is not)
print(x is y)  # False, different objects
print(x is not y)  # True

# membership Operators (in, not in)
print("h" in y)  # True
print("h" not in y)  # False
print("h,l" in y)  # False
