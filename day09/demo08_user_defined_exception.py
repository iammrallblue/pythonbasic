"""
    User-Defined Exception:
        A User-Defined Exception should typically be derived from the Exception or Error class,
        either directly or indirectly.
"""


# derived class inherited from Class Exception
class LengthControlException(Exception):
    """
    A User-Defined Exception Class
        to regulate the length of ...
    """

    def __int__(self, length):
        """
        Initial Constructor
        :param length:
        :return:
        """
        self.length = length
        pass

    def __str__(self):
        return "the length of your input is out of length range." + str(self.length)
        pass

    pass


def get_data():
    name = input("input your info:")
    if len(name) > 10:
        raise LengthControlException(len(name))
    else:
        print(name)


get_data()
