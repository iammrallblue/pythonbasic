"""
    keyword self
        it is the object itself, must in the first index of parameters
        works when define methods inside of class, which are instance methods
        interpreter will assign for self,
        self can be changed. any names

"""


class Person:
    """
        Person class
    """

    def __init__(self, career):
        self.career = career
        pass

    def eat(self, name, food):
        """
        instance method
        :return:
        """
        print("memory location of self = ", id(self))  # 4378787216
        print("%s love(s) eating %s" % (name, food))
        print("career: ", self.career)
        pass

    pass


# create an object of Person Class
superman = Person("Student")
print("memory location of object superman = ", id(superman))  # 4378787216
superman.eat("Bella", "Mango", )

# output object superman
print(type(superman))  # <class '__main__.Person'>
print(superman)  # <__main__.Person object at 0x1095c9c70>
