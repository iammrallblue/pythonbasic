"""
    Multiple Inheritance:
        in the instance:
            Hulk and Banner are the base classes of SmartHulk class
            SmartHulk is inherited from class Hulk and Banner both.
        Syntax:
            class Hulk:
            class Banner:
            class SmartHulk(Hulk,Banner):
        Key point:
            1. order of calling same name instance methods in multiple base classes
                a) can use magic method __mro__() to show the calling sequence
                    (<class '__main__.SmartHulk'>, <class '__main__.Hulk'>, <class '__main__.Banner'>, <class 'object'>)
                    the result shows that object first called method in Class SmartHulk, then Class Hulk, then
                    Class Banner, then the root class Object.
                    in the instance, object will stop calling while assess Class Hulk's instance method loveBlackWidow()
                    because, it found out the method and it stopped calling.
            2. __mro__() magic function,
                to show the order of calling instance methods from base classes.

"""


class Hulk:

    def smashing(self):
        print("Hulk like smash")
        pass

    def loveBlackWidow(self):
        """

        """
        print("Hulk loves black widow")
        pass


class Banner:

    def smart(self):
        print("Banner is a Dr.")
        pass

    def loveBlackWidow(self):
        print("Dr.Banner loves black widow")
        pass


class SmartHulk(Hulk, Banner):  # multiple inheritance

    def green(self):
        print("Banner Hulk, is Green.")
        pass


hulk = SmartHulk()
hulk.green()
hulk.smart()
hulk.smashing()
hulk.loveBlackWidow()  # call the loveBlackWidow in base class Hulk

# order of calling same name instance method
print(SmartHulk.__mro__)
# (<class '__main__.SmartHulk'>, <class '__main__.Hulk'>, <class '__main__.Banner'>, <class 'object'>)


