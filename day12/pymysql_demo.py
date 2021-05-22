# coding:utf-8
# 4/24/21 9:49 PM

import pymysql.cursors

"""
    USAGE of pymysql module
        key points:
            1. establishment of mysql connection by pymysql.connect()
            2. MUST call pymysql.cursor() for passing sql statements
            3. Using cursor() to pass sql statement   
            4. Executing sql statement by cursor.execute() function, then return the result
            5. Calling fetchone() or fetchall() function to get data from table (userinfo)
                ** if user and password are correct
                ** fetchone() return a dict
                ** fetchall() return a list
            5. Closing function cursor(), and mysql connection after received result
            6. Verifying user and password.

            ** pymysql.cursors.DictCursor, return result in a dictionary       
    ISSUE:
        to prevent mysql injection bug
"""
# receive user input
user_name = input("User Name: ").strip()
passwd = input("Enter password: ").strip()

# establishment of mysql connection
connection = pymysql.connect(host="localhost",
                             port=3306,
                             user="root",
                             password="tyghbn",
                             database="testDB",
                             charset="utf8",
                             cursorclass=pymysql.cursors.DictCursor
                             )
# call cursor() function from new object "connection", return result in form of dictionary
cursor = connection.cursor()  # <class 'pymysql.cursors.DictCursor'>

# using cursor() function to pass sql statements which is a str
query_sql = 'SELECT * FROM userinfo WHERE user="%s" AND passwd="%s"' % (user_name, passwd)

# execute sql statement and return 1 or 0, 1 means user and password are correct, otherwise.
rows = cursor.execute(query_sql)
print(rows)
# check rows
# print(type(rows))

result = cursor.fetchone()  # return <class 'dict'> to result

for i in result:
    print(i)  # {'id': 1, 'user': 'Jun', 'passwd': '123'}
    pass

cursor.close()
connection.close()

# verifying user and password by if statement
if rows:
    print("Welcome {} !".format(user_name))
    pass
else:
    print("User name or Password is Wrong!")
    pass

# check user and password
if result["user"] == 'Jun':
    print("it's a good sign..")
elif result["user"] == "Bella":
    print("it's a good sign as well..")
else:
    print("code should be modified.")
    pass
