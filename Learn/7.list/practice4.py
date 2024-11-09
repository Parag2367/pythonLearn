# Write a Python code to check if a given list is sorted in ascending order.

# my_list = [3, 4, 5, 6, 1]

# for i in range(1, len(my_list)):
#     if my_list[i - 1] > my_list[i]:
#         print("NO")
#         break
#     else:
#         continue
# print("YES")


# Write a python program to check if the list contains three consecutive
# common numbers in Python.

# my_list = [4, 5, 5, 3, 8]

# for i in range(2, len(my_list)):
#     if my_list[i - 2] == my_list[i - 1] and my_list[i - 1] == my_list[i]:
#         print("consecutive number is ", my_list[i])
#     else:
#         continue

# Write a Python code to check if a list is a palindrome

# my_list = [1, 2, 3, 3, 2, 1, 3]

# if my_list == my_list[::-1]:
#     print("Palindrome")
# else:
#     print("not palindrome")


# Given two sorted lists, write a Python code to merge them into a single sorted list.


# def mergelist(a: list, b: list) -> None:
#     my_list = []
#     if len(a) < len(b):
#         for x in b:
#             for y in a:
#                 if y < x:
#                     my_list.append(y)
#             else:
#                 my_list.append(x)

#     else:
#         for x in a:
#             for y in b:
#                 if y < x:
#                     my_list.append(y)
#             else:
#                 my_list.append(x)

#     print(list(set(my_list)))


# a = [1, 4, 5, 6, 7, 8, 9, 10]
# b = [1, 2, 4, 5, 6, 7, 8]

# mergelist(a, b)


# Write a Python code to find the occurrence of each element in a list
# and print the element with the highest occurrence.


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
