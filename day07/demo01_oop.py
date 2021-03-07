"""
    OOP:
        Object-Oriented Programming (OOP) :
            An object has two characteristics: (a parrot is an object )
            attributes
                name, age, color, gender, as attributes
            behavior
                singing, dancing, as behavior
        Class:
            a blueprint of an object.
            1. ClassName
            2. attributes
                class attributes, which are belonged to Class
                key point:
                    1. attributes are variables inside of Class,
            3. behavior (method)
                instance method, which object can use them.
                key point:
                    1. instance method is defined inside of Class
                    2. using keyword def to define
                    3. the first default parameter is "self"
                    4. instance methods can access by any instance related to them.
                    5. the variable defined inside of methods are called instance attributes
                        using self.methodAttributes = value
            Syntax:
                class Parrot:
                pass
        Object:
            An object (instance) is an instantiation of a class.
            Syntax:
                obj = Parrot()
                    obj is an object of class Parrot.
            1. ObjectName
            2. attributes:
            3. behavior
"""


# create a class
class Person:
    """
    attributes:
        name, age
    """
    name = "Abby"
    age = 18

    """
        behaviors (method)
        singing()
    """

    def singing(self):
        print("a pro singer.")
        pass

    def dancing(self):
        mtd_variable = "pop"  # method attribute
        print("a pro dancer.")

    def __init__(self):
        self.name = "Bella"  # instance attribute
        pass


# declare an object

Abby = Person()
print("Name: {}, Age: {}".format(Abby.name, Abby.age))
Abby.singing()  # call function
Abby.dancing()
