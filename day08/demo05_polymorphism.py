"""
    Polymorphism in Python:
        The word polymorphism means having many forms.
         In programming, polymorphism means same function name
         (but different signatures) being uses for different types.

        Two Pre-conditions:
            1. Inheritance, Polymorphism MUST in b/w base class and derived class.
            2. Overriding, Derived class CAN override methods from Base Class


    Instance of Built in polymorphism functions len()

        Key point:
            1. polymorphism can increase the program's flexibility
            2. polymorphism can increase the programs' expandability
"""
# len() is a built in polymorphism
print(len("Bella"))

print(len([1, 2, 3]))


class Animal:
    """
    the Base Class Animal
    """

    def whoami(self):
        print("I am an animal")
        pass


# inherited from Base Class Animal
class Duck(Animal):
    """
    The Derived Class Duck
    """

    # override the base class' method whoami()
    def whoami(self):
        """
            the base class' instance method is overridden
        whoami()
        :return:
        """
        print("I am a duck")
        pass

    pass


# inherited from Base Class Animal
class Dog(Animal):
    """
    The Derived Class Duck
    """

    # override the base class' method whoami()
    def whoami(self):
        """
            the base class' instance method is overridden
        whoami()
        :return:
        """
        print("I am a dog")
        pass

    pass


# inherited from Base Class Animal
class Cat(Animal):
    """
    The Derived Class Cat
    """

    # override the base class' method whoami()
    def whoami(self):
        """
            the base class' instance method is overridden
            whoami()
        :return:
        """
        print("I am a Cat")
        pass

    pass


# inherited from Base Class Animal
class Bird(Animal):
    """
    The Derived Class Bird
    """

    # override the base class' method whoami()
    def whoami(self):
        """
            the base class' instance method is overridden
            whoami()
        :return:
        """
        print("I am a Bird")
        pass

    pass


# a temp method for integration of method calling
def temp_method(obj):
    """
        a method for all objects' calling
    :param obj:
    :return:
    """
    obj.whoami()
    pass


pass

duck = Duck()
duck.whoami()
# result shows that object called whoami() which is
# overrode in class Duck.


# Q: if many objects need to create, the code will be redundant
# solution: define a method with a list to make calling nest and brief

obj_list = [Duck(), Dog(), Cat(), Bird()]
for i in obj_list:
    """
        this for loop is for calling methods
    """
    temp_method(i)
    pass
pass
