"""
    Modifying Private Attributes:
        Key point:
            1. define an instance method to change the value of attribute
            2. using getter() and setter() to change the value of attribute
"""


class Person:
    """
        Class Person
    """

    # private class attribute
    __hobby = "Singing"
    __nationality = "USA"

    # initial constructor
    def __init__(self):
        self.__name = "Bella"
        self.age = 18
        pass

    # return the object as a string
    def __str__(self):
        return "{} is {} years old, hobby: {}, nationality: {}".format(self.__name, self.age, Person.__hobby,
                                                                       Person.__nationality)
        pass

    def attr_change(self, temp):
        """
        change the value of private attributes
        :param temp:
        :return:
        """
        Person.__hobby = temp
        pass

    # get and set
    def get_naionality(self):
        return Person.__nationality
        pass

    def set_nationality(self, tmp_nationality):
        Person.__nationality = tmp_nationality
        pass


# a base class Student
class Student(Person):
    """
    A derived class Student
    """

    # instance method
    def show_info(self):
        # print(self.__hobby) # error Derived class can't inherit private attribute from the base class
        print(self.age)  # inherited from the base class
        pass


# an object of Class Student
bella = Student()

# change the value of private attribute __hobby
# Person.attr_change("Dancing")
bella.set_nationality("Korea")
bella.attr_change("Dancing")  # the private variable __hobby is changed
print(bella)  # call __str__() which is in the base class
print(bella.get_naionality())
