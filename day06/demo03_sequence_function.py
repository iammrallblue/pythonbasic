"""
    Sequence type:
        str, list, tuple, range,

    Sequence function:
        all()
            Return True if all elements of the iterable are true (or if the iterable is empty).
            it's False when 0, None, and False, otherwise.
            all() will have boolean values, True or False.
            key point:
                all() is similar with logic AND, if there is a False ,the whole statement will be False
        any()
            Return True if any element of the iterable is true. If the iterable is empty, return False
            Key point:
                any() is similar with logic OR, if there is True, the whole statement will be True.
        sorted()
            Return a new sorted list from the items in iterable.
            specify ascending or descending order.
            Strings are sorted alphabetically,
            and numbers are sorted numerically.
            diff b/w sorted() and sort:
                1. sorted() can iterate the specified iterable object (list,str,tuple, dict....)

                2. sort() directly changed the list itself.
                    list.sort(), is one of methods with list.
                    tuple is immutable, it can be changed,
        reverse()
        range()
        zip()
        enumerate()

"""
# all(), similar with logic and
print(all([]))  # an empty list, True
print(all(()))  # an empty tuple, True
print(all([1, 2, False]))  # False, b/c it has value False
print(all([1, 2, 3]))  # True
print(all([1, 3, 0]))  # False
print(all([1, 2, None]))  # False

# any(), similar with logic or
print(any((3, 0, 0)))  # True
print(any(("", None, 0, False)))  # False

# sorted() and list.sort()
list_a = [2, 45, 1, 67, 23, 10]
print("the original list:", list_a)
# list_a.sort()  # directly changed the original object of list_a

# sorted() function
sorted_list = sorted(list_a)
print("after using sorted()", sorted_list)  # [1, 2, 10, 23, 45, 67]
sorted_list2 = sorted(list_a, reverse=True)
print("after using sorted(), and reversed list:", sorted_list2)

my_tuple = (2, 45, 1, 67, 23, 10)
print(my_tuple)
sorted_tuple = sorted(my_tuple, reverse=False)
print(sorted_tuple)

# range()

# zip()
list_b = [1, 2, 3, 4]
print(list_b)
list_c = ["Abby", "Bella", "Cathy", "Danielle"]
print(list_c)

print(list(zip(list_b)))  # [(1,), (2,), (3,), (4,)]

print(list(zip(list_b, list_c)))  # [(1, 'Abby'), (2, 'Bella'), (3, 'Cathy'), (4, 'Danielle')]

# list_a has more than 4 elements, but will ONLY use 4 elements, see result
print(list(zip(list_a, list_b, list_c)))


# [(2, 1, 'Abby'), (45, 2, 'Bella'), (1, 3, 'Cathy'), (67, 4, 'Danielle')]


# instance of zip() function
def book_item():
    """
    book information management
    zip() funciton usage
    :return:
    """
    book_list = []  # empty list for storing info of books.
    book_id = input("input book's id: (input space if searching many books")
    book_name = input("input book's name: ")
    book_position = input("input book's location: ")

    # split each of book_info
    id_list = book_id.split(" ")
    name_list = book_name.split(" ")
    position_list = book_position.split(" ")

    book_collection = zip(id_list, name_list, position_list)  #
    for book in book_collection:
        """
            iterating info of books then storing
        """
        dict_info = {"ID": book[0], "Book Name": book[1], "Location": book[2]}
        book_list.append(dict_info)
        pass
    for item in book_list:
        print(item)


# call function book_item()
book_item()