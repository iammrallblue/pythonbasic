# coding:utf-8
# 4/24/21 9:49 PM

import pymysql.cursors

"""
    The MySQL Injection Bug,    
    ISSUE:
        to prevent mysql injection bug
        when input Jun" -- xxxx
        Enter password: leave black
        SELECT * FROM userinfo WHERE user="Jun" -- xxxx" AND passwd=""
                                            everything after -- will be avoided.
        Welcome Jun" -- xxxx !
        still can login successful w/o password
    SOLUTION:
        query_sql = 'SELECT * FROM userinfo WHERE user=%s AND passwd=%s'
        rows = cursor.execute(query_sql,(user_name, passwd))
        put parameters user_name, and passwd in function execute can void the MySQL injection bug.
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
query_sql = 'SELECT * FROM userinfo WHERE user=%s AND passwd=%s'

# execute sql statement and return 1 or 0, 1 means user and password are correct, otherwise.
rows = cursor.execute(query_sql, (user_name, passwd))
# check rows
print(rows)

result = cursor.fetchone()  # return <class 'dict'> to result

# print(query_sql)

cursor.close()
connection.close()

# verifying user and password by if statement
if rows:
    print("Welcome {} !".format(user_name))
    pass
else:
    print("User name or Password is Wrong!")
    pass
