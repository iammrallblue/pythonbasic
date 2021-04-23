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
    if... statement in short term
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


# short term if statement
if 5 > 2:
    print("Yes")
else:
    print("No")


print("yes") if 5 > 2 else print("no")

# while statement with else statement
x = 1
while x < 6:
    print(x)
    x += 1 # condition must be presented
    pass
else:
    print("x is no longer less than 6")