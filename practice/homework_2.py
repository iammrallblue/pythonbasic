"""
    requiring person's height and weight for calculating BMI:
        1. less than 18.5 -->
        2. btw 18.5 - 25
        3. 25 - 28
        4. 28 - 32
        5. 32
        6. over 32
      key point:
        a. using if...elif..else statement for procedures control.
"""

# input weight and height for BMI calculation
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

# formula of BMI
BMI = weight / (height ** 2)
if BMI < 18.5:
    print("You are in underweight range.")
    pass
elif 18.5 < BMI < 25:
    print("You are in normal or healthy weight range.")
    pass
elif 25 < BMI < 28:
    print("You are in overweight range.")
    pass
elif 28 < BMI < 30:
    print("You are overweight.")
    pass
else:
    print("You are in obese range, eat healthy..")
    pass
pass

# def BMI(height, weight):
#     bmi = weight / (height ** 2)
#     return bmi
#
#
# height = 1.6616
# weight = 57
#
# bmi = BMI(height, weight)
# print("The BMI is", format(bmi))
#
# print("Health status = ", end="")
# if (bmi < 18.5):
#     print("Underweight")
#
# elif (bmi >= 18.5 and bmi < 24.9):
#     print("Healthy")
#
# elif (bmi >= 24.9 and bmi < 30):
#     print("Overweight")
#
# elif (bmi >= 30):
#     print("Suffering from Obesity")
