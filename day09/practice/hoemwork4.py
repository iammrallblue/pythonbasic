"""
    Dynamic types:

"""
import types


def run(self):
    print("cat is running.")
    pass


@classmethod
def info(cls):
    print("cat is an object of Animal Class")


class Animal:
    pass


cat = Animal()
cat.run = types.MethodType(run, cat)  # Dynamically binding
cat.run()

# binding a class attribute in the Class Level
Animal.color = "Black"

# binding a class method inf the Class Level
Animal.info = info

# using the binding class attribute in an instance.
print(cat.color)

# an instance called the class method
cat.info()

# Class name Animai called the class method
Animal.info()
