"""
. Write a Python code to check if a given list is sorted in ascending order.
"""

# def sorted(mylist: list) -> bool:
#     for i in range(1, len(mylist)):
#         if mylist[i - 1] > mylist[i]:
#             return False
#     return True


# mylist = [1, 1, 1, 1, 2, 3, 4, 1, 2]
# print(sorted(mylist))

"""
Given two sorted lists, write a Python code to merge them into a single sorted list.
"""

# a = [1, 4, 6, 7, 8, 12, 14, 22]
# b = [34, 56, 78, 99, 100]
# result = []

# i = 0
# j = 0
# while i < len(a) and j < len(b):  # it will run untill anyone of i or j exhausts
#     if a[i] < b[j]:
#         result.append(a[i])
#         i = i + 1
#     elif b[j] < a[i]:
#         result.append(b[j])
#         j = j + 1
#     else:3 for same number
#         result.append(a[i])
#         result.append(b[j])
#         i = i + 1
#         j = j + 1

# while i < len(a): # it will run if j exhausts first
#     result.append(a[i])
#     i = i + 1

# while j < len(b): # it will run if i exhausts first
#     result.append(b[j])
#     j = j + 1

# print(result)


"""
Write a python program to check if the list contains three consecutive common numbers in Python.
"""
# mylist = [1, 2, 3, 4, 55, 55, 55, 6, 7, 7, 7]
# for i in range(0, len(mylist) - 2):
#     if mylist[i] == mylist[i + 1] == mylist[i + 2]:
#         print(mylist[i])


"""Write a Python code to find the occurrence of each element in a list
# and print the element with the highest occurrence.
"""


# my_list = [44, 11, 11, 11, 23, 235, 546, 44, 55, 77, 77, 77, 77]
# new_list = []

# for a in my_list:
#     if a not in new_list:
#         new_list.append(a)

# occur = 0
# number = 0
# for a in new_list:
#     cnt = my_list.count(a)
#     print(f"{a} occured {cnt} times")
#     if cnt > occur:
#         occur = cnt
#         number = a
# print(f"highest occurence is : {number} occured {occur} times")


"""
second largest number
"""


# def second_largest(mylist: list) -> int | float | str:
#     largest = float("-inf")
#     second_largest = float("-inf")
#     if len(mylist) < 2:
#         print("Not enough numbers")
#     for a in mylist:
#         if a > largest:
#             second_largest = largest
#             largest = a
#         elif a > second_largest and a != largest:
#             second_largest = a

#     if second_largest == float("-inf"):
#         return "There is no second largest number"
#     else:
#         return second_largest


# mylist = [12, 74, -89, 96, -98, -96, 52]
# result = second_largest(mylist)
# print(f"Second largest element = {result}")

"""
Write a Python code to find the difference between two lists (i.e.,
elements present in the first list but not in the second).

"""
lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]
new_list = []
for a in lst1:
    if a not in lst2:
        print(a, end=" ")
