# coding:utf-8
# 3/23/21 7:10 PM
"""
    File Operation:

        Common Function/Method:
            open(file, mode='r', encoding='utf-8')
                Open file and return a stream.  Raise OSError upon failure.
            read()
            readline()
            write()
            mode:
                r, w, a, rb, wb, ab,
"""

# create an object of the file, in reading mode
file_obj = open("tmp.txt", "r", encoding='utf-8')

# read() method, read the whole content of the file
file_content = file_obj.read()
file_obj.close()
print(file_content)

# readline() method, reading one line of the file

# create an object of the file, in writing mode
file_write = open("tmp.txt", "w", encoding='utf-8')

# write() method, to write content to the file
file_write.write("Be nice to the world, then you will have the love from the whole world.\n")

