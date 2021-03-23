"""
    1. accumulating function receives n numbers, to calculate n numbers
        return the amount of n number
        1. the number of argument is unknown, using *args
        2. using for loop to iterate numbers in *args
        3. *args is a tuple, because args accepts tuple data type.
                my_tuple = ()
        4. return the amount to caller
    2. defining a function that can find all odd number from a list, or tuple
        and return all odd number as a new list.
        1. a new list or tuple to store all odd number
        2. if statement to determine all odd number, add numbers to new odd list
            by function append()
        3. return the new list to caller
    3. defining a function that checking the length of each value in the dict.
        1. if the length of values is greater than 2, keep first two of each value.
"""


# instance 1
def accumulating_function(*args):
    """
    calculate amount of all number in the tuple (*args)
    return amount to caller
    :param args:
    :return:
    """
    # calculate the amount of n numbers
    amount = 0
    for x in args:
        amount += x  # add numbers,then assign to variable total
        pass
    return amount


# call accumulating_function()
total = accumulating_function(1, 2, 3, 4, 5)
print("Amount is {}".format(total))  # 15

total_2 = accumulating_function(10, 20, 30, 40, 50)
print("Amount is %d" % total_2)  # 150

total_3 = accumulating_function(-1, -2, -3, -4, -5, -6)
print("Amount is ", total_3)  # -21


# instance 2, find odd number from the list or tuple
def find_odds(numbers):
    """
    Find all odd numbers from a received list or tuple
    return the new odd list to caller
    :param numbers:
    :return:
    """
    odd_list = []
    for x in numbers:  # iterate numbers list or tuple
        if x % 2 == 1:
            odd_list.append(x)  # if x is odd, add to the new list.
            pass
        pass
    return odd_list
    pass


# call odd_number()
result = find_odds([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(type(result))  # <class 'list'>
# check numbers in the result list
print(result)  # [1, 3, 5, 7, 9]

# find_odds() with range()
# the original tuple converted from range()
original_tuple = tuple(range(10, 31))
print("original tuple: ", original_tuple)
result_2 = find_odds(tuple(range(10, 31)))
# print(type(result_2))  # <class 'list'> before convert range() to tuple
print(type(result_2))
print("the odds from the original tuple: ", result_2)


# instance 3
def iterating_dict(temp_dict):  # parameters can be **kwargs
    """
    check all key and value pairs in the dict
    :param temp_dict: 
    :return: 
    """
    # define a new empty dict for storing key and value pair
    new_dict = {}
    # iterate the temp_dict
    for key, value in temp_dict.items():
        if len(value) > 2:
            new_dict[key] = value[:2]  # (0,2], adding to the new dict by
            pass
        else:
            new_dict[key] = value
            pass
        pass
    return new_dict
    pass


# call iterating_dict()
obj_dict = {"Name": "Abby", "Gender": "Female", "Hobby": ["Singing", "Hiking", "Bakery", "Reading"], "Age": "18"}
print(iterating_dict(obj_dict))
