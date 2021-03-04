"""
    Python Variable Assignment and Memory Location
        Key point:
            1.variable x, y are unchangeable data types, number,string,tuple
            2. changeable data types, list, dict, set
                in python everything is an object.
                when calling the function, the actual parameter (argument) passed the object reference
                formal parameter.
"""
# unchangeable data type
x = 1


def my_func(y):
    print("memory location of {} is {}".format("y", id(y)))  # y 4329867568
    y = 2
    print("memory location after changed the value of y",
          id(y))  # after changed 4558776656
    pass


# call my_func()
print("memory location  of %s is %d" % ("x", int(id(x))))  # x 4329867568
# passing variable x to parameter y basically just passed the memory location
my_func(x)

# changeable data type, list
list_a = []


def test_reference(prm):
    list_a.append([1, 2, 3, 4, 5])
    print("the memory location of parameter prm is: ", id(prm))  # 4427145472
    pass


print("ths memory location of list list_a is: ", id(list_a))
test_reference(list_a)  # passed list_a's memory location to parameter prm.

print("list_a outside of the function: ", id(list_a))
