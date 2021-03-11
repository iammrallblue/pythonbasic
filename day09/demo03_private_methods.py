"""
    Private Method:
        Key point:
            1. can't call outside of the class, usually calling inside of the class
            2. can calling inside of the other method in the same class
            3. the base class can't inherit private method and attributes.

    "_" variable or method adding _ before the name, means it's protected type.
    the protected class can't import, but can inherit by its derived classes

    "__xxx__" means magic method, usually built in methods

    "str_" means to void having the same name with reserved words
"""


# Base Class
class Animal:
    """
    An Animal Class
    """

    # private instance method
    def __eat(self):
        print("eating")
        pass

    def run(self):
        self.__eat()  # call private method inside of the other method
        print("running")
        pass


# Derived Class
class Bird(Animal):
    """
    A Derived Class Bird
    """
    pass


bird = Bird()
# print(bird.eat())
# AttributeError: 'Bird' object has no attribute 'eat'
print((bird.run()))
