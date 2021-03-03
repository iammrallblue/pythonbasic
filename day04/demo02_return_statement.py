"""
    return statement
        A return statement is used to end the execution of the function call 
        and “returns” the RESULT 
        (value of the expression following the return keyword) to the caller. 
        
        Key point:
            1. The statements after the return statements are not executed.
            2. If the return statement is without any expression, 
                then the special value NONE is returned.
            3. Return statement can not be used outside the function.
            4. It can return any data types, it depands on the expressions after return
            5. A function can have many returns, but ONLY one return can have value back to caller.
        Syntax:
            def my_func(parameter):
                statements
                ...
                return [expression]
"""


def add(x, y):
    result = x + y
    return result
    pass


# w/o return inside add() function, it will show no result
print(add(1, 2))

get_result = add(2, 3)
print(get_result)


# accumulation of numbers
def calc_numbers(num):
    result = 0
    x = 1
    while x <= num:
        result += x
        x += 1
        pass
    return result
    pass


# call calc_numbers
accu_total = calc_numbers(5)
print(type(accu_total))  # <class 'int'>
print(accu_total)
pass


# list for storing even numbers and return the list to caller
def calc_evens(num):
    even_list = []
    result = 0
    x = 1
    while x <= num:
        if x % 2 == 0:
            result += x
            pass
        x += 1  # for while loop
        pass
    even_list.append(result)
    return even_list


# call function calc_evens()
get_evens = calc_evens(10)
print(type(get_evens))  # <class 'list'>
print(get_evens)


# tuple for storing and return the tuple to caller
def tuple_return():
    """
    return a tuple type to caller
    :return:
    """
    # return 1, 2, 3  # this is a tuple
    my_tuple = (1, 2, 3)
    return my_tuple


# call tuple_return()
get_value = tuple_return()  # <class 'tuple'>
print(type(get_value))
print(get_value)  # (1,2,3)
