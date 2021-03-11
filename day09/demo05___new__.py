"""
    object.__new__(cls[, ...])
        Called to create a new instance of class cls. __new__() is a static method
        (special-cased so you need not declare it as such) that
        takes the class of which an instance was requested as its first argument.
    Key point:
        1. __new__() is executed before the __init__() function.
        2. whenever the object is created, the __new__() function will be default called.


"""


class Animal:
    """
        An Animal Class
    """

    def __init__(self):
        self.color = "Red"
        pass

    # this is the default  __new__() function, if it did not present.
    # def __new__(cls, *args, **kwargs):
    #     return super().__new__(cls, *args, **kwargs)
    # pass


# the object of the Class Animal
tiger = Animal()

# when the new object is created, it default call the __new__() function to create the object
