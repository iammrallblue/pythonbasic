"""
    Function:
        A function is a block of code which only runs when it is called.
        You can pass data, known as parameters, into a function.
        A function can return data as a result.

        Syntax:
            def functionName(parameters):
                code block
                ...
                pass

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


# define a function()
def showinfo():
    """
    showinfo(), for printing out personal information
    :return:
    """
    print("--- Personal Information ---")
    print("Name: %s" % "Bella")
    print("Gender: %s" % "Female")
    print("Age: %d" % 23)
    print("Height: %f" % 5.5)
    print("Weight:%d" % 95)
    pass


# call a function
showinfo()


# define a function with argument
# what is your favorite vehicle
def vehicle(brand, color, origin, year):
    print("Brand: %s, Color: %s" % (brand, color))
    print("Origin: %s, Year: %d" % (origin, year))
    pass


# call function vehicle
vehicle("BMW", "Red", "Germany", 1900)


# formal parameter, x,y are formal parameters,
def summation(x, y):
    result = x + y
    print(result)
    pass


# a function can assign to a variable
def my_func():
    value = 1 + 2
    return value
    pass


total = my_func()
print("total of the function:", total)

# call function sum(), actual parameter,
summation(1, 2)  # 1, 2 are called actual parameter,


# formal parameters with default values
def subtraction(m=10, n=3):
    result = (m - n)
    print(result)
    pass


# call function w/o actual parameters
subtraction()

# also can call function with new actual parameters to replace the default values
subtraction(20, 100)  # -80


# Arbitrary Argument *args
def sum_numbers(*args):
    """
    sum up all numbers from parameter
    :param args:
    :return:
    """
    total = 0
    for i in args:
        total += i
        pass
    print("total is: ", total)
    pass


def greet(*names):
    """
    this function greets all names in the name tuple
    :param names:
    :return:
    """
    # *names is a tuple with arguments
    for name in names:
        print("Hello", name)
        pass


# call function greet(), pass a tuple into.
greet("Abby", "Bella", "Cathy", "Danielle", "Eva")

# call sum_numbers() function
sum_numbers(1)
sum_numbers(1, 2, 3)
sum_numbers()


# keyword arguments
# the actual parameter must be key=value pairs
def key_parameter(**kwargs):
    print(kwargs)
    pass


# call the function with keyword parameter
key_parameter()  # empty {} , no actual argument

# call the function with default values
key_parameter(name="Bella", age=23)

# error, actual argument must in the form of key=value
# key_parameter(1, 2, 3)

# call the function with a dict parameter
dict_a = {"Name": "Abby", "age": 20}
key_parameter(**dict_a)


# complex function
def complex_function(*args, **kwargs):
    print(args)
    print(*kwargs)
    pass


# call the complex function
complex_function()

complex_function(1, 2, 3, 4, 5, name="Cathy")
complex_function(age=18)


# a function have multiple return values
def my_function():
    sum_value = 1 + 2
    stu_name = "Bella"
    stu_age = 17
    return sum_value, stu_name, stu_age


return_values = my_function()
print(return_values)
print(type(return_values))  # <class 'tuple'>, (3, 'Bella', 17)


# a function can have return values like list, dict, and tuple
def my_function2():
    expr_number = 1 + 2
    stu_name = "Bella"
    stu_age = 17
    return expr_number, stu_name, stu_age, 90, [100, ], {"A": 100}, (1, 2, 3)


# if only need to show first three elements in the list
number, name, age, *list_a = my_function2()
print(number, name, age)  # 3, Bella, 17
print(list_a)  # print out the list [90, [100], {'A': 100}, (1, 2, 3)]
print(*list_a)  # print out all values in the list. 90 [100] {'A': 100} (1, 2, 3)
