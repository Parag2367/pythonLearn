"""
Make a function named sumPattern that takes an integer n as an
argument from the user. And then calculate the sum of the following
pattern.
1/1! + 1/2! + 1/3! +....
"""

# def sumPattern(n: int) -> float:
#     total = 0
#     fac = 1
#     for i in range(1, n + 1):
#         fac = fac * i
#         total = total + (1 / fac)
#     return total


# print(sumPattern(5))


"""
Create a function named as checkPrime that takes an integer as an
argument. Print YES if the number passed is a prime number else print NO.
"""


# def checkPrime(n):
#     cnt = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             cnt = cnt + 1
#     if cnt == 2:
#         print("Yes")
#     else:
#         print("No")


# checkPrime(7)

"""
Create a function named as printPrimeFactors that takes an integer n
as a argument and print all the prime factors of that number.
"""


# def checkPrime(n) -> bool:
#     cnt = 0
#     i = 1
#     while i <= n:
#         if n % i == 0:
#             cnt = cnt + 1
#         i = i + 1
#     if cnt == 2:
#         return True
#     else:
#         return False


# def printPrimeFactors(num):
#     i = 1
#     while i <= num:
#         if num % i == 0:
#             if checkPrime(i):
#                 print(i, end=" ")
#         i = i + 1
#     print()


# printPrimeFactors(20)


"""
n1,n2 print prime between n1 and n2
"""


def primeBetween(n1, n2):
    for i in range(n1, n2 + 1):
        cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:
                cnt = cnt + 1
        if cnt == 2:
            print(i, end=" ")
    print()


primeBetween(2, 10)
primeBetween(50, 60)
