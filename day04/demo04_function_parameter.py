# coding:utf-8
# 3/29/21 11:09 AM

"""
    Parameter of Function:
        Parameter and Argument:
            From a function's perspective:
            A parameter is the variable listed inside the parentheses in the function definition. aka (formal parameter)
            An argument is the value that is sent to the function when it is called. aka (Actual parameter)

            Arguments, aka actual parameter
                Key point:
                    1. Required Argument
                        Required arguments are the arguments passed to a function in correct positional order.
                        def myfunction(x):
                            x = 1
                            print(x)
                        in the above code, 1 is the required argument, which is actual parameter.
                    2. Default Argument
                         A default argument is an argument that assumes a default value
                         if a value is not provided in the function call for that argument
                    3. Arbitrary Arguments, *args
                        when the argument is unknown, add * before the parameter name
                        This way the function will receive a tuple of arguments,
                        and can access the items accordingly
                        *** *args is always a tuple.
                            tuple:
                                my_tuple=(1,2,3,"A","B","C")
                    *** Arbitrary Arguments are often shortened to *args in Python documentations.
                    4. Keyword Arguments **kwargs
                        You can also send arguments with the key = value syntax.
                        This way the order of the arguments does not matter.
                            dict:
                                my_dict={"key"=value,"key"="value}
                    5. *args and **kwargs can be parameters together.
                        but *args MUST be the first parameter.

                        keyword arguments can be empty or as many as requited.
                Parameters, aka formal parameter
                    key point:
                        1. def sum(x,y), x, y are formal parameters,
                            they are not assigned memory allocation while defining.
                        2. when call a parameterized function
                            sum(1,2), 1,2 are actual parameter, they are assigned memory allocation.
                        3. a parameterized function MUST assign actual parameter when it is called.
                            unless the parameters have default values.
                        4. a function can return many values, they will return in the tuple form.
                Argument, aka actual parameter
"""


# # argument of function
# def my_func(x, y, z=10):
#     print(x)
#     print(y)
#     print(z)
#     pass
#
#
# my_func(1, 2, 3)


# # *arg, arbitrary argument
# def foo(x, y, *args):
#     print(x)  # 1
#     print(y)  # 3
#     print(args)  # a tuple, (4, 5, 6, 'Bella', [1, 2, 4, 5])
#     print(*args)  # elements of the tuple, 4 5 6 Bella [1, 2, 4, 5]
#
#
# # call function foo()
# foo(1, 3, 4, 5, 6, "Bella", [1, 2, 4, 5])


# *kwargs, keyword argument
def func(x, y, **kwargs):
    print(kwargs)  # return values in a dict form.
    # {'name': 'Bella', 'age': 17}


func(1, 3, name="Bella", age=17)


def my_function(name, age, *args, **kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    print(*args)
    print(**kwargs)
    pass


# call function my_function()
my_function("Bella", 17, )
