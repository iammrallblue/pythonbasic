# coding:utf-8
# 3/20/21 10:25 PM
"""
    built-in range() function:
        in Python 2.7.x, range() function is a list type <type 'list'>
        in Python 3.x.x, range() is redesigned, it's an object of class range <class 'range'>
"""

range(9)
print(type(range(9)))  # <class 'range'>

# in 2.7.x
print(type(range(9)))  # <type 'list'>

# # print numbers 0 - 10
# for i in range(10):  # [0,10)
#     print(i)
#     pass
# # result: 0 1 2 3 4 5 6 7 8 9 (not included 10)

# # print EVEN and ODD numbers
# for i in range(0,10, 2):
#     print(i)
#     pass
# # result: 0 2 4 6 8

for i in range(1, 10, 2):
    print(i)
    pass
# result: 1 3 5 7 9
