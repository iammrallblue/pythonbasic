"""
    Dynamic Attributes:
        are terminologies for attributes that are defined at runtime,
        after creating the objects or instances
        Key point:
            1. Instance attributes ONLY works with the instance where it is declared
            2. the dynamic attribute adds to the Class Level, which is the Class Attribute

        Q:
            If the instance zoey wants to access the attribute weight,
            we need to declare weight attribute in the Class Level,
            which is declared in the Class Student

    Dynamic Methods/Functions:

        Key point:
            1. when using the dynamic methods, types module needs to import
            2. define the method  or function which will be applied as the dynamic method
"""

import types


def dyn_method(self):
    try:
        print("Name: {}".format(self.name), "Age: %d" % self.age, "Weight:", self.weight, "lb")
        pass
    except Exception as msg:
        print(msg)
        pass

    pass


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def __str__(self):
        return "{} is {} years old".format(self.name, self.age)

    pass


# to add an attribute weight in Class Level
Student.weight = 106

bella = Student("Bella", 18)
# bella.weight = 100# attribute weight ONLY belongs to the instance bella

# binding the dynamic method
bella.print_info = types.MethodType(dyn_method, bella)
print(bella, bella.weight)

zoey = Student("Zoey", 19)
print(zoey.weight)  # error, AttributeError: 'Student' object has no attribute 'weight'

# call the Dynamic Methods
dyn_method(zoey)
