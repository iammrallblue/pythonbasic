"""Recursion Function:
    function recursion in python, which means a defined function can call itself.(condition 1)
    Recursion is a common mathematical and programming concept.
    This has the benefit of meaning that you can loop through data to reach a result.
    Key point:
        1. should be very careful with recursion as it can be quite easy
            to slip into writing a function which never terminates,
            or one that uses excess amounts of memory or processor power.
        2. However, when written correctly recursion can be a very efficient
            and mathematically-elegant approach to programming.
        3. all recursion can be achieved by loop statement,
        4. condition 2, it must have a "exit", in the instance, the exit is if n == 1,
            the code will terminate when condition n == 1,
    Pros and Cons:
        Pros:
            1. Simple Logic
            2. Simple Definition
        Cons:
            1. a lot of ram usage. stack overflow.
    factorial instance:
        1. Find a factorial of a number.
        2. simulate tree structure (files searching)
"""


# factorial instance, find the factorial of numbers by for loop
def calc_factorial(n):
    product = 1
    for number in range(1, n + 1):  # (1,n+1]
        product *= number
        pass
    return product


# call calc_factorial
print(calc_factorial(5))


# factorial instance, find the factorial of numbers by recursion funciton
def recur_factorial(n):
    """
        Find a factorial of a number by recursion
    :param n: parameter of factorial
    :return:
    """
    if n == 1:
        return 1
    else:
        return n * recur_factorial(n - 1)
    pass


# call recursive function
print(recur_factorial(10))

import os  # import write or read of file function.


# tree structure instance
def find_file(file_path):
    list_dir = os.listdir(file_path)  # collect all files and folders under the path
    for files in list_dir:
        full_path = os.path.join(file_path, files)  # get the full path fo files and folder
        if os.path.isdir(full_path):  # determine the path whether folder or file
            find_file(full_path)  # if it is folder, recursion(function called itself)
        else:
            print(files)
            pass
        pass
    else:
        return
    pass


# call find_file()
find_file("/Users/junoh/Downloads")
# result will print out all files list, except folder
