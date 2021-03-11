"""
         3. Static Method
            The static methods, in general, utility methods.
            Inside these methods we won’t use any instance or class variables.
            No arguments like cls or self are required at the time of declaration.

            We can declare static method explicitly by using @staticmethod decorator.
            We can access static methods by using class name or object reference

        Instance Code:
            class Demo:
                @staticmethod
                def sum(x, y):
                    print(x+y)
                @staticmethod
                def multiply(x, y):
                    print(x*y)
            Demo.sum(2, 3)
            Demo.multiply(2,4)
        Key point:
            1. usually use Class name to call a static method
            2. usually don't use the object of the class to call a static method
                b/c complex
            3. why using a static method
                    which is bound to the class and not the object of the class.
                    can’t access or modify class state,such as attributes and normal methods
                    It is present in a class because it makes sense for the method to be present in class.
                    inside of a static method, doesn't involve any operation of methods and attributes
"""


class People:
    """
    a Class People
    """
    # Class Attributes
    country = "China"

    # a static method
    @staticmethod
    def get_data():
        return People.country
        pass


print(People.country)

import time


# return current system time
class CurrentTime:
    """
        Current Time Class
    """

    # Class Attributes
    # initial constructor
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        pass

    pass

    # a static method
    @staticmethod
    def show_time():
        return time.strftime("%H:%M:%S", time.localtime())
        pass

    pass


# call show_time()
print(CurrentTime.show_time())

# NOT RECOMMENDED, b/c show_time() is a static method
# time_current = CurrentTime(1, 10, 20)
# print(time_current.show_time())
