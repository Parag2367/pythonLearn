# num1: int = int(input("Enter number 1 = "))
# num2: int = int(input("Enter number 2 = "))

# if num1 > num2:
#     print("num1 is greater")

# elif num1 == num2:
#     print("they are equal")

# else:
#     print("num2 is greater")


# ###########################

# num=int(input("Enter number to check = "))

# if (num%2 == 0):
#     print("it is an even number")
# else:
#     print("it is an odd number")


# #########################

# phy = int(input("Enter physics marks = "))
# chem = int(input("Enter chemistry marks = "))

# if (phy > 33 and chem > 33):
#     print("PASS")

# else:
#     print("Fail")


# #########################

# integer = int(input("Enter a number = "))

# if(integer >= 0):
#     print("checking number")
#     print("It is a positive number")

# else:
#     print("checking number")
#     print("It is a negative number")


##########################

# letter = input("Enter a letter = ")

# if ( letter in ['a','e','i','o','u']):
#     print("It is a vowel")

# else:
#     print("it is a consonant")


# #############################

# num1 = int(input("enter num1 = "))
# num2 = int(input("enter num2 = "))

# if (num1 % num2 == 0):
#     print("num1 and num2 are divisible by each other")

# else:
#     print("they are not divisible")


###################################


# held = int(input("Number of classes held = "))
# attended = int(input("Number of classes attended = "))


# allowed = (attended/held) * 100

# if (allowed >= 75.0):
#     print("you are allowed for giving exams atendace is",allowed)

# else:
#     print("You are nit allowed! come meet me in office attendance is",allowed)


#############################

# marks1 = int(input("enter marks = "))
# marks2 = int(input("enter marks = "))
# marks3 = int(input("enter marks = "))
# marks4 = int(input("enter marks = "))
# marks5 = int(input("enter marks = "))

# total = marks1 + marks2 + marks3 + marks4 + marks5
# percentage = (total / 500) * 100
# print("percentage is", percentage)

# if percentage >= 81 and percentage <= 100:
#     print("Grade A")
# elif percentage >= 71 and percentage <= 80:
#     print("Grade B")
# elif percentage >= 65 and percentage <= 70:
#     print("Grade C")
# elif percentage >= 61 and percentage <= 65:
#     print("Grade D")
# elif percentage >= 1 and percentage <= 60:
#     print("Grade E")
# else:
#     print("invalid percentage")


### An example of how if, elif ,else flows:
# percentage: float = float(input("Enter your percentage = "))

# if percentage >= 81 and percentage <= 100:
#     print("Grade A")
# if percentage >= 71 and percentage <= 80:
#     print("Grade B")
# if percentage >= 65 and percentage <= 70:
#     print("Grade C")
# if percentage >= 61 and percentage <= 65:
#     print("Grade D")
# if percentage >= 1 and percentage <= 60:
#     print("Grade E")
# else:
#     print("invalid percentage")

# the ouput for this will also print else part as it will check all the if condition ,
# but if we have used elif  it would have only checked one condition and come out of the condition


"""
Ask a number from user
print 'Yes' if it is divisible by 5 and 6
else No
"""

# num: int = int(input("Enter a number = "))

# if num % 5 == 0 and num % 6 == 0:
#     print("Yes")
# else:
#     print("No")


"""
foobar
num%3 num%5
"""

num: int = int(input("Enter a number = "))

if num % 3 == 0 and num % 5 == 0:
    print("FOOBAR")
elif num % 3 == 0:
    print("foo")
elif num % 5 == 0:
    print("bar")
else:
    print("FOOFOOBARBAR")


"""
Types of Triangle
"""

angle1: float = float(input("Enter an angle = "))
angle2: float = float(input("Enter an angle = "))
angle3: float = float(input("Enter an angle = "))

sum = angle1 + angle2 + angle3

if sum > 0 and sum <= 180:
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("Right angle")
    elif angle1 < 90 and angle2 < 90 and angle3 < 90:
        print("Acute triangle")
    else:
        print("Obtuse angle")
else:
    print("sum of angles should be between 0 and 180")
