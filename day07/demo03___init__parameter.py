"""
    parameter of __init__ method:
        __init__ method
            the built-in method, called magic method
            the method for the initialization of an object.
                1. define the instance attributes.
                2. data initialization
                2.


"""


class Animal:
    """
    Attributes
    """
    """
        instance methods
    """

    def __init__(self, name, breed, age):
        """
        declaration of instance attributes
        :param name:
        :param breed:
        :param age:
        """
        self.name = name
        self.breed = breed
        self.age = age
        pass

    def eating(self, food):
        """
        instance method eating()
        :return:
        """
        print(self.name + "food lover " + food)


husky = Animal("Husky", "Husky", "3")
print(husky.name, husky.breed, husky.age)
husky.eating("bones")

gr = Animal("GR", "Golden Retriever ", "2")
print(gr.name, gr.breed, gr.age)
gr.eating("Fruit")
