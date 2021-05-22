# coding:utf-8
# 4/26/21 10:26 AM
"""
    CRUD by pymysql
        Create
        Insert Into:

        Retrieve
        Update
        Delete
        functions of pymysql:
            connect()
            cursor()
            cursor.execute(str_value, ('a','tuple))

            cursor.executemany(str_value, [list('tuples'),('tuples'),('tuples'),('tuples'),('tuples')])
            cursor.fetchone()
                return a dictionary
            cursor.fetchmany(int size)
                return a list which contains many tuples by specified size
            cursor.fetchall()
                return a list which contains many tuples
            cursor.scroll(number, mode='relative', or 'absolute)
                return a list started from specified rows
            cursor.lastrowid()

"""
import pymysql.cursors

# establishment the connection
connection = pymysql.connect(host="localhost",
                             port=3306,
                             user="root",
                             password="tyghbn",
                             database="testDB",
                             charset="utf8",
                             cursorclass=pymysql.cursors.DictCursor
                             )

# call cursor() function, return in a dictionary
cursor = connection.cursor(pymysql.cursors.DictCursor)

# passing sql statements by execute() function
# insert a new record to userinfo table, needs to know all columns first
insert_sql = 'INSERT INTO userinfo(user, passwd) VALUES(%s,%s)'
rows = cursor.execute(insert_sql, ("Abby", "123"))  # pass values as a tuple
print(rows)  # return a value, 1 is effected, 0 is something wrong

# insert into many record at one time to userinfo table
insert_sql = 'INSERT INTO userinfo(user, passwd) VALUES(%s,%s)'
many_rows = cursor.executemany(insert_sql, [("Cathy", "123"), ("Danielle", "123"), ("Eva", "123"), ("Farina", "123")])
print(many_rows)  # return an int value, since inter into 4 records, return value is 4

# update a record in userinfo table
update_sql = 'UPDATE userinfo SET passwd="999" WHERE id=3'
row = cursor.execute(update_sql)
print(row)  # return 1

# delete a record in userinfo table
delete_sql = 'DELETE FROM userinfo WHERE id=7'
row = cursor.execute(delete_sql)
print(row)  # return 1

# query records in userinfo table, and return data by fetchone() function
row = cursor.execute("SELECT * FROM userinfo;")
print(row)  # return an int value NOT DATA, 6

print(cursor.fetchone())  # return a tuple <class 'dict'>
print(cursor.fetchall())  # return a list which contains many tuples, <class 'list'>
print(cursor.fetchmany(3))  # return a list which contains many tuples, <class 'list'>

return_dict = cursor.fetchone()
for i, j in return_dict.items():
    print(i, j)
print(return_dict)

# using lastrowid() function to determine which row will be insert into
insert_sql = 'INSERT INTO userinfo(user,passwd) VALUES (%s,%s)'
rows = cursor.executemany(insert_sql, [("George", "123"), ("Frank", "456"), ("Hunter", "123"), ("Ivy", "456")])
print(rows)

# KEY, If executing CRUD statement, commit() function MUST be called
connection.commit()

# after sql statement finished
cursor.close()
connection.close()
