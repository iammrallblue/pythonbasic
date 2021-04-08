# coding:utf-8
# 3/19/21 2:59 PM

"""
    Break and Continue Statements:

"""
for_break = ""
# nested for loop statement
for i in range(1, 5):
    for j in "abc":
        print(i, "==", j)
        if j == "b":
            for_break = True
            break  # j for loop will skip when j == "b"
        pass
    if for_break:
        break  # when j for loop is in break, i for loop will be in break
    print("...")
    pass
print("code is continue.")

# tuple instance
tuple_a = {}
tuple_a[(1, 2, 4)] = 8
tuple_a[(4, 2, 1)] = 10
tuple_a[(1, 2)] = 12
_sum = 0
for i in tuple_a:
    _sum += tuple_a[i]
    pass
print(len(tuple_a) + _sum)


# instance searching an element in database
