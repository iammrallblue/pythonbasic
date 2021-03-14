"""
    Binding Class Method

    Syntax:
        ClassName.class_method_name = class_method

"""


# class method
@classmethod
def class_method(cls):
    print("a class method")
    pass


@staticmethod
def static_method():
    print("a static method")
    pass


class Student:
    """
    A Student Class
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def __str__(self):
        return "Name:{}, Age:{}".format(self.name, self.age)

    pass


print("Binding a Class Method")
Student.test_method = class_method
# call the class method
Student.test_method()

print("class method test is finished.")

print("Binding a Static Method")
Student.sta_test_method = static_method
# call the static method
Student.sta_test_method()

print("a static method test is finished.")
