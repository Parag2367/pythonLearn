# num1 = int(input("Enter number = "))
# num2 = int(input("Enter number = "))
# num3 = int(input("Enter number = "))

# if num1 > num2:
#     if num1 > num3:
#         print("num1 is greater")
#     else:
#         print("num3 is greater")
# elif num2 > num1:
#     if num2 > num3:
#         print("num2 is greater")
#     else:
#         print("num3 is greater")


################################

# year = int(input("Enter year = "))

# if year%4 == 0:
#     if year%100 == 0:
#         if year%400 == 0:
#             print("It is a leap year")
#         else :
#             print("It is not a leap year")
#     else:
#         print("It is a leap year")
# else:
#     print("it is not a leap year")


#############################

# weight = float(input("weight in kgs = "))
# height = float(input("height in meters = "))

# bmi = round(weight / (height**2), 2)

# if bmi <= 29.9:
#     if bmi > 25 and bmi <= 29.9:
#         print("overweight as your bmi is", bmi)
#     elif bmi > 18.5 and bmi <= 25:
#         print("normal weight as your bmi is", bmi)
#     else:
#         print("underweight as uour bmi is", bmi)
# else:
#     print("obesity as your bmi is", bmi)


"""
Rock , paper ,scissor
"""
# import random

# options = ["rock", "paper", "scissors"]
# comp_guess = random.choice(options)
# print(comp_guess)

# guess = input("Enter anything from rock/paper/scissors = ")

# if guess == comp_guess:
#     print("No one wins")
# elif guess == "paper" and comp_guess == "rock":
#     print("User wins")
# elif guess == "scissors" and comp_guess == "paper":
#     print("User wins")
# elif guess == "rock" and comp_guess == "scissors":
#     print("User wins")
# else:
#     print("Computer wins as it is", comp_guess)


"""
Leap year
"""
year = int(input("Enter year = "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        print(
            "It is a leap year"
        )  # year which are less than 100, and years which are > then 100 and not divisible by 100
else:
    print("Not a leap year")
