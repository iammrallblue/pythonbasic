"""
    Sequence Tuple:
        Tuples are used to store multiple items in a single variable.
        format:
            my_tuple = ("A" ,"B", "C")
            slice of my_tuple
                my_type[start:end:step]
        key point:
            1. Tuple is 4 built-in data type, others List,Set,and Dictionary, all different
            2. Tuple is a collection which is ORDERED and UNCHANGEABLE.
            3. Tuples are written with round brackets.
                ("A" ,"B", "C")
            4. A tuple can store many different data type, include list.
            5. since tuple is unchangeable, can add,del, and reorder.
                ONLY query, search...
            6. the comma which is after every element in the tuple can determine
                whether a tuple is a tuple or not, (see code)
            7. range() can be converted to a tuple
        common functions/methods:
            1. count()
            2. index()

"""
# define an empty tuple
my_tuple = ()  # ()
print(type(my_tuple))  # <class 'tuple'>
print(id(my_tuple))  # memory hashcode: 4529127488

# define a tuple
my_tuple = ("Hello", "World", 1, 2.34, [11, 22, 33])
print(my_tuple)
print(id(my_tuple))  # memory hashcode: 4412836736

# query, and search a tuple
# iterating a tuple
for ele in my_tuple:
    print(ele, end=", ")  # Hello World 1 2.34 [11, 22, 33]
    pass
print()

# print out element by index of slice
print(my_tuple[0])  # Hello

print(my_tuple[2:4])  # (2,4] (1, 2.34)

# print out element reversely
print(my_tuple[::-1])  # ([11, 22, 33], 2.34, 1, 'World', 'Hello')
print(my_tuple[::-2])  # ([11, 22, 33], 1, 'Hello')
print(my_tuple[-2:-1:])  # (2.34,) ** the comma, is important to insure my_tuple is a tuple type.

#
# my_tuple[0] = 1  # TypeError: 'tuple' object does not support item assignment
# print(my_tuple[0])
print(len(my_tuple))  # 5

# edit the list "my_tuple[4]" in side the tuple, the list is editable.
print(type(my_tuple[4]))  # <class 'list'>
# modify the element of the fourth element of the tuple
my_tuple[4][0] = 666
print(my_tuple[4])
print(my_tuple)

# important comma for a tuple
my_tuple2 = (1)  # my_tuple2 will be treated as an int type.
print(type(my_tuple2))  # <class 'int'>

my_tuple2 = (1,)
print(type(my_tuple2))  # <class 'tuple>, because the comma tells that my_tuple2 is a tuple

# range()
my_tuple3 = tuple(range(10))  # convert a range() to tuple
print(my_tuple3)  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# count(x), to find out many same element in the tuple, x is the element in the tuple
print(my_tuple3.count(8)) # 1 , there has only one number 8
