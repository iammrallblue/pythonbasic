"""
    Override methods from Base Class:
        When Derived class and Base class have same name methods.
            in the Derived class, the instance method is overridden.
        Key point:
            1. When a method in a subclass has the same name, same parameters or
                signature and same return type(or sub-type) as a method in its super-class,
                then the method in the subclass is said to override the method in the super-class.
            2. why overriding:
                because in some situations, the method in base class won't satisfied the derived class
                therefore, the derived class needs to override it.
            3. In the instance Class Dog and Class Husky
                object of derived class will call __init__() method in base class, when its __init__()
                did not declared.
                    in instance husky.bark() show error shows
                        TypeError: __init__() missing 2 required positional arguments: 'name' and 'color'
                     because object of derived class called the base class' __init__()
                    Solution:
                        to override the __init__() of base class in derived class
            3. Derived class' __init__() needs to call Base class' __init__(), b/c if using instance attributes from
                base class in derived class itself.
"""


# the base class Parent
class Parent:
    # attributes

    # initial constructor
    def __init__(self):
        self.text = "I am from Base Class"
        pass

    def show_method(self):
        print(self.text)
        pass


# the derived class Child
class Child:
    # attributes

    # initial constructor
    def __init__(self):
        self.text = "I am from Derived Class"
        pass

    def show_method(self):  # overrode
        print(self.text)
        pass


# Driver's code

dad = Parent()
son = Child()

dad.show_method()
son.show_method()  # result shows the show_method() is overridden.


# the Base Class Dog
class Dog:
    # attributes

    # initial constructor
    def __init__(self, name, color):
        self.name = name
        self.color = color
        pass

    def bark(self):
        print("dog is barking...")
        pass


# the Derived Class Husky
class Husky(Dog):
    # attributes

    # overrode the base class' __init__()
    def __init__(self, name, color):  # overrode
        # call base class' __init__() for using its attributes
        super().__init__(name, color),  # to call base class
        # Dog.__init__(self, name, color)
        # extending other attributes of derived class
        self.height = 90
        self.weight = 20
        pass

    def __str__(self):
        return "{} is {}, {}, height {}, weight {},".format(self.name, self.color, self.height, self.weight)

    # instance method, (overrode)
    def bark(self):
        # call base class' instance method
        super().bark()
        print("Husky is barking...")
        pass


husky = Husky("Husky", "Brown")
husky.bark()
# object husky called its instance method bark,
