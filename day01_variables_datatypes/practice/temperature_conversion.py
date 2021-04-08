# coding:utf-8
# 3/31/21 11:21 AM

"""
    Temperature Conversion:
        1. Convert from Fahrenheit to Celsius
"""
temp_f = float(input("temperature F to C: "))
temp_c = (temp_f - 32) / 1.8
# print("Temperature Conversion: %fF = %fC" % (temp_f, temp_c))

# %.1f, shows short term of values
print("Temperature Conversion: %.1fF = %.1fC" % (temp_f, temp_c))
