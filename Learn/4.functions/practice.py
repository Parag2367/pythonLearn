"""
Write a Python function to reverse a string using slicing and return it.
"""


# def reverse(a: str):
#     b = a[::-1]
#     return b


# d = reverse("hello world")
# print(d)


"""
Write a Python function that accepts a string and counts the number of
upper and lower case letters.
"""


# def count(a: str):
#     countu = 0
#     countl = 0
#     for i in a:
#         ascii = ord(i)
#         if ascii >= 65 and ascii <= 90:
#             countu = countu + 1
#         elif ascii >= 97 and ascii <= 122:
#             countl = countl + 1
#     print(f"Count of uppercase {countu}")
#     print(f"Count of lowercase {countl}")


# my_string = "heeloo WORLD i AM"
# count(my_string)


"""
Write a Python function that takes a list and returns a new list with distinct
elements from the first list.
"""


# def unique(l: list):
#     l1 = []
#     for a in l:
#         if a not in l1:
#             l1.append(a)
#         else:
#             continue
#     print(l1)


# my_list = [11, 11, 22, 44, 55, 33, 22, 44]
# unique(my_list)


"""
Write a Python function that takes a number as a parameter and checks
whether the number is prime or not.
"""


# def prime(num: int):
#     factor = 0
#     for a in range(1, num + 1):
#         if num % a == 0:
#             factor = factor + 1
#     if factor == 2:
#         print(f"{num} is a prime number")
#     else:
#         print(f"{num} is not a prime number")


# prime(7)


"""
Write a Python function that takes start_number and end_number as a
parameter. Now print all the prime numbers between start_number to
end_number.
"""


# def prime_between(n1, n2):
#     for a in range(n1, n2 + 1):
#         factor = 0
#         for i in range(1, a + 1):
#             if a % i == 0:
#                 factor = factor + 1
#         if factor == 2:
#             print(f"{a} is a prime number")


# prime_between(3, 11)

"""
Python function to print even length words in a string.
"""


# def even(a: str):
#     b = a.split()
#     c = []
#     for x in b:
#         if len(x) % 2 == 0:
#             if x not in c:
#                 c.append(x)
#             else:
#                 continue
#     print(c)


# my_string = "hello how aree your"
# even(my_string)


"""
Write a Python function to find the Maximum and minimum of three
numbers. Use 3 parameters. Make 2 different functions named as maxi and
mini.
"""


# def max(a: int, b: int, c: int):
#     max = a
#     if max < b:
#         max = b
#     if max < c:
#         max = c
#     print(f"max number is {max}")


# def min(a: int, b: int, c: int) -> None:
#     min = a
#     if min > b:
#         min = b
#     if min > c:
#         min = c
#     print(f"min is {min}")


# max(25, 52, 33)
# min(2, 4, 6)


"""
Attempt the same leap year question (Week 1 - Assignment 2 - Q8) but
using function. Try calling function with different years as a parameter and
check the output.

"""


# def leapYear(year: int) -> None:
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print(f"{year} is leap year")
#             else:
#                 print(f"{year} is not a leap year")
#         else:
#             print(f"{year} is leap year")
#     else:
#         print(f"{year} is not a leap year")


# leapYear(2024)


# def leap(year: int):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400):
#         print(f"{year} is a leap year")
#     else:
#         print(f"{year} is not a leap year")


# leap(2024)


"""
Create a function that takes three numbers as parameters and returns
the largest among them. Also if no arguments are passed, make sure the
parameters take default value as None and return answer as -1.

"""


def largest(
    num1: int | None = None, num2: int | None = None, num3: int | None = None
) -> int:
    if num1 != None and num2 != None and num3 != None:  # putting this is to restrict
        large = num1
        if num2 > large:
            large = num2
        elif num3 > large:
            large = num3
        return large
    else:
        return -1


a = largest(22, 0, 23)
print(a)


"""
# Ask 3 numbers from user. Make a function which returns the middle of
# those 3 numbers. Then make a function to check if that middle number is
# divisible by both 3 and 4. Make 2 functions for reusability.
# """


def middle(num1: float, num2: float, num3: float) -> float:
    if (num1 <= num2 <= num3) or (num3 <= num2 <= num1):
        return num2
    elif (num2 <= num1 <= num3) or (num3 <= num1 <= num2):
        return num1
    else:
        return num3


def check(num: float) -> None:
    if num % 3 == 0 and num % 4 == 0:
        print("divisible")
    else:
        print("Not divisible")


a: float = float(input("enter a number = "))
b: float = float(input("enter a number = "))
c: float = float(input("enter a number = "))

mid = middle(a, b, c)
print(mid)

check(mid)
