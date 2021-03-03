"""

"""
x = 1


def my_func(y):
    print("memory address of {} is {}".format("y", id(y)))  # y 4329867568
    y = 2
    print("memory address after changed the value of y", id(y))  # after changed 4558776656
    pass


# call my_func()
print("memory address of %s is %d" % ("x", int(id(x))))  # x 4329867568
my_func(x)

# list
list_a = []


def memory_value(parameters):
    print(id(parameters))  # 4427145472
    pass


print(id(list_a))
memory_value(list_a)  # 4427145472
