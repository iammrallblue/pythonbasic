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
"""

# how to declare variables
# int variables x, and y
x = 3
print(x)  # 3
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
