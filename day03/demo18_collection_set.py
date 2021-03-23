# coding:utf-8
# 3/23/21 11:25 AM

"""
    class set:
        set()

        Common Functions/Methods
            add()
                Adds an element to the set
            clear()
                Removes all the elements from the set
            remove("element")
                Removes the specified element
            pop()
                Removes an element from the set
            update()
                Update the set with the union of this set and others
            difference()
                Returns a set that contains the difference between two sets.
            intersection()
                Returns a set that contains the similarity between two or more sets.
            union()
                Returns a set that contains all items from the original set, and all items from the specified set(s).
        Key point:
            1. the element can not duplicate, which means the element will be unique.
            2. A set is unordered. print out different result everytime.
            3. A list can convert to set
            4. A dict can convert to set, but ONLY keep keys
"""

my_set = set()
print(type(my_set))  # <class 'set'>
print(my_set)  # set()

my_set = {1, "hello", "bella", "oh", 1, 2}
print(my_set)  # {1, 2, 'bella', 'oh', 'hello'} unique elements

my_list = ["disk", "cpu", "memory", "graphic card"]
# list to set
print(set(my_list))  # {'disk', 'memory', 'graphic card', 'cpu'}

my_dict = {"A": "1", "B": "2", "C": "3", "D": "4"}
# dict to set
print(set(my_dict))  # {'C', 'B', 'D', 'A'}

# Common Functions/ Methods
my_set = {1, "hello", "bella", "oh", 1, 2, "a", "A", "C"}
my_set.add("Billy")
print(my_set)
my_set.remove("C")
print(my_set)

pop_elem = my_set.pop()
print(pop_elem)

# difference() method, find different element in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = y.difference(x)
print("difference of sets x and y:", z)  # return a new set
# print(y - x)  # return the result as difference() method

# intersection() method, find same element in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print("intersection of sets x and y:", z)
# print(x & y)  # return the result as intersection() method

# union() method, find all elements in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print("union of sets x and y:", z)
# print(x | y)  # return the result as union() method

# ^, to skip the duplicated elements, keep unique elements
print("^: ", x ^ y)
