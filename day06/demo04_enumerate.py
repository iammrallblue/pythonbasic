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
