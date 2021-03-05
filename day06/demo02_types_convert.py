"""
    Type conversion function:
        int()
            return an integer object constructed from a number or string
        float()
            return a float point object constructed from a number or string
        str()
            return an integer object constructed from a number or string
        ord()
            Given a string representing one Unicode character,
            return an integer representing the Unicode code point of that character
        chr()
        bool()
        bin()
        hex()
        oct()
        list()
        tuple()
        dict()
        bytes()
            Return a new “bytes” object, which is an immutable sequence of integers in the range 0 <= x < 256.

"""
# bin() function
print(bin(999))  # 0b1111100111
print((bin(-999)))  # -0b1111100111

print(hex(999))  # 0x3e7
print(hex(20))  # 0x14

# tuple converts to list
my_tuple = (1, 2, 3, 4, 3, 4, 3, 4, 'unchangeable')  # unchangeable
print(type(my_tuple))  # <class 'tuple'>
print("my tuple:", my_tuple)
my_list = list(my_tuple)
print(type(my_list))  # <class 'list'>
my_list[8] = "changeable" # list can be modified.
print("my list:", my_list)  # [1, 2, 3, 4, 3, 4, 3, 4]

# dict type


# bytes() function
print(bytes("名古屋出身の女の子", encoding='utf-8'))
# b'\xe5\x90\x8d\xe5\x8f\xa4\xe5\xb1\x8b\xe5\x87\xba\xe8\xba\xab\xe3\x81\xae\xe5\xa5\xb3\xe3\x81\xae\xe5\xad\x90'

