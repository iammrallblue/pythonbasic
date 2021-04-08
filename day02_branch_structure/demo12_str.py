"""
    Text Sequence Type:
        class str: <class 'str'>
            Common methods/functions:
                1. capitalize()
                    Return a copy of the string with its first character capitalized and the rest lowercased.
                2. strip()
                    Return a copy (substring) of the string with the leading and trailing characters removed.
                3. lstrip() and rstrip()
                    eliminate empty space on the left and the right and return a copy of string w/o
                    empty spaces.
                4. id(object)
                    to show memory hashcode of the object.
                5. find()
                    to check if a string whether contained the specified character or not
                     and return the index of the specified character
                6. index()
                    both are similar for a string.
                    the diff of find(), and index(),if did not contain substring, find() returns -1
                    and index() returns an exception.
                7. startswith(), endswith()
                    return the boolean value True and False if prefix and suffix are contained
                    the specific character.
                        ONLY working with the str and tuple of str
                8. lower() and upper()
                    convert all letters to lower or upper.
                9. len()
                    print out the lenth of th string
                10. split()
                11. rsplit()
            instance:
                msg_str = "Hello Hiking"
                reversed_str = "gnikiH olleH"
                                123456789
                new_str = msg_str[::-2], step is -2, from the right to left
                        = gii le
"""
# define a string
string = "I'm a string."

# print out the first letter of string by using index of string
print("First letter is %s in the string." % string[0])
print("letter in the string. %s" % string[4])

# iterating a string by for loop
for letters in string:
    print(letters, end="  ")  # I  '  m     a     s  t  r  i  n  g  .
    pass

# function capitalize()
string = "beautiful"
print("\nCapitalize a string word %s to: %s" % (string, string.capitalize()))
pass

# function strip(), to get rid of empty space in a string
string = "    beautiful soul    "
no_space_string = string.strip()
print("The original string word: ", string)
print("After calling strip() function: ", no_space_string)
# function lstrip() , to get rid of empty space on the left side of string
string = "     hiking day     "
print(string.lstrip())  # eliminate empty space on the left
print(string.rstrip())  # eliminate empty space on the right
string = "Hello"
print(string.strip("H"))  # get rid of the letter "H", result ello

# copy string, is just assign the same memory address to the new string variable.
copy_string = string
# memory address of copy string
print("memory address of string: %d" % id(string))  # 4352609776
print("memory address of copy string: %d" % id(copy_string))  # 4352609776

# function find(), and index()
wordStr = "Bella is my wife"
print(wordStr.find("y"))  # index of y is 10
print(wordStr.find("Z"))  # return -1 did not contain.

# detect the string whether contains "w" or not, return index.
print(wordStr.index("w"))  # index of o is 12
# print(wordStr.index("0"))  # ValueError: substring not found

# function startswith(), and endswith()
wordStr_2 = "Today is hiking day."
print(wordStr_2.startswith("t"))  # False,
print(wordStr_2.endswith("."))  # True

# Typeerror
# int_str = "1234"
# print(int_str.startswith(1))  # TypeError: startswith first arg must be str or a tuple of str, not int

# function lower() and upper()
print(wordStr_2.lower())  # today is hiking day.
print(wordStr_2.upper())  # TODAY IS HIKING DAY.

# slice [start:end:step]
msg_str = "Hello Hiking"
print(msg_str)
print(msg_str[0])  # H
print(msg_str[2:5])  # (2,5] llo
print(msg_str[2:])  # llo Hiking
# [0:3] == [:3],
print(msg_str[0:3])  # Hel
print(msg_str[:3])  # Hel
# reverse iterating from right to left
print(msg_str[::-1])  # gnikiH olleH
# the length of the string msg_str
print(len(msg_str))  # length is 12

# reversely print a string by step -2
print(msg_str[::-2])  # gii le

# a string url address
str_url = "www.google.com/search"

new_str_url = str_url.split()
print(new_str_url)  # ['www.google.com/search'] a list

# split the string by  parameter "."
new_str = str_url.split(".")
print(new_str)  # ['www', 'google', 'com/search']

# split the string by the default "space"
str_a = "www google com /search \ndd    "
print(str_a.split())  # ['www', 'google', 'com', '/search', 'dd']
print(str_a.split(" "))
print(str_a.split("  "))
print(str_a.split("\n"))

# split first element by parameter "."
print(str_a.split(".", 1))

print(str_a.rsplit(" ", 1))
print(type(str_a.split()))  # <class 'list'> return a list.

first, *rest = str_url.split(".")
print("First part is: ", first)  # www
# by slice[]
slice_str = str_url[:3]
print("by slice: ", slice_str)

print("Rest part is: ", *rest)  # how all elements in the list
print("The list of rest part: ", rest)  # ['google', 'com/search']

# split() function is to get part of text from the original
part_str = str_url.split(",")
