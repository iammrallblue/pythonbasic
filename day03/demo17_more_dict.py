# coding:utf-8
# 3/22/21 6:32 PM
"""
    continue
        dict type:
            my_dict = {"a":"A", "b":"B"}
            this_dict = {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
            }
        Key point:
            1. dict type can be used as switch... case statement
            2. list type can be the value in the dict

        Common Functions:
            get()
                The get() method returns the value of the item with the specified key.
            setdefault()
                The setdefault() method returns the value of the item with the specified key.
                Syntax:
                    my_dict.setdefault("key","value")

"""
my_dict = {}

# add key and value
my_dict["Name"] = "Abby"
print(my_dict)  # {'Name': 'Abby'}

# replace switch case statement
my_dict2 = {
    "0": "Zero",
    "1": "One",
    "2": "Two"
}

# arg = input(">>:")
#
# get_value = my_dict2.get(arg, "nothing")
# print(get_value)

while True:

    arg = input(">>:")  # input key to find value
    if arg == "Exit" or arg == "exit":
        # exit()
        break
        pass
    else:
        # get()
        get_value = my_dict2.get(arg, "nothing")  # get() function finds the value by key
        print(get_value)
        pass
    pass
pass

# setdefault() function
my_dict3 = {"a": "1"}

return_value = my_dict3.setdefault("a")  # parameter is the key in the dict
print(return_value)  # return value by key, the value is 1
print(my_dict3)  # print out my_dict3, {'a': '1'}

# add key and value if don't exist
my_dict3.setdefault("b", "Bella")
print(my_dict3)  # {'a': '1', 'b': 'Bella'}

# list as value in dict
list_as_value = my_dict3.setdefault("list", [])
print(list_as_value)  # [], return an empty list
print(type(my_dict3["list"]))  # <class 'list'>
print(id(my_dict3["list"]))  # 4441325888

print(my_dict3)  # {'a': '1', 'b': 'Bella', 'list': []}

# # add elements to the list in my_dict3
add_elem = my_dict3.setdefault("list", []).append(1)
print(my_dict3)  # {'a': '1', 'b': 'Bella', 'list': [1]}
