# coding:utf-8
# 4/26/21 1:34 PM

"""
    Key points:
        'INSERT INTO table(columns) VALUES(%s)'

            user_name = input("Enter user name: ")

            #
            insert_sql = 'INSERT INTO employee(name) VALUES(%s)'

            try:
                cursor.execute(insert_sql, user_name)
                mysql_conn.commit()
                print("Name is inserted.")
                pass
            except Exception as e:
                mysql_conn.rollback()  # rollback current transaction
                print("Exception", e)

        Functions for retrieving records from databases
            fetchone()
            fetchall()

            rowcount() return the number of record.
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

query_sql = 'SELECT * FROM userinfo'
try:
    cursor.execute(query_sql)
    results = cursor.fetchone()

    # for i in results.items():
    #     print(i)
    #     pass
    for key, value in results:
        print("%s %s" % (key, value))

except Exception as e:
    print("Exception: ", e)
pass

# close cursor() and connection
cursor.close()
mysql_conn.close()
