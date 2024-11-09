"""
Calculate the cube of all numbers from 1 to a given number.

"""

# def cube(num):
#     for a in range(1, num + 1):
#         a = a**3
#         print(a, end=" ")


# cube(8)


"""
Write a function named notPrimeNumbers which accepts 2 integers n1
and n2. Print all the numbers from n1 to n2 which are not prime.
"""


# def notPrimeNumbers(n1, n2):
#     for a in range(n1, n2 + 1):
#         cnt = 0
#         for i in range(1, a + 1):
#             if a % i == 0:
#                 cnt = cnt + 1
#         if cnt == 2:
#             continue
#         else:
#             print(a, end=" ")


# notPrimeNumbers(3, 10)
# print()
# notPrimeNumbers(5, 20)


"""
Write a function named armstrongRange which accepts 2 integers n1
and n2. Print all the numbers from n1 to n2 which are armstrong numbers.

"""


def armstrong(num: int):
    a = num
    total = 0
    while a > 0:
        total = total + (a % 10) ** 3
        a = a // 10
    if total == num:
        print(num, end=" ")


def armstrongRange(n1: int, n2: int):
    for a in range(n1, n2 + 1):
        armstrong(a)


armstrongRange(56, 1000)
