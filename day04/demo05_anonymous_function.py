# coding:utf-8
# 3/29/21 1:51 PM

"""
    Anonymous Function: (lambda expression)
        Syntax:


"""


# A standard function
def anon_function(arg):
    return arg


name = anon_function("Bella")
print(name)

# An anonymous function (lambda expression)
lam_value = lambda arg, arg2: arg + arg2

result = lam_value(1, 3)
print(result)
