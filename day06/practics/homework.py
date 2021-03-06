"""
    A. calculate 3 sets of numbers' total, 1 ~ 10, 20 ~ 30, 35 ~ 45
        1. define a function for calculating sum
        2. return a sum function which can sum up all number in the range
        3. use range() as a parameter of sum() function

    B. 100 birds eat 100 slices of oreo, 1 big bird can eat 1 oreo, 3 small bird can eat 1 oreo
        Question, how many big birds? and how many small birds?
"""


# instance A
def sum_range(x, y):
    """
    calculate total of a set number,
    1 ~ 10, 20 ~ 30, 35 ~ 45
    :param x:
    :param y:
    :return:
    """
    return sum(range(x, y + 1))
    pass


# call sum_range() for number range 1 ~ 10
print("the total of 1 to 10 is %d" % sum_range(1, 10))

# call sum_range() for number range 10 ~ 20
print("the total of 10 to 20 is", sum_range(10, 20))

# call sum_range() for number range 35 ~ 45
print("the total of 35 to 45 is {}".format(sum_range(35, 45)))


# instance B
def count_birds():
    """

    :return:
    """
    for x in range(1, 100):
        if x * 3 + (100 - x) * (1 / 3) == 100:
            return x, 100 - x  # return a tuple (x, 100-x)
        pass
    pass


# call count_birds()
print(type(count_birds()))  # <class 'tuple'>
bird_tuple = count_birds()
print("{} big birds, and {} small birds ".format(bird_tuple[0], bird_tuple[1]))

# instance C
my_list = [1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 6, 7, 8, 8, 8, 8, 9, 9, 9]
my_set = set(my_list)  # keep all unique numbers, and return a new set
print(type(my_set))  # <class 'set'>
print("the original list: {}".format(my_list))
print("exclusive result: ", my_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9} all unique element in my_set

# the for loop is for determining all duplicated numbers.
for i in my_set:
    my_list.remove(i)  # my_list left all duplicated elements based on my_set
    pass
print("all duplicated numbers in my_list: ", my_list)  # [2, 3, 5, 6, 6, 8, 8, 8, 9, 9]

# in here, my_list =  [2, 3, 5, 6, 6, 8, 8, 8, 9, 9]
uni_numbers = set(my_list)  # keep all unique numbers, and return a new set
print(type(uni_numbers))  # <class 'set'>
print("unique numbers ", uni_numbers)  # a new unique set {2, 3, 5, 6, 8, 9}

# the for loop is for determine and print out the unique number in my_set
# my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
for i in my_set:
    if i not in uni_numbers:
        print(i)  # the unique number, 1,4,7
        pass
    pass
pass
