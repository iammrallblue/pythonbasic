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


# def L(x, y): return x+y 
L = lambda x, y: x+y


# call lambda function
print(L(3, 4))  # 7

result = lambda x,y,z: x*y*z
print(result(1,2,3))