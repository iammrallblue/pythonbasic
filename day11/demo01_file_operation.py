"""
    File Operation:
        functions for operate local files

    Common Functions:
        open("file", "w/wb/a/r", encoding="utf-8")
            Open file and return a corresponding file object.
        write()
            method write() writes a string str to the file. There is no return value.
            might show up after flush() and close() is called
        read()
            returns the specified number of bytes from the file.
            Default is -1 which means the whole file.
        readline(size)
            The readline() method returns one line from the file.
            You can also specified how many bytes from the line to return,
            by using the size parameter.
            parameter:
                size: Optional. The number of bytes from the line to return.
                      Default -1, which means the whole line.
        readlines()
            return all lines in form of list []

    Key point:
        1. specify a format to files.
            encoding="utf-8"

        2. It's better to call close() function at the end, when the object of file
            is no longer needed. it can prevent memory overflow.
"""

# # create an object of txt document, created if not existed,
# txt_obj = open("./tmp.txt", "w", encoding="utf-8")
#
# # writing and reading operation
# txt_obj.write("Bella is my wife.")
# txt_obj.write("she had me at-hello.")
# txt_obj.write("春華秋實，春花秋月")
# txt_obj.close()
#
# # writing data info file as binary
# txt_obj = open("./tmp.txt", "wb")  # str -> bytes
# txt_obj.write("Deer park water".encode("utf-8"))
# txt_obj.close()
#
# # appending data at the end of the file
# txt_obj = open("./tmp.txt", "a", encoding="utf-8")
# txt_obj.write("\r\nthis is a appended statement.")
# txt_obj.close()

# read a file
# txt_obj = open("./tmp.txt", "r")
# print(txt_obj.read())  # show all content in the file

# read specified characters in the file
# print(txt_obj.read(8))  # Deer par
# print(txt_obj.read())  # starts from k,

# # read one line in the file
# print(txt_obj.readline())  # result, Deer park water
#
# print(txt_obj.readlines())
# # ['this is a appended statement.\n', '\n', 'Bella is my wife.\n', 'She had me at-hello']

txt_obj = open("./tmp.txt", "rb")  # to read tmp.txt as binary
data = txt_obj.read()
print(data.decode("utf-8"))  # decode the binary to utf-8, if decode to others such as gbk,
# it will post error UnicodeDecodeError:
# 'gbk' codec can't decode byte 0x80 in position 98: illegal multibyte sequence

txt_obj.close()  # close the txt object
