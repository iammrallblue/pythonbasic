"""
    function enumerate(iterable, start=0)
        Return an enumerate object. iterable must be a sequence,
        an iterator, or some other object which supports iteration.
        key point:
            1. it can use for iterating tuple, dict..
            2. it can set a specified index, enumerate(list, 3)
                index starts from 3
"""
list_a = ["Abby", "Bella", "Cathy", "Danielle"]
for ele in enumerate(list_a):
    print(ele)
    pass
# function enumerate() will add numbers for each peson
# (0, 'Abby')
# (1, 'Bella')
# (2, 'Cathy')
# (3, 'Danielle')

# the index is not mandatory from 0.
list_b = ["Abby", "Bella", "Cathy", "Danielle"]
for index, person in enumerate(list_b, 3):
    # print(person, index)
    print(index, person)
    pass

# function enumerate() with dict
my_dict = {}
my_dict["Name"] = "Joey"
my_dict["Age"] = "23"
my_dict["Career"] = "Arist"
print(my_dict)  # {'Name': 'Joey', 'Age': '23', 'Career': 'Arist'}

# for loop to iterate my_dict
for i in enumerate(my_dict):
    print(i)
    pass

# (0, 'Name')
# (1, 'Age')
# (2, 'Career')
