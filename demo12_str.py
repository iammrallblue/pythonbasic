"""
    Text Sequence Type:
        str:
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
                    return the boolean value True and Fals if prefix and suffix are contained
                    the specific character.
                8. lower() and upper()
                    convert all letters to lower or upper.
                9. len()
                    print out the lenth of th string
"""
# define a string
string = "I'm a string."

# print out the first letter of string by using index of string
print("First letter is %s in the string." % string[0])
print("letter in the string. %s" % string[4])

# iterating a string by for loop
for letters in string:
    print(letters, end="  ")
    pass

# function capitalize()
string = "beautiful"
print("\n capitalize a string word %s to: %s" % (string, string.capitalize()))
pass

# function strip(), to get rid of empty space in a string
string = "    beautiful soul    "
no_space_string = string.strip()
print("the original string word: ", string)
print("after calling strip() function: ", no_space_string)
# function lstrip() , to get rid of empty space on the left side of string
string = "     hiking day     "
print(string.lstrip())  # eliminate empty space on the left
print(string.rstrip())  # eliminate empty space on the right

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
# the lenth of the string msg_str
print(len(msg_str))  # length is 12
