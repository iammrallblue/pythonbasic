# coding:utf-8
# 3/31/21 7:46 PM

"""
    Function:
                3x - 5  (x > 1)
        f(x) =  x + 2   (-1 <= x <= 1)
                5x + 3  (x < -1)

    two solutions:
        1. if ... elif ... else
        2. if ... else ... nested if... else...
"""

x = float(input("x = "))
if x > 1:
    y = 3 * x - 5
    pass
elif x >= -1:
    y = x + 2
    pass
else:
    y = 5 * x + 3
    pass
print("f(%.1f = %.1f)" % (x, y))

x = float(input("x = "))
if x > 1:
    y = 3 * x - 5
    pass
else:
    if x >= -1:
        y = x + 2
        pass
    else:
        y = 5 * x + 2
        pass
print("f(%.1f = %.1f)" % (x, y))
