"""
    Lambda Expression aka Lambda Function (Anonymous Function):
        Small anonymous functions can be created with the lambda keyword.
            Syntax:
                lambda a, b: a+b
                This function returns the sum of its two arguments:
        Key point:
            1. using keyword lambda to define function, no function name.
            2. can have many arguments.
            3. the expression after colon is unique. it's not an argument
            4. lambda function has a default return.
            5. lambda function can ONLY have one expression after colon.
                the designation of lambda function is ONLY for a simple function requirement.
            5. lambda function is for simple logic, not for complex logic.
"""


# a standard function in python


def add_numbers(x, y):
    """
        adding number
    : param x:
    : param y:
    : return:
    """
    return x + y
    pass


print(add_numbers(1, 2))  # 3

# lambda function, convert a standard function into lambda function
# def L(x, y): return x+y (Not recommended)
L = lambda x, y: x + y

# call lambda function
print(L(3, 4))  # 7

result = lambda x, y, z: x * y * z
print(result(1, 2, 3))

# lambda function substitutes if else statement
age = 12
print("You are adult." if age > 18 else "You are just a kid.")

# by lambda function
lambda_func = lambda x, y: x if x > y else y
print(lambda_func(10, 9))
print(type(lambda_func)) # <class 'function'>

# by lambda function 2
lambda_func2 = (lambda x, y: x if x > y else y)(19, 15) # directly call lambda function
# 1. (lambda x, y: x if x > y else y) this is the object of an anonymous function
# 2. (19,15) call the anonymous function directly after the function
print(lambda_func2)
