"""
    Sequence types: list, tuple, range
        list: (same as array)
            names = []  # <class 'list>
            names = ["Abby", "Bella", "Cathy", "Danielle", "Eva"]
          Key point:
            1. "Abby" each of them is called an element.
            common methods:
                a. insert(i,x), insert an element to array
                    i is index (position)
                    x is value which will be inserted.
                    names.insert(0,"John Doe")
                b. append(x), adding an element to the end of array
                    x is value which will be inserted.
                    names.append("John Doe")
                c. delete an element from list or the entire list
                    the del statement:
                     remove an element from list
                    del names[0]
                d. modify an element from list
                    names[0] = "John Doe"
                e. search an element in list, return boolean value
                     1. "John Doe" in names (names is the list)
                     2. search to determine element's index by index()
                         names(x,[,start[,end]]), return zero-based index
                     statement nested: search an element then remove it.
                        del names[names.index("John Doe")]


"""

# Sequence types: list
names = []  # empty list, no element stored.
print(names)
# print empty []

print(type(names))
# result <class 'list'>

names = ["Abby", "Bella", "Cathy", "Danielle", "Eva"]  # assign elements to list names
print(names)  # ["Abby", "Bella", "Cathy", "Danielle", "Eva"]
# print out all elements in the names list

# print out a specific element
print(names[0])  # Abby
# result is Abby

# insert an elements to names list by insert()
names.insert(5, "Anna")  # add the element "Anna" to index 5
print(names)  # ['Abby', 'Bella', 'Cathy', 'Danielle', 'Eva', 'Anna']

# add an elements to the end of names list by append()
names.append("Zoey")
print(names)  # ['Abby', 'Bella', 'Cathy', 'Danielle', 'Eva', 'Anna', 'Zoey']

# remove an element from list by del statement
del names[5]
print(names)  # deleted element "Anna"

# modify an element from list
print(names[0])  # Abby
names[0] = "Anna"  # "Abby" replaced by new element "Anna"
print(names)  # ['Anna', 'Bella', 'Cathy', 'Danielle', 'Eva', 'Zoey']

# search element in a list by " "" in list "
"Anna" in names  # search in list
print("Anna" in names)  # return a boolean True

# determine index of an element by function index()
ele_index = names.index("Zoey")
print(ele_index)  # index 5

"""
why need to know index?
easy to remove an element when the index is determined.
"""
del names[5]
print(names)

# combine both del and index() statement
# search the element first, then del to remove the search-element
del names[names.index("Anna")]
print(names)  # ['Bella', 'Cathy', 'Danielle', 'Eva']
