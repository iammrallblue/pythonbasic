"""

  Global Variables:
      Variables that are created outside of a function are known as global variables.
      Global variables can be used by everyone, both inside of functions and outside.
"""
# global variable
x = "Bella"


def myFunction():
    print("name is: " + x)
    # using variable x inside of function
    pass


myFunction()


# using variable x outside of function
print(x)


# declare global variable inside of a function
def myFunc():
    # global y = 333 # error
    global y
    y = 333
    print("y = ", y)

# call myFunc()
myFunc()

print("outside of function: ", y)
