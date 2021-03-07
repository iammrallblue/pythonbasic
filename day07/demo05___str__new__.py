"""
    object.__str__(self)
        Called by str(object) and the built-in functions format() and print() to compute the “informal” or
        nicely printable string representation of an object.
        The return value must be a string object.
    object.__new__(cls[, ...])
        Called to create a new instance of class cls.
        __new__() is a static method (special-cased so you need not declare it as such)
        that takes the class of which an instance was requested as its first argument.
         The remaining arguments are those passed to the object constructor expression (the call to the class).
         The return value of __new__() should be the new object instance (usually an instance of cls).
    Key point:
        1. when the program is executed. the __new__() method will always running in the first place
        2. the __init__() method will running after __new__() method.
        3. difference of the __new__() method and the __init__() method:
                1) __new__() is the method the class instantiation
                    creating object of classes in __new__() method.
                2) __init__() is the method for the attributes initialization
                    declaring instance attributes, it is similar with Java's constructors.
                3) __new__() has the parameter cls, cls represents the current class which will be instantiated
                    and the parameter cls is provided by the python interpreter
                4) __new__() method will be always executed before __init__() method, because ONLY the object is existed
                    then can execute the __init__() method of the object.
"""


class Person:
    """
    Person Class
    """

    def __init__(self, career, name, food):
        """
        instance attributes
        :param career:
        :param name:
        :param food:
        """
        self.career = career
        self.name = name
        self.food = food
        print("__init__ method is executed")
        pass

    # similar with Java overridden toString() method
    # __str__() magic method
    def __str__(self):
        """
        print out object information in string form
        :return:
        """
        return "Career: %s, %s love(s) eating %s " % (self.career, self.name, self.food)

    pass

    # __new__() magic method, cls means current class which is Person class.
    def __new__(cls, *args, **kwargs):
        """
        method of creating an object.
        :param args:
        :param kwargs:
        """
        print("__new__ method is executed")
        # __new__ method creates an object of Person class
        return object.__new__(cls) # created an object of the current class (Person)

    # the result will see __new__ method is executed first when the program is running.
    # print(cap_america), the result is None, because __new__ method haven't created any
    # object of the current class which is Person class.
    # when object.__new__(cls) is declared, it means __new__ method is created an object
    # of the current class (Person)

    def eat(self, name, food):
        """
        instance method
        """
        print("%s love(s) eating %s" % (name, food))
        print("career: ", self.career)
        pass


# create an object of Person
cap_america = Person("Hero", "Cap.America", "sushi")
# print(type(cap_america))
# print(cap_america)
# cap_america.eat("CapAmerica", "Pizza")
print(type(cap_america))  # <class '__main__.Person'>
# print(cap_america)  # None
# call object cap_america, after __new__ method declared the object of the current class (Person)
print(cap_america)  # Career: Hero, Cap.America love(s) eating sushi
