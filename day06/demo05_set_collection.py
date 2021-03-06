"""
    Set Types — set, frozenset¶
        A set object is an unordered collection of distinct hashable objects.
         Common uses include membership testing, removing duplicates from a sequence, 
         and computing mathematical operations such as intersection, union, difference, and symmetric differenc
        Syntax:
            my_set = {1,2,3,4}
            compares to 
            my_dict = {"a":1,"b":2}
        Key point:
            1. set does not support slice[], and index,
            2. set is an unordered collection and no duplicated elements.
            3. it is similar with dict, but ONLY has Key, no values.
        Common functions:
            add(elem)
                Add the element elem to the set
            clear()
                Remove all elements from the set
            difference(*others)
            set - other - ...
                Return a new set with elements in the set that are not in the others.
            intersection(*others)
            set & other & ...
                Return a new set with elements common to the set and all others.
            union(*others)
            set | other | ...
                Return a new set with elements from the set and all others.
            pop()
                Remove and return an arbitrary element from the set. Raises KeyError if the set is empty.
            discard(elem)
                Remove element elem from the set if it is present.
            update(*others)
            set |= other | ...
                Update the set, adding elements from all others.
            len(d)
                Return the number of items in the dictionary d.

"""
# set
my_set = {1, 2, 3, 4, 5}
my_set2 = {2, 3, 4, 5, 6, 7}
print(type(my_set))  # <class 'set'>
print(my_set)  # {1, 2, 3, 4, 5}

# dict
# my_dict = {"a": 1, "b": 2}

# add(elem) function
my_set.add("Python")  # add element to the end of the set
print(my_set)  # {1, 2, 3, 4, 5, 'Python'}

# clear(), delete all elements in the set
# my_set.clear()
# print(my_set)  # set()

# difference(*other), find different elements from two sets
diff_elem = my_set.difference(my_set2)
print(type(diff_elem))  # <class 'set'>
print(diff_elem)  # {'Python', 1}
# difference(*other), is equal to my_set - my_set2
print(my_set - my_set2)  # {'Python', 1}
print(my_set)

# intersection(*other), find same elements from two sets
same_elem = my_set.intersection(my_set2)
print(type(same_elem))  # <class 'set'>
print(same_elem)  # {2, 3, 4, 5}
# intersection(*other), is equal to  my_set & my_set2
print(my_set & my_set2)  # {2, 3, 4, 5}

# union(*other), print out all elements in either set.
union_sets = my_set.union(my_set2)
print(type(union_sets))  # <class 'set'>
print(union_sets)  # {1, 2, 3, 4, 5, 6, 7, 'Python'}
# union(*other), is equal to my_set | my_set2
print(my_set | my_set2)  # {1, 2, 3, 4, 5, 6, 7, 'Python'}

# pop() function, delete an element in the set
print(my_set)  # {1, 2, 3, 4, 5, 'Python'}
pop_elem = my_set.pop()  # arbitrary element
print(pop_elem)  # 1

print(my_set)  # {2, 3, 4, 5, 'Python'}

# discard(elem), remove a specific element
print(my_set.discard(3))  # None
print(my_set)  # {2, 4, 5, 'Python'}

my_set3 = {1, 2, 3, 4, 5}
my_set4 = {2, 3, 4, 5, 6, 7}
# update(*other), combine two sets, no duplicated elements
my_set3.update(my_set4)
print(my_set3)