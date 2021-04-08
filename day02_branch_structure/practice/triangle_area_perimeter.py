# coding:utf-8
# 4/5/21 8:57 AM

"""
    Determine three sides of triangle, then calculate the perimeter and area of
    triangle
"""

x = float(input("x ="))
y = float(input("y ="))
z = float(input("z ="))

if x + y > z and x + z > y and y + z > x:
    print("The perimeter of triangle is: %.2f" % (x + y + z))
    value = (x + y + z) / 2
    area = (value * (value - x) * (value - y) * (value - z)) ** 0.5
    print("Area of the triangle is: %.2f" % area)
    pass
else:
    print("Can't be any triangles.")
