"""
    Global variable:
        key point:
            1. global variable is for all functions, every function can use it
            2. when global variable and local variable have the same name,
                prefer to use local variable inside of the function
            3. inside functions, to change value of a global variable,using keyword "global"
                Syntax:
                    global name
                     name = "new value"

    Local variable:
        the variable is defined inside of function.
        ONLY can use inside of the function.
        key point:
            1. different functions can have same-name variable in each scope.
            2. local variable is for temporary storing data, defined in side the function

"""

# global variable
day_weather = "Sunny Day"
name = "Bella"


def my_func():
    name = "Abby"  # name is local variable
    print(name)
    print("{} {}".format(name, day_weather))
    pass


def my_func2():
    name_2 = "Andy Lau"
    # print(name)# NameError: name 'name' is not defined
    print(name_2, day_weather)
    pass


# call my_func()
my_func()

# call my_func2()
my_func2()


def change_global():
    """
    modify global variable
    :return:
    """
    # name = "Cathy"  # name is local variable, not change global variable

    # change value of global variable
    global name
    name = "Zoey"
    print(name)
    pass


change_global()
