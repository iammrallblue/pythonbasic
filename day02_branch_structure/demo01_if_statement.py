# coding:utf-8
# 3/31/21 6:56 PM
"""
    1. if statement (single if)
            format:
                if cond_expr:
                    expr_1
                    expr_2
                    ...
        Usage:
            if-statement:
    2. multiple if...elif...elif...elif...else
                format:
                    if cond_expr:
                        expr_1
                        expr_2
                        ...
                    elif cond_expr_2:
                        expr_3
                        expr_4
                    elif con_expr_3:
                        expr_5
                        expr_6
                    else:
                        expr_7
                        expr_8
    Instance:
        to verify user inputs by if-else statement.
"""
username = input("Enter user name: ")
password = input("Enter user password: ")

if username == "admin" and password == "123":
    print("Matched, Welcome {}".format(username))
    pass
else:
    print("Mismatched.")
    pass
