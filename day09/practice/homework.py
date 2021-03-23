"""
    Instance:
        1. define a Person Class, with __init__() function,
        2. __init__() has two private attributes, name and age
        3. a method for collecting user input information.
        4. a method for getting private attributes
        5. getter and setter methods for modify values of private attributes
        6. a method to limit the age range b/w (0 ~ 120), failed setting if out of age range
"""


class Person:
    """
    A Person Class
    """

    # initial constructor
    def __init__(self, name, age):
        """
        initial constructor
        :param name:
        :param age:
        """
        self.__name = name  # private variable
        self.__age = age  # private variable
        pass

    def __str__(self):
        """
        to print out all information
        :return:
        """
        return "Name:{}, Age:{}".format(self.__name, self.__age)

    # getter and setting
    def get_age(self):
        return self.__age
        pass

    def set_age(self, age):
        if 0 < age < 120:
            self.__age = age
            pass
        else:
            print("invalid input")
            pass

    def get_name(self):
        return self.__name
        pass

    def set_name(self, name):
        self.__name = name
        pass
