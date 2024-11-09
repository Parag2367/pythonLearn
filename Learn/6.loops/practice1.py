"""
Create a function named factorial which takes a integer as an input and
returns the factorial of that number.
"""

# def factorial(num: int) -> int:
#     if num != 0:
#         fact = 1
#         i = num
#         while i >= 1:
#             fact = fact * i
#             i = i - 1
#         return fact
#     else:
#         fact = 1
#         return fact


# x = factorial(0)
# print(x)


"""
Create a function named pattern which takes an integer as an input
and print the following pattern.
pattern(4)
10 20 30 40
"""


# def pattern(num):
#     i = 1
#     while i <= num:
#         print(i * 10, end=" ")
#         i = i + 1


# pattern(4)


# another way
# def pattern(n):
#     num = 10
#     i = 1
#     while i <= n:
#         print(num, end=" ")
#         num = num + 10
#         i = i + 1


"""
Create a function named pattern which takes an integer as an input
and print the following pattern.
patern(4)
1 2 4 8
pattern(7)
1 2 4 8 16 32 64
"""


# def pattern(num):
#     i = 0
#     while i <= (num - 1):
#         print(2**i, end=" ")
#         i = i + 1


# pattern(7)


"""
Don’t create a function, just print the following pattern
1 11 111 1111 11111....n times (Ask n from user)
"""
# n: int = int(input("Enter a number = "))

# i = 1
# num = 1
# while i <= n:
#     print(num, end=" ")
#     num = (num * 10) + 1
#     i = i + 1


"""
1,11,101,1001,10001
"""
# n = 10
# i = 1
# num = 1
# while i <= n:
#     print(num, end=" ")
#     num = 10 ** (i) + 1
#     i = i + 1

"""
1 3 6 8 11 13 16 18
"""


# def pattern(n):
#     i = 0
#     num = 1
#     while i < n:
#         if i % 2 == 0:
#             print(num, end=" ")
#             num = num + 2
#         else:
#             print(num, end=" ")
#             num = num + 3
#         i = i + 1


# pattern(7)

"""
2 22 222 2222 22222 ... upto n. (Ask n from user)
"""


# def pattern(n):
#     i = 1
#     num = 2
#     while i <= n:
#         print(num, end=" ")
#         num = (num * 10) + 2


"""
1 + 1/2 +1/3+....
"""


# def harmonic(n):
#     i = 1
#     sum = 0
#     while i <= n:
#         sum = sum + (1 / i)
#         i = i + 1
#     print()
#     print(sum)


# harmonic(5)

"""
Ask x and n from user and then calculate the following answer.

"""


# def harmon(x, n):
#     total = 0
#     for i in range(0, n):
#         total = total + (x / (2 * i + 1))
#     print()
#     print(total)


# harmon(6, 4)

"""
 Ask x and n from user and then calculate the following answer.
6^1-6^3+6^5-6^7
"""


# def pattern(x, n):
#     sum = 0
#     for i in range(0, n):
#         if i % 2 == 0:
#             a = x
#         else:
#             a = -x
#         sum = sum + a ** (2 * i + 1)
#     print()
#     print(sum)


# pattern(6, 4)


"""
Create a function addDigits() that takes an integer as an argument.
Calculate the sum of digits of that number.
addDigits(123)
6
"""


def addDigits(num):
    n = num
    total = 0
    while n > 0:
        total = total + n % 10
        n = n // 10
    return total


a = addDigits(123)
print(a)
