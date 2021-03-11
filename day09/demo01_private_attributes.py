"""
    Private Attributes (Variables):
        python doesn’t have anything called private member variable in Python.
        However, adding two underlines(__) at the beginning makes a variable
        or a method private is the convention used by most python code.
        Syntax:
            __attribute = value
        Private Instance Attributes
            Key point:
                1. declare a private attribute/variable by adding "__" in front of
                    the private attribute, it can't directly use outside of the class
                    but inside of the class.
                2. however, the private attributes can indirectly access by the methods which defined
                    in the same class
                3. the private attribute can't be inherited by any derived classes.
                4.
                2. When using the private attributes (variables):
                    1. to hide the specific attribute, which means not allowed the accessing
                        from outside of the class
                    2. to keep value unchangeable.
                    3. to keep it inside of the class, prevent derived class inheriting

        Private Class Attributes
            Key point:


"""


class MainClass:
    """
        Class MainClass
    """
    # private class attributes
    __private_var = 2020

    # instance methods
    def __private_method(self):
        print("I am the private method inside of the MainClass")
        pass

    def inside_class(self):
        print("Private Variable:", MainClass.__private_var)
        self.__private_method()
        pass


foo = MainClass()
foo.inside_class()


class Person:
    """
        Class Person
    """
    # Private Class Attributes
    __hobby = "Singing."

    # initial constructor
    def __init__(self):
        """
            initial constructor
        """
        self.__name = "Bella"  # set name in private
        self.age = 30
        pass

    # __str__()
    def __str__(self):
        """
            return an object as a string
            access private attribute in
            this instance method
        :return:
        """
        return "{} is {} years old, hobby: {}".format(self.__name, self.age, Person.__hobby)


# create object of Class Person()
bella = Person()

# call variable by the object's name.
# print(bella.name)
# when variable name is private, code will post AttributeError
# AttributeError: 'Person' object has no attribute 'name'

# call instance method to show private attributes outside of the class
print(bella.__str__())


# create a derived class Student inherited from Class Person
class Student(Person):
    """
        A Derived Class Student
    """

    # instance method
    def print_info(self):
        print(self.age)
    pass


# object of derived class can't access the private attribute in the base class (Person)
student = Student()
# print(student.__name)
# AttributeError: 'Student' object has no attribute '__name'
student.print_info()
print(student)


# class attribute can access by Class Name, and Object of the Class
# print(Person.hobby)
# print(Student.hobby)
# print(student.hobby)

# access the private class attributes
# print(Person.__hobby)
# print(student.__hobby)
# print(Student.__hobby)
# AttributeError: type object 'Person' has no attribute '__hobby'
