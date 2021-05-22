# coding:utf-8
# 3/18/21 7:59 AM

"""
    the FALSE value in Python:
        1. False    boolean
        2. None   null
        3. 0   int
        4. 0.0  float
        5. "", or '' empty str
        6. [], empty list
        7. (), empty tuple
        8. {}, empty dict
        9. set(), empty collection
"""

is_value = '0'
print(is_value)  # 0
print(type(is_value))
if is_value:
    print("Yes")
else:
    print("No")

