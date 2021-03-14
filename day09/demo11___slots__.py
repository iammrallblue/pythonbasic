"""
    __slots__, magic function

    Key point:
        1. __slots__ is to restrict the instance's attributes,
        2. all instance's attributes is stored in a dict by __dict__ function
        3.__slots__() magic function, and __dict__ cannot use at the same time,
            the __dict__ will post error
                AttributeError: 'Student' object has no attribute '__dict__'
        4. __slots__() magic function,provide a special mechanism to reduce the size of objects.
            It is a concept of memory optimisation on objects. save memory space.
        5. the derived classes will not inherit the __slots__ from the base class,
            the derived class can define attributes without restriction, when there is no __slots__() magic function
             inside of the derived class' body.
                the instance zoey can define attributes without restriction
        6. when the derived class declared the __slots__() magic function, it will also inherit
            the __slots__() from the base class.
        7. in the base class slots has ("name","age","address"), don't need to declare in the
            derived class' slots again,
"""


class Student(object):
    # using __slots__ magic
    __slots__ = ("name", "age", "address")

    def __str__(self):
        return "Name:{}, Age:{}, Address: {}".format(self.name, self.age, self.address)


pass

bella = Student()
bella.name = "Bella"
bella.age = 19
# bella.gender = "Female"  # AttributeError: 'Student' object has no attribute 'gender'
bella.address = "GA"

# to show all attributes by __dict__() function
# print(bella.__dict__)  # {'name': 'Bella', 'age': 19, 'address': 'GA'}
print(bella)


# the Derived Class of Class Student
class SubStudent(Student):
    __slots__ = ("gender", "major")
    pass


zoey = SubStudent()
zoey.gender = "Female"
zoey.major = "CS"
zoey.name = "Zoey"
print(zoey.name, zoey.gender, zoey.major)
