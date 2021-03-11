"""
    Three types of methods in a Class
         1. Instance Method
                Instance methods are methods which act upon the instance variables of the class.
                They are bound with instances or objects, that”s why called as instance methods.
                 The first parameter for instance methods should be "self variable" which refers to instance (object).
                 Along with the "self variable" it can contain other variables as well.

            Instance Code:
                class Demo:
                    def __init__(self, a):
                        self.a=a
                    def m(self):
                        print(self.a)

                # create object and call methods
                d=Demo(10)
                d.m()
            Key point:
                1. Instance method MUST have self as the first parameter,
                2. using self to access all class attributes and instance attributes.
                    if class attributes and instance attributes have name conflicted.
                    the instance attributes have the highest priority
         2. Class Method
                Class methods are methods which act upon the class variables or static variables of the class.
                We can go for class methods when we are using only class variables (static variables) within the method.

            Instance Code:
                class Pizza:
                    # Class Attributes
                    radius=200

                    @classmethod
                    def get_radius(cls):
                        return cls.radius

                print(Pizza.get_radius()

            Key point:
                1. a static method does not need specific keyword, like cls, and self.
                1. Class Method has a header @classmethod
                2. the method name can be defined as instance method
                3. the method MUST have "cls" as the first parameter inside the (),
                # call Class Method

         3. Static Method
"""


class People:
    # Class Attribute
    country = "China"

    # define a class method
    @classmethod
    def get_country(cls):
        print("I am a class method")
        return cls.country  # access class attribute
        pass

    @classmethod
    def change_country(cls, data):
        cls.country = data
        pass

    pass


# call class method by class name
print(People.get_country())

# call class method by the object of the class
person = People()
print("Access Class Method by the Object of The Class: %s" % person.get_country())

# changing class attribute country by class name
People.change_country("Japan")  # change the value of Class Attribute

print(People.get_country())
