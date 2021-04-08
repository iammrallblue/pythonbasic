# coding:utf-8
# 4/3/21 12:06 PM

"""
    Conversion of Metric and Imperial Units
"""

value = float(input("input the length: "))
unit = input("input the unit: ")
if unit == "inch" or unit == "in":
    print("%.2f(inch) = %.2f(cm)" % (value, value * 2.54))
    pass
elif unit == "cm" or unit == "centimeter":
    print("%.2f(cm) = %.2f(inch)" % (value, value / 2.54))
    pass
else:
    print("input valid values.")
