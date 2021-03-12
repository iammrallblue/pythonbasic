"""
    Exceptions:
        1. try...except...:
                The try block lets you test a block of code for errors.
                The except block lets you handle the error.
                The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""


class TryExcept:
    try:
        print(x)
    except NameError:
        print("variable is undefined.")
        pass
    else:
        print("nothing is wrong")

    try:
        1 / 0
    except ZeroDivisionError:
        print("O can't be divided")
        pass
    else:
        print("0 is superman")
    finally:
        print("the try except is terminated.")