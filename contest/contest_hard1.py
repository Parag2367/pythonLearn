"""
Make a function named reverse which accepts an integer n from the
user. Reverse the number passed as a parameter and return the reverse
number. Do not use STRINGS.
"""

# def reversed(num: int) -> int:
#     n = num
#     y = 0
#     while n > 0:
#         y = (y* 10) + n%10
#         n = n // 10
#     return y


# a = reversed(1234)
# print(a)


"""
Make a function named checkPalindrome which accepts an integer n
from the user. Return True or False if the number is palindrome or not.
"""


# def checkPalindrone(num):
#     y = 0
#     n = num
#     while n > 0:
#         y = (y*10) + n%10
#         n = n // 10
#     if y == num:
#         print("yes palindrome")
#     else:
#         print("No")


# checkPalindrone(1221)


"""
Make a function named printWords which accepts an integer n from
the user. Print the number as words.

"""

# def refer(num):
#     if

# def printWords(num:int)-> str:


"""
Make a function named checkArmstrong which accepts an integer n
from the user. Return True or False if that number is an armstrong number.
"""


# def checkArmstrong(num: int):
#     x = num
#     total = 0
#     while x > 0:
#         total = total + (x % 10) ** 3
#         x = x // 10
#     if total == num:
#         print(f"{num} is armstrong")
#     else:
#         print("Not armstrong")


# checkArmstrong(153)
# checkArmstrong(407)


"""
Make a function named sumOfFirstAndLastDigit which accepts an
integer n from the user. Calculate the sum of first and last digit of a
number and return it.
"""


# def sumOfFirstAndLastDigit(num: int) -> int:
#     if num <= 9:
#         return num  # when num is less than 9
#     # other cases
#     n = num
#     last_digit = n % 10  # never change the given number always create a variable

#     while n > 0:
#         if n <= 9:
#             first_digit = n
#             break
#         n = (
#             n // 10
#         )  # this always gives integer , 123//10 == 12, 12//10 == 1(this is less than 9), 1//10 == 0
#     # return first_digit + last_digit


# print(sumOfFirstAndLastDigit(123456))
