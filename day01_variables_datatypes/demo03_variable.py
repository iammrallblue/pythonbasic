"""
    Variable:
        Variables are nothing but reserved memory locations to store values.
        Key point:
            1. format:
                variable_name = value
                            x = 3
            2. not like Java or C/C++
                declare a datatype before defining a variable
                in java, int x = 1; String name = "Bella"
            
                in Python, the datatype is hidden,
                    x = 1, name = "Bella"
            3. Multiple Assignment:
                x = y = z = 1
                m, n, v = 1, true, "Bella"
            
            4. many time assign values
                x = 1
                x = 2
                x = 20
                here, x can be assigned many different values
                in different time.
            5. reserved words
                import keyword
                  keyword.wklist
            6. three characteristics of an object in Python:
                a) all values have an unique memory hashcode in the memory
                    i = 3
                    print(id(i)), show the memory hashcode
                b) values can be different data types.
                    i = 3, i is an int type.
                    print(type(i)) <class 'int'>
                c) values itself
                    print(type(10)) <class 'int'>
            7. type() function:
                    type() method returns class type of the argument(object) passed as parameter.
                    type() function is mostly used for debugging purposes.
            8. Some builtin functions can convert data types.
                int(),
                float()
                str()
                chr()
                ord()
"""
import keyword

# how to declare variables
# int variables x, and y
x = 3
print(x)  # 3

# dynamic variable
y = x
print(y)  # 3

y = 10
print(x + y)  # 13

# declaration of variables
name = "Bella"
age = 19
height = 170.2
print("Name: {}".format(name), "Age: %d" % age, "Height: %f" % height)

address = "1101 Elise Ln Georgia"
print("Address: " + address)

# Constant in Python.
OLD_PEOPLE = "Senior"
print(OLD_PEOPLE)  # Constant format in Python

# reserved words can not use for variables, methods, classes
# print(keyword.kwlist, end="\n")
is_bool = keyword.iskeyword("del")  # return True is keyword
print(is_bool)

print(id(x))  # 4397353328

print(type(x))

print(type(10))

# type() function, return the class tyep of parameters
a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'complex'>
print(type(d))  # <class 'str'>
print(type(e))  # <class 'bool'>

# builtin functions, int(), float(), str(), chr(), ord()
x = int(input("Value will convert to int: "))
print("x is int: ", x)
y = float(input("Value will convert to float: "))
print("y is float: ", y)
