"""
    Ways to add comments
        1. single line comment, block comment
            a. block comment
                explains the code that follows it.
                Typically, you indent a block comment at the same level as the code block.
                see below
            b. inline comment
                A comment places on the same line with a statement,
                see below
        2. docstrings, aka multiple line comments
            A documentation string is a string literal that you put as the first lines in a code block,
            for example, a function.
            *** it can write in one line***
            see below
        3. special comments in Linux/Unix or Mas OS,
            which are always in the first line of every python files (xxx.py)
                a. #!/usr/bin/python3
                b. # -- coding = utf-8 --, in Python 3, utf-8 is default format.

"""
# Single line comment

# comment tells that code block is about retail price, this is a block comment
retail_price = 15.43

# this is a inline comment
print(retail_price)  # to show retail price of products.

# docstring, multiple line comment
"""
    this is multiple line comment (recommended) 
"""

'''
    this is multiple line comment
'''

# one line docstring
"""this is one line docstring."""
