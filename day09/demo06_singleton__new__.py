"""
    Singleton：
        This pattern restricts the instantiation of a class to one object.
        It is a type of creational pattern and involves only one class to create methods and specified objects.

        Key point:
            1. for Singleton object or instance, Usually based on the built in function
                __new__().
            2. in the instance, cls._instance = cls.__new__(cls)
                if cls, which is the current class called its __new__(), it will cause a dead loop
                    solution:
                        For avoiding the dead loop, to call the __new__() from the root class "object"
            3. hasattr(object, string) function, the arguments are the object and a string,
                    The result is True if the string is the name of one of the object’s attributes,
                    False if not.

        Instance code:
            to show the created objects are the same by
                1. the root class __new__()
                2. hasattr(object, string) function
                3. if statement to determine whether the instance/object is existed, or not.
"""


class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance == None:
            Singleton()
            return Singleton.__instance
        pass

    # initial constructor
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is Singleton.")
        else:
            Singleton.__instance = self
            pass
        pass


inst = Singleton()

inst = Singleton.get_instance()
print(inst)

inst = Singleton.get_instance()
print(inst)


# class DatabaseClass inherited Class object
class DatabaseClass(object):
    """
    A Class DatabaseClass
    """

    # __new__() override
    def __new__(cls, *args, **kwargs):
        # cls._instance = cls.__new__(cls) # a dead loop,
        # because the class used itself __new__()
        # solution: call the __new__() function from the root class object
        if not hasattr(cls, "_instance"):  # if is not same instance then creating a new instance
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
        pass

    pass


# derived class
class DerivedDatabase(DatabaseClass):
    pass


# an object of DatabaseClass
obj_db = DatabaseClass()
print(id(obj_db))

obj_db2 = DatabaseClass()
print(id(obj_db2))

obj_db3 = DatabaseClass()
print(id(obj_db3))

der_db = DerivedDatabase()
print(id(der_db))

der_db2 = DerivedDatabase()
print(id(der_db2))

der_db3 = DerivedDatabase()
print(id(der_db3))
