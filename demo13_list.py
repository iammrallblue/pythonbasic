"""
    Lists
        Lists are mutable sequences, typically used to store collections of homogeneous items
         (where the precise degree of similarity will vary by application).
        class list([iterable])
        format:
            list = ["a", 1, 1.1, "hello", True]
                list can store many different data types in a list
                index of a slice starts from ZERO 0
        key point:
            1. slice [start,end,step], to get sublist from a list.
            2. usually goes with for loop statement
            3. quickly create a list by range() function,
            4. modify elements in a list, list[0] = "modified_content"
                a) data type does not limit: for example
                    the original element is boolean type,
                    modified type can be any types.
            5. determine the length of a list by len()
        common functions/methods:
            1. append()
                add an element to the tail of sequence list
            2. count()
            3. extend()
                merge two or more lists together.
            4. index(ele,start,end)
                determine the index of an element in the list
            5. insert(i,x)
                insert an element x into the specified index i.
            6. pop(i), i is the index of the element
                delete an element based on the input index.
            7. remove(x), x is the element in the list,
                delete an element in the specified index
            8. reverse()
            9. sort()
            10. del
                delete elements from a list

        *** in Python 2, range() is a sequence list for generating numbers
            in Python(2.x). The range() function is used to generate a sequence of numbers.
        ***
"""
# define an empty list
list_a = []  # empty list.
print(type(list_a))  # <class 'list'>

# define a list
list_a = [1.23, 1, "Bella", True, False]  # elements can be different types.
# find the length of list by len()
print(len(list_a))  # 5
print(list_a)  # [1.23, 1, 'Bella', True, False]

# get a slice of the list
print(list_a[1:3])  # [1, 'Bella'], (1,3]
print(list_a[2:])  # ['Bella', True, False]

# print out in a reverse order.
print(list_a[::-1])  # [False, True, 'Bella', 1, 1.23]

# print out more than one time
print(list_a * 3)  # multiple times print out list

# add elements to sequence list, append() and insert()
# function append()
list_a.append(["wife", "wifi"])  # add to the end of the list
list_a.append(123)
print("after append()", list_a)  # nested list

# function insert(i,x), i is the index, x is the element
list_a.insert(1, "adding by insert()")
print("after insert()", list_a)

# generating 10 number by range() function, and convert into a list
range_number = list(range(10))  # (0,10] does not include 10
# check data typ
print(type(range_number))  # <class 'list'>
# merging two lists by function extend(), list_a and range_number
list_a.extend(range_number)  # add to the end of list
print("after extend()", list_a)

# directly add a new list to another
list_a.extend([666, 2333, 999])  # add to the end of list
print(list_a)

# modify element in a list, modify data type can be different.
list_a = [1, "Bella", True]
print("Before modified: ", list_a)
list_a[2] = "Good day"  # index starts from 0
print("After modified: ", list_a)

# delete elements in a list
list_b = list(range(10, 31))  # generated a list from range()
print(list_b)
del list_b[0]  # delete first element of the list
print(list_b)

# delete a slice of the list [x:y]
del list_b[2:8]  # (2,8]
print("delete a slice from [2:8], ", list_b)

# delete elements from a list by function remove(x), x is the element in the list
list_b.remove(30)  # 30 is the element in the list
print("delete number 30 from the list: ", list_b)

# delete elements from a list by function pop(i), i is the index of a element
list_b.pop(4)  # 4 is the index of the element.
print("delete element from the list by pop(): ", list_b)

# determine element(s) index by function index(x), x is the element in the list
ind = list_b.index(28)
print("the index is: ", ind)  # 10

# determine element index within a slice (element,start, end)
ind_2 = list_b.index(22, 1, 10)
print("the index is: ", ind_2)

