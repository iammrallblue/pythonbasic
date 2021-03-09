"""
    Three Characteristics of OOP:
        1. Encapsulation
            a block statements encapsulated into a container, such function, method
            for calling in a convenient way.
            in python, encapsulation is the __init__() method encapsulated codes into
            objects, then using objects or calling through self keyword.
        2. Inheritance
            base class (superclass)
            derived class (subclass)
                Syntax:
                    class DerivedClass(BaseClass):
                        statements...
                        pass
            below code,
                Dog and Cat are the derived classes of Animal class
                Animal class is the base class.
        3. Polymorphism

"""


# base class
class Animal:
    """
    Animal class, is a base class
    attributes, functions, method
    can be inherited.
    """

    # attributes

    # instance method
    def eat(self):
        """

        :return:
        """
        print("eating....")
        pass

    def drink(self):
        """

        :return:
        """
        pass


# derived class
class Dog(Animal):

    # instance method
    def sound(self):
        print("barking...")
        pass


# derived class
class Cat(Animal):
    # instance method
    def sound(self):
        print("meow,meow...")

    pass


dog = Dog()
dog.sound()
dog.eat() # inherited from base class Animal


cat = Cat()
cat.sound()
cat.eat()
