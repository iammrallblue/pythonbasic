"""
   Text type: str
        Strings in Python are identified as a contiguous set of characters
        represented in the quotation marks.
            name = "Bella" (recommended)
            or
            name = 'Bella' (confused when 'I'm or Bella's' will cause error
        String Concatenation:
            first_name = "Bella"
            last_name = "Wang"
            full_name = first_name + last_name
        String Formatting Operator %:
            Formats the string according to the specified format.
            format:
                name = "Bella"
                print("Name: %s" % name)
              common use:
                %s - String (or any object with a string representation, like numbers)
                %d - Integers
                %f - Floating point numbers
            Key point:
                1. % also can use in list
                    list = [1,2,3]
                    print("a list is: %s" %list)
"""

# Text type: string
name = "Bella,Wang"
print(name)  # Bella,Wang
print(type(name))
# <class 'str'>

# strings are array, can get letters from a string
# print(name[0])  # result is B.
letter = name[0]
print(letter)

# string concatenate
first_name = "Bella"
last_name = "Wang"
# full_name = first_name + ", " + last_name
# print(full_name)
print("My first name is %s, last name is %s" % (first_name, last_name))

# print full_name 3 times
print(last_name[0] * 3)

# %s in lists, %s can use in lists
list_a = [1, 2, 43, 4, 5]  # list[int]
print(type(list_a))  # <class 'list'>
print("A new list: %s" % list_a)

# instance of String formatting operator %
# print out information in a string format
name = "Abby"
cell_phone = 6787018436
ssn = 46100898
address = "110 Chase Med Ln Georgia"
zip_code = 30032

# show information by % string formatting operator
print("----- Personal Information by % ------")
print("Name: %s" % name)
print("Cell#: %d" % cell_phone)
print("SSN: %d" % ssn)
print("Address: %s %d" % (address, zip_code))

# show information by {} placeholder
print("----- Personal Information by {} ------")
print("Name: {} \nCell#: {}".format(name, cell_phone))
print("SSN#: {}".format(ssn))
print("Address: {} {}".format(address, zip_code))
