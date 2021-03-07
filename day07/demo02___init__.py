"""
    object.__init__(self[, ...])¶
        __int__ method
            it is for defining instance attributes.

"""


class People:
    # attributes
    # no instance attributes at here
    def __init__(self):
        """
            defining instance attributes here
        """
        self.name = "Abby"
        self.age = 17
        self.gender = "Female"

    def eating(self):
        """
        eating method, instance method
        :return:
        """
        print("fruit lover")
        pass

    pass


# instantiate an object of People class.
# define some instance attributes for the object person
person = People()
person.name = "Abby"
person.age = 17
person.gender = "Female"
print(person.name, person.age, person.gender)
person.eating()

# instantiate an object of People class.
person2 = People()
person2.name = "Bella"
person2.age = 18
person2.gender = "Female"
print(person2.name, person2.age, person2.gender)
person.eating()
