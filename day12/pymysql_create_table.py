# coding:utf-8
# 4/26/21 12:53 PM

"""
    Create tables by pymysql module

"""
import pymysql

# establishment of mysql connection
mysql_conn = pymysql.connect(host="localhost",
                             port=3306,
                             user="root",
                             password="tyghbn",
                             database="testDB",
                             charset="utf8",
                             cursorclass=pymysql.cursors.DictCursor
                             )

# calling cursor() function
cursor = mysql_conn.cursor()

# drop table from db
del_table = 'DROP TABLE IF EXISTS employee'

# create table by pymysql
create_table = 'CREATE TABLE employee(id int auto_increment primary key, name varchar(20) NOT NULL)'

# pass sql statement to mysql
try:
    cursor.execute(del_table)
    print("Table is deleted.")
    cursor.execute(create_table)
    print("Table is established.")
except Exception as e:
    print("Exception: ", e)
    pass

# commit changes,
mysql_conn.commit()

# close cursor() and connection
mysql_conn.close()
cursor.close()
