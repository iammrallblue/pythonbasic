import random

"""
    1. guessing number to match a random number which is generated by function random
        players have 3 attempts to guess number, if players ran out of 3 attempts, ask players 
        whether to continue or to end the game.
        
            a. while loop with if statement to achieve  

"""
# import random, to generate a random number
counter = 0
ran_number = random.randint(0, 10)  # (0,10]
while counter <= 3:  # 3 attempts
    input_number = int(input("Enter guessing number: "))  # user input a number to match random number
    if input_number == ran_number:
        print("Bingo, You got it")
        break  # end game if attempt is within 3 times.
        pass
    elif input_number > ran_number:
        print("Guessing number is greater than random number")
        pass
    else:
        print("Guessing number is less than random number")
        pass
    counter += 1

    # asking user whether to continue or to quit the game after 3 attempted.
    if counter == 3:
        choice = input("Keep going press Y/y, otherwise N/n")
        if choice == "y" or choice == "Y":
            counter = 0  # user keeping play, set counter to 0
            pass
        elif choice == "n" or choice == "N":  # user ended game
            break  # end the game
            pass
        else:
            print("Input Error, Hint: Y/y, or N/n")
            pass
pass
