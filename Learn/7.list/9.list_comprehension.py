"""
LIST COMPREHENSION : use this when we want to create a list
"""

# my_list = []

# for a in range(1, 21):
#     my_list.append(a)

# print(my_list)

"""
to achieve similar things we can use list comprehension
list comprehension is fast compared to above, as it is compact and optimized
"""

# my_list = [
#     i for i in range(1, 21)
# ]  # the first is like variable you can perform some ops on it
# print(my_list)


# my_list = [i % 2 for i in range(1, 21)]
# print(my_list)

# my_list = [i % 2 == 0 for i in range(1, 21)]
# print(my_list)

"""
Two ways of getting output
If you want to print everything with changing as per condition
"""
# my_list = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 21)]
# print(my_list)

# my_list = [1 if i % 2 == 0 else 0 for i in range(1, 11)]

"""
if you only want to print values which meets the condition
"""
# my_list = [i for i in range(1, 21) if i % 2 == 0]
# print(my_list)


# my_list = [i for i in range(10, 0, -1)]
# print(my_list)

# my_list = [i**2 if i % 2 == 0 else i**3 for i in range(1, 21)]
# print(my_list)

###################################################################

"""
Generate a list of squares of numbers from 1 to 10 using list
comprehension.

"""
# my_list = [i**2 for i in range(1, 11)]
# print(my_list)


"""
Given a list of strings, create a new list containing the lengths of
each string using list comprehension.
"""

# l1 = ["parag", "ram", "kussu", "rahul"]

# l2 = [len(a) for a in l1]
# print(l2)

"""
Generate a list of strings where each string repeats itself three times,
using list comprehension.
"""

# my_list = ["a", "b", "c"]

# new_list = [a * 3 for a in my_list]
# print(new_list)


"""
Generate a list of list using list comprehension where format should
be [[1, ”ODD”], [2, “EVEN”], [3, ”ODD”]]
"""

# my_list = [[i, "EVEN"] if i % 2 == 0 else [i, "ODD"] for i in range(1, 21)]
# print(my_list)


"""
generate two list from list
list of int
list of float
we will use second way of printing as it only want value
"""

# original_list = [10, 23, 45, 55, 66.66, 77.8, 99]
# int_list = [i for i in original_list if type(i) == int]
# float_list = [i for i in original_list if type(i) == float]

# print(int_list)
# print(float_list)


"""
Advanced
"""


# def checkDiv(num: int) -> bool:
#     if num % 2 == 0 and num % 3 == 0:
#         return True
#     else:
#         return False


# my_list = [i for i in range(1, 50) if checkDiv(i) == True]
# print(my_list)


"""
prime
"""


# def checkPrime(num: int) -> bool:
#     cnt = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             cnt = cnt + 1
#     if cnt == 2:
#         return True


# my_list = [i for i in range(1, 51) if checkPrime(i) == True]
# print(my_list)


"""
armstrong
"""


def checkArm(num: int) -> bool:
    n = num
    total = 0
    while n > 0:
        last_digit = n % 10
        total = total + (last_digit) ** 3
        n = n // 10
    return num == total


my_list = [i for i in range(1, 3000) if checkArm(i) == True]
print(my_list)

my_list1 = [i for i in range(1, 3000) if checkArm(i)]
print(my_list1)
