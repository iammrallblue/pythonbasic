"""
    Property() function:
        the main purpose of Property() function is to create property of a class.
    Syntax:
        property(fget, fset, fdel, doc)
        Parameters:
            fget() – used to get the value of attribute
            fset() – used to set the value of attribute
            fdel() – used to delete the attribute value
            doc() – string that contains the documentation (docstring) for the attribute
            Return: Returns a property attribute from the given getter, setter and deleter.

    Key point:
        1. changing value of private attribute by the property() function.
        2. the property decorator, @property this means set the method as a getter method
            a) when the object bella.age is called. it will calling the decorator # property
                to get the value of age
            b) when bella.age is assigned a new value, it will calling the @age.setter to set
                a new value for private attribute age.

"""


class Person(object):
    """
    A Person Class
    """

    # instance method
    def __init__(self):
        self.__age = 18  # a private variable
        pass

    """
        method 2, by property()
    """

    @property  # get the value of the private attribute
    def age(self):
        return self.__age
        pass

    @age.setter  # set the value to the private attribute
    def age(self, parms):
        if parms < 0:
            print("invalid input.")
            pass
        else:
            self.__age = parms
            pass
        pass


"""
    # method 1, changing private variable by set() and get() 
    
    def get_age(self):
        return self.__age
        pass

    def set_age(self, age):
        if age < 0:
            print("invalid input.")
            pass
        else:
            self.__age = age
            pass
        pass

    # a property function for accessing the private variable
    age = property(get_age, set_age)
"""

# an object of the Class Person
bella = Person()

# changing private variable by set() and get()
# bella.set_age(18)
# print(bella.get_age())  # 18

print(bella.age)  # 18

bella.age = 17
print(bella.age)  # 17
