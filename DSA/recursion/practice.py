"""
Write a Python program to get the sum of a non-negative integer using recursion.
sum(345) = 12
"""

# def sumint(num, sum):
#     if num // 10 == 0:
#         return sum + num
#     return sumint(num // 10, sum + (num % 10))


# print(sumint(3456, 0))


# # better as less operations
# def sumin(num):
#     if num == 0:
#         return 0
#     return num % 10 + sumin(num // 10)


# print(sumin(3456))


"""
Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0) using recursion .
Test Data:
sum_series(6) -> 12
sum_series(10) -> 30
"""


# def sumseries(num, a):
#     if a == 0:
#         return 0
#     return a + sumseries(num, a - 2)


# print(sumseries(10, 10))


# # alternative way
# def sumseriesa(num):
#     if num == 0:
#         return 0
#     return num + sumseriesa(num - 2)


"""

Write a Python program to calculate the sum of harmonic series upto n terms.
Note: The harmonic sum is the sum of reciprocals of the positive integers.
Example :
harmonic series
"""


# def harmonic(num):
#     if num == 1:
#         return 1
#     return 1 / num + harmonic(num - 1)


# print(harmonic(4))


"""
Write a Python program to find the greatest common divisor (GCD) of two integers using recursion.
"""
# Define a function named Recurgcd that calculates the greatest common divisor (GCD)
# of two numbers 'a' and 'b' using recursion and the Euclidean algorithm


def gcd(num1, num2):
    low = min(num1, num2)
    high = max(num1, num2)

    if (
        low == 0
    ):  # this case is when they are totally divisible/one number is factor of other(14,7) or a have a common factor:3(6,9)
        return high
    if low == 1:  # this case is when they are not at all divisible(14,11) prime
        return 1
    return gcd(low, high % low)


print(gcd(15, 12))
