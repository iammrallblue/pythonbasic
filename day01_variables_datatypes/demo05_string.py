"""
    String: 
      Strings in python are surrounded by either single quotation marks, or double quotation marks.
      'hello' is the same as "hello".


"""

my_str = "Hello Bella !  "
print(my_str[0])


# a String can be a long statement.
long_str = """You may have tried to debug your serverless functions by adding print statements, 
but I’m going to show you how it’s possible to run and debug local 
serverless functions written using AWS’s Chalice micro-framework."""


# Get the characters from index 2 to index 4 (llo).
print(my_str[2:5])

# remove all white space before or after text by function stipe()
my_str2 = " Hello, Hello !  "
print(my_str2.strip())  # "Hello, Hello !"

# Replace String
# The replace() method replaces a string with another string:
my_str3 = "Hello, World!"
print(my_str3.replace("e", "2"))
