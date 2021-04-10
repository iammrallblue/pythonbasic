"""
    Exceptions:
        1. try...except...:
                The try block lets you test a block of code for errors.
                The except block lets you handle the error.
                The finally block lets you execute code, regardless of the result of the try- and except blocks.
            Key point:
                1. the errors which need to be caught are can be specified
                    like NameError, ZeroDivisionError ...
                2. If errors are not specified, the except can have Exception to throw a msg
                3. If Exception is applied, we don't need any others' excepts to catch error.
                    but you can expect as many as excepts you want to catch errors.
                4. The Exception is usually the last except in the code, if many excepts are present.
                5. The Exception does not to be the specified place, it can replace into a potential
                    place where might occur errors.
                6. The Exception makes catching errors more flexible, simple, and efficient
"""


class TryExcept:
    try:
        print(x)
    # except NameError as msg:
    #     # print("variable is undefined.")
    #     print(msg)  # name "x" is not defined
    #     pass
    except Exception as msg:
        print(msg)  # name "x" is not defined
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

        pass

    # catch list errors by try... except
    try:
        list_a = [1, 2, 4]
        print(list_a[10])
        pass
    # except NameError as msg:  # this except will be invalid, because the error is not a NameError
    #     print(msg)
    #     pass
    # except IndexError as msg:
    #     print(msg)  # list index out of range
    #     pass
    except Exception as result:
        print(result)  # list index out of range
        pass


print("If this executed, errors are caught.")


# Exception does not to be a precise position
def method_a(x):
    return 10 / int(x)
    pass


def method_b(y):
    return method_a(y) * 2
    pass


def main():
    try:
        method_b("0.0")
        pass
    except Exception as msg:
        print(msg)
        pass
    pass


# call main() method
main()
# division by zero, when method_b("0")
# invalid literal for int() with base 10: '0.0', when method_b("0.0")


# try-except-finally
try:
    int("fff")
    pass

except Exception as msg:
    print("error is: ", msg) # invalid literal for int() with base 10: 'fff'
    pass
finally:
    print("whether errors are caught or not, this finally will be executed.")
    pass
