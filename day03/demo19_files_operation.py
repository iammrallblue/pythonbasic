# coding:utf-8
# 3/23/21 7:10 PM
"""
    File Operation:

        Common Function/Method:
            open(file, mode='r', encoding='utf-8')
                Open file and return a stream.  Raise OSError upon failure.
            read()
            readline()
            readlines()

            mode:
                r, w, a, rb, wb, ab,
            encoding
                return the encode of the file
            readable()
                return boolean values, True is readable, False is unreadable
                if mode of the file is "w" or "a", the readable() will return False
            name
                return the file's name
            write()
                adding ONLY str, the argument MUST be str
            writelines()
                adding content line by line, the argument can be list, or str



"""

# create an object of the file, in reading mode
file_obj = open("tmp.txt", "r", encoding='utf-8')

# # read() method, read the whole content of the file
# file_content = file_obj.read()
# file_obj.close()
# print(file_content)

# # readlines() method, reading all file lines
# file_content = file_obj.readlines()
# print(file_content)
# # ['Be nice to th world, then you will have the love from the whole world.\n', 'ABC\n', 'abc\n', '123']

# encoding, to show encode of the file
print(file_obj.encoding)  # utf-8

# readable(), check files readability
print(file_obj.readable())  # True
# ** if file mode is "w" or "a", readable() will return False

# name, get file's name
print(file_obj.name)  # tmp.txt

# create an object of the file, in writing mode
file_write = open("tmp.txt", "w", encoding='utf-8')

# writelines(),
file_write.writelines(['a\n', 'b\n', 'c\n'])
file_write.write("1")
file_write.close()
# # write() method, to write content to the file
# file_write.write("Be nice to the world, then you will have the love from the whole world.\n")
