"""
    nested function:
        A nested function is simply a function within another function,
        and is sometimes called an "inner function".



"""


# nested function
def nested_func():
    print("this is in the first function.")
    print("the end of the first function")
    pass


def call_func():
    print("this is in the second function.")
    # call nested_func()
    nested_func()
    print("the end of the second function.")
    pass


# call function call_func()
