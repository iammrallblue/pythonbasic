"""Built-in Function:
    The Python interpreter has a number of functions and types built into it that are always available.
        id()
        print()
        input()
        len()
        range()
        arithmetical operation function:
            abs()
                get absolute value
            round()
                get rounded and nearest integer after the decimal point
            pow()
                get base to the power x^y
            divmod()
                get quotient and remainder when using integer division
            max()
                get max value from a few numbers
            min()
                get min value from a few numbers
            sum()
                get sum of a few numbers
            eval()
                The arguments are a string and optional globals and locals.
                If provided, globals must be a dictionary.
                If provided, locals can be any mapping object.
                the arguments are also called expression arguments.

    reference: https://docs.python.org/3.9/library/functions.html
    """
# abs()
print(abs(-0.2))  # 0.2

# round()
print(round(3.37))  # 3

# round() to keep one decimal place.
print(round(3.38, 1))  # 3.4

#
print(type(round(300.00000004, 2)))
value = round(300.123454444, 2)
print(value)
# pow()
print(pow(3, 3))  # 27
# same as
print(3 ** 3)  # 27

# divmod()
print(divmod(10, 2))  # (5, 0) 5 is quotient, 0 is remainder

# max()
print(max([1, 20, 333, 999, 666, 1.1]))

# min()
print(min([1, 20, 333, 999, 666, 1.1, 0.1]))  # 0.1

# sum()
print(sum([1, 2, 3, 4, 5, 6, 7, 8]))  # 36
print(sum(range(0, 51)))  # 1275

# eval()
x, y, z = 1, 2, 4
print(eval("x + y + z-90"))  # "x + y + z -98" one expression


# eval() function
def test_func():
    print("you see me when running in eval() function")
    pass


# call test_func()
eval("test_func()")  # eval("can execute another function as an expression")

# eval() function with dict
print(eval("x+y+z", {"y": 3, "z": 5, "x": 5}))
