"""
    Mapping type - Dictionary (dict)
        Dictionaries are used to store data values in key:value pairs.
        it's not a sequence, it is unordered key: value pairs.
        format:
            my_dict = {"a":"A", "b":"B"}
            this_dict = {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
            }
        key point:
            1. A dictionary is a collection which is ordered*,
            2. changeable
            3. does not allow duplicates.
            4. using for loop to iterate the dict
        Common functions/methods
            1. add key:value pair into a dict
                format:
                    my_dict["Key"] = "Value"
            2. keys()
                print out all keys in the dict
            3. values()
                print out all values in the dict
            4. items()
                print out keys and values together
            5. update({"key":value})
                update the key:value in dict
                or if dict does not exist the key:value, update() will
                add key:value as new data in the end of dict.
            6. del, to delete key:value
            7. pop()
                delete key:value from the dict
            8. sorted()
                a) sort by key
                b) sort by value
            9. keyword in
                to determine whether elements in the dict or not
                return True, False
            10. hash()
                    Return the hash value for the given object.

"""
# define an empty dict
my_dict = {}
print(type(my_dict))  # <class 'dict'>
print(my_dict)  # {}
print(id(my_dict))  # 4414216896

# define a dict with data
my_dict = {"Brand": "Audi", "Make": "Germany", "Year": 2021}
# add an key:value pair to my_dict
my_dict["name"] = "Bella"
my_dict["age"] = "25"
my_dict["career"] = "Student"
my_dict["gender"] = "Female"
print(id(my_dict))  # 4473875200 ,it's the same dict

# the length of dict
print(len(my_dict))  # 7

# print out value by the key
print(my_dict["name"])  # Bella

# edit the key:value in the dict
my_dict["name"] = "Abby"
print(my_dict["name"])  # Abby

# print out all keys by function keys()
print(my_dict.keys())  # dict_keys(['Brand', 'Make', 'Year', 'name', 'age', 'career', 'gender'])

# print out all values by function values()
print(my_dict.values())  # dict_values(['Audi', 'Germany', 2021, 'Abby', 25, 'Student', 'Female'])

# keys and values together print out
print(my_dict.items())
# dict_items([('Brand', 'Audi'), ('Make', 'Germany'), ('Year', 2021), ('name', 'Abby'),
# ('age', 25), ('career', 'Student'), ('gender', 'Female')])

# iterating by for loop
# for i in my_dict.items():
#     print(i)
#     pass
for key, value in my_dict.items():
    print("%s == %s" % (key, value))

# update key:value in dict by update() function
my_dict.update({"Brand": "BMW"})
print(my_dict.items())

# add key:value in the end of dict by update() as new data
my_dict.update({"Phone": "6787779999"})
for key, value in my_dict.items():
    print("%s == %s " % (key, value))

# delete {key:value}
del my_dict["Year"]
print(my_dict.items())

# delete {key:value} by pop("key") function
my_dict.pop("career")

print(my_dict.items())

# sorting a dict by sorted(), using key as keyword of sorting
print(sorted(my_dict.items(), key=lambda d: d[0]))  # 0 == key, reordered.

# sorting a dict by sorted(), using value as keyword of sorting
print(sorted(my_dict.items(), key=lambda d: d[1]))  # 1 == value, reordered.
# if keys or values are not same data type, it will post
# TypeError: '<' not supported between instances of 'int' and 'str'
# solution: to change all data type in same form

# find element by in keyword
print("Phone" in my_dict)  # True

# hash() function
print(hash(True))  # 1
print(hash(100))
# print(hash([1])) # TypeError: unhashable type: 'list'
