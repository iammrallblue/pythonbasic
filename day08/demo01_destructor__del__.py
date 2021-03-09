"""
    Destructor:
        Destructors are called when an object gets destroyed.
        Key point:
            1. In Python, destructors are not needed as much needed in C++ because
                Python has a garbage collector that handles memory management automatically
            2. A reference to objects is also deleted when the object
                goes out of reference or when the program ends.
            3. When a program goes end, it will call the destructor at the end.
            4. destructor is always declared inside of classes.
            5.  __del__() will call by interpreter automatically, when it does not reference to scope.
            6. when object is delete by developer, __del__() will execute as well.
                syntax:
                    del object
            7. after __del__() executed. attributes, functions, objects, are gone.
        Syntax of destructor declaration :
            def __del__(self):
                # body of destructor

        Instance:
            def __del__(self):
                print(__del__() is a destructor)

"""


class Animal:
    def __init__(self, name):
        """
            this is the initial constructor
        :param name:
        """
        self.name = name
        print("__init__ is initialized instance attributes as parameter")
        pass

    def __del__(self):
        print("__del__() is called at the ending of the program.")
        print("the object %s is destroyed to free the memory space" % self.name)
        pass


cat = Animal("kitty")
# for the result , __init__() is executed before __del__()

dog = Animal("husky")
# __del__() will automatically execute after every object is finished using.

# manual delete object.
del dog

#
input("waiting to exit program...")
