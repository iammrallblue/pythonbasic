"""
    1. create a class, instantiate an object of the class

    2. define an instance method inside of the class.
    3. create a fruit class,
        attributes: color
       call constructor __init__(self, color) to initialize instance attribute
"""


class Student:
    """
        Student class
    """

    # attributes

    def homework(self):
        """
        doing homework method
        (instance method)
        :return:
        """
        print("doing homework everyday")
        pass

    pass


# instantiate an object of Student class
abby = Student()

# call instance method homework()
abby.homework()


class FruitClass:
    """
    FruitClass,
    """

    def __init__(self, name, color):
        """
                constructor: __init__() method
        color assignment.
        :param color:
        """
        self.name = name
        self.color = color
        pass

    def __str__(self):
        """
        __str__method, return object as a string
        :return:
        """
        return "Fruit: %s is %s" % (self.name, self.color)

    pass


apple = FruitClass("Apple", "Green")
print(apple)


class Person:

    # instance method
    def weight(self):
        print("memory location of self: ", id(self))
        pass

    pass


bella = Person()
bella.weight()
print("memory location of bella: %s" % id(bella))


class Animal:

    def __init__(self, color, name, age):
        """

        :param color:
        :param name:
        :param age:
        """
        self.color = color
        self.name = name
        self.age = age
        pass

    def __str__(self):
        return "%s is %s, %d years old" % (self.name, self.color, self.age)

    def eat(self):
        print("%s is eating." % self.name)
        pass

    def run(self):
        print("%s is running." % self.name)
        pass


cat = Animal("white", "mimi", 3)
cat.run()
cat.eat()
print(cat)
