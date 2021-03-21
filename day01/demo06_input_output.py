"""
    input() and output() functions:
        input([prompt]) function:
          if prompt argument is present. then the input() function read a line from input
          *** convert it to a string, and return that.***
          name = input("type your name: ")

        print out format text:
          %s, string
          %d, int
          %f, float
          %u,
          format:
              msg = '''
              %s
              %s
              ''' % (, , ,)
          key point:
            1. ''' ''' format text output
            2 % (), to show all variables
            3. %s, reserved position for all variables
                s means string it can save all type of data.
            4. all data input() will convert to a string
                therefore in the msg, we use all %s to reserved
                position for all variable
            5. %d means for digital numbers, but in this instance
                it will post typeerror because all data converted to strings.
                solution:
                    if some data need to save as other types such as saving age as int
                    age = int(input("Age: "), then can use %d to reserve position for age
            6.  %f, float numeric.
            7. strip()
                    Removes any leading (spaces at the beginning) and trailing (spaces at the end)
                    characters (space is the default leading character to remove)
"""

# # input some values
# name = input("Enter your name: ")
# age = int(input("Age: "))
# gender = input("Gender: ")
# like_weather = input("Do you like rain day.")
#
# # show all input information by using % placeholders
# print("My name is %s, I'm %d years old." % (name, age))
# # print("Age: ", age)
# print("Gender: ", gender)
#
# # format text print out
# msg = '''
# --- Personal Info ---
# Name: %s
# Age:  %d
# Gender: %s
# Weather-Like: %s
# --- End ---
# ''' % (name, age, gender, like_weather)
# print(msg)
#
# if like_weather == "yes" or like_weather == "Yes":
#     print("I like rain day.")

# # how to use \n
# print("this is a whole line print out.")
# print("a line \n separate to two line")  # one line separate to two.

# instance of input() function
# to print out information from user input()
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_gender = input("What is your gender:")
stu_id = int(input("What is your student id: "))
user_address = input("Enter your home address:")
zip_code = int(input("Enter your zip code: "))

# # by string formatting operator %
# print("Your information")
# print("Name: %s" % user_name)
# print("Age: %d" % user_age)
# print("Gender: %s" % user_gender)
# print("Student ID: %s" % stu_id)
# print("Address: %s %d" % (user_address, zip_code))

# by placeholder {}
print("Your Info: ")
print("Name: {}".format(user_name))
print("Age: {}".format(user_age))
print("Gender: {}".format(user_gender))
print("Student ID: {}".format(stu_id))
print("Address: {} {}".format(user_address, zip_code))

# strip() function to remove any space from input
u_name = input("User Name: ").strip()
if u_name == "root":
    print("good user")
    pass

print("wrong input")
