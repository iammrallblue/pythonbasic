"""
    Control Structures:
        1. Sequential Structure
            The first statement in a function is executed first, followed by the second, and so on.
            natural order from top to bottom.

        2. Selection Structure/Condition Control Structure
            a. if statement (single if)
                format:
                    if cond_expr:
                        expr_1
                        expr_2
                        ...
            b. if...else statement
                format:
                    if cond_expr:
                        expr_1
                        expr_2
                        ...
                    else:
                        expr_3
                        expr_4
                        ...
            c. multiple if...elif...elif...elif...else
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
            Key point:
                1. cond_expr can be Logic, Comparison, Assignment, Operators.
                2. indentation, expressions MUST have a indent at beginning of expressions.
                (see print("x is greater than y."))
                (see if-statements in condition_if_statement.py

        3. Iteration/Loop Structure
            a. while loop statement (see demo09_while_loop_statement.py)
                format:
                    while cond_expr:
                        expr_1
                        expr_2
                while condition is true, while loop will keep looping.
            b. for loop statement (see for_loop_statement)
                A for loop is used for iterating over a sequence
                (that is either a list, a tuple, a dictionary, a set, or a string).
                format:
                    for ... in (str,list,tuple,set.):
                        print(...)
"""
