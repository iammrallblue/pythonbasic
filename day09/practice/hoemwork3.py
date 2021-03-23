"""
    1. create a Student Class,
    2. declare __init__() with two private attributes (name, and age)
    3. declare __call__(), it makes the instance/object performed as a function
    4. use @property to get and set private attributes' values
    5. use an instance/object as a function
        Syntax:
            obj_name()
"""


class Student:
    def __init__(self):
        self.__name = "Bella"
        self.__score = 90
        pass

    def __str__(self):
        return ""

    def __call__(self, *args, **kwargs):
        print("Name:", self.__name, "Score:", self.__score)
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        pass

    @property
    def score(self):
        return self.__score

    pass

    @score.setter
    def score(self, score):
        self.__score = score
        pass


# instantiate an object of Student Class
stu = Student()

# using instance/object as a function, "call function"
stu()  # stu() will call the __call__() function

stu.name = "Abby"
stu.score = 100
stu()  # name and score  changed.
