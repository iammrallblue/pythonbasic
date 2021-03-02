"""
    Built-in Data types:
        Text type: str
            (see demo05_text_type_string.py)
            x = "Bella"

        Numeric types:
            int:
                class_number = 1
                age = 10
                year = 100
            long: for large number,
              * Python3 abolished long type
              * in Python2 will still show <class 'long'> for a large number
                such as
                  large_number = 2**128

            float:
                retail_price = 1.1
                decimal_number = 0.1
                offer_price = 0.5

            complex,
                x = 3.14j

        Boolean type: True, False
            x = True, y = False
            x = 1
            y = 2
            x > y False
            y > 2 True

        Sequence types: list, tuple, range
            list:
                list_a = ["apple", "banana", "cherry", "dragon fruit", "Elderberries"]
                print(type(list_a))  # <class 'list'>
            (see demo05_sequence_type_list.py)
            tuple:
                list_b = ("apple", "banana", "cherry",)
                print(type(list_b))  # <class 'tuple'>

        Mapping type: dict
            dict:
                dict_a = {"name" : "John Doe", "age" : 35}
                print(type(dict_a))

        Set types: set, frozenset

        Binary types: bytes, bytearray, memoryview.
        Key point:
            1. using function type(),
                type(variable) to check data type
            2. print(), type() in Python are called functions.
"""

# Numeric types: int
x = 10
print(type(x))  # result <class 'int'>

# Numeric types: long
y = 2 ** 128
print(y)
# y is long type, result 340282366920938463463374607431768211456
print(type(y))  # result shows y is int type not long type

# boolean value
y = True
print(type(y))  # result <class 'bool'>

# boolean type
x = 1
y = 2
print(x > y)
# result is false


# list instance
list_a = ["apple", "banana", "cherry", "dragon fruit", "Elderberries"]
print(list_a)
print(type(list_a))  # <class 'list'>

# tuple instance
list_b = ("apple", "banana", "cherry",)
print(list_b)
print(type(list_b))  # <class 'tuple'>

# dict instance
dict_a = {"name": "John Doe", "age": 35}
print(dict_a)
print(type(dict_a))  # <class 'dict'>
