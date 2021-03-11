"""
    Class Attribute and Instance Attribute:
        An instance attribute is a Python variable belonging to one, and only one, object.
        This variable is only accessible in the scope of this object and it is defined
        inside the constructor function, __init__(self,..) of the class.

        Key point:
            1. Instance Attribute can ONLY access by the object of class.
            2. Class' object can't modify the value of the class attributes (class variable)
                in the Instance, bella.name = "Abby", this isn't changed the value of Class Attribute
                the value "Abby" is ONLY assigned to the object's attribute name, which is "inherited"
                from its Class "Student"

        A class attribute is a Python variable that belongs to a class rather than a particular object.
        It is shared between all the objects of this class and it is defined
        outside the constructor function, __init__(self,...), of the class.

        Key point:
            1. Class Attributes can access by both Class' name and Class' object
            2. in the Student instance, the object of Class Student did not have
                the attribute name, the object will loop up to its Class, which is
                Class Student.

"""


class Student:
    """
     a Student Class

    """
    # Class Attributes
    name = "Bella"

    def __init__(self, age):
        """
        Initial Constructor
        :param age:
        """
        self.age = age  # Instance Attribute


bella = Student(20)
print("{} {}".format(bella.name, bella.age))

# access class attributes by class name
print(Student.name)
# print(Student.age)  # ERROR AttributeError: type object 'Student' has no attribute 'age'

bella.name = "Abby"
print(bella.name)  # the object's attribute is changed "Abby"
(print(Student.name))  # this is still "Bella"
