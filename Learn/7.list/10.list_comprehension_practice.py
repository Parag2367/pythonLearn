"""
. Write a Python program to generate a list of powers of 2 less than 100
using list comprehension.

"""

# my_list = [2**i for i in range(0, 100) if 2**i < 100]
# print(my_list)


"""
Write a Python program to generate a list of factorials less than 1000
using list comprehension.

"""


# def fact(num: int):
#     fact = 1
#     for i in range(1, num + 1):
#         fact = fact * i
#     return fact


# my_list = [fact(i) for i in range(1, 100) if fact(i) < 1000]
# print(my_list)


"""
Generate a list of numbers less than 1000 which are divisible by the
sum of their digits.
"""


# def divsum(num: int) -> int:
#     n = num
#     total = 0
#     while n > 0:
#         last_digit = n % 10
#         total = total + last_digit
#         n = n // 10
#     if num % total == 0:
#         return num


# my_list = [divsum(i) for i in range(1, 1001) if divsum(i) == i]
# print(my_list)

"""
Remove duplicates from the list just by using list comprehension.
"""


# def noDup(my_list: list) -> list:
#     new_list = []
#     for a in my_list:
#         if a not in new_list:
#             new_list.append(a)
#     return new_list
lst = [22, 33, 44, 33, 55, 33, 55, 22]
my_list = []
mynodup_list = [my_list.append(a) for a in lst if a not in my_list]
print(my_list)
