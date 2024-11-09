"""Slicing"""

a = [23, 34, 44, 56, 76, 87, 98, 12]
# # b = a[::-1]
# # b = a[-4:-1]
# # b = a[-4:-1:-1]
# # b = a[::5]
# b = a[1:5:7]
# b = a[-1:-5:-1]
# print(b)

# Note

my_list = [10, 20, 22, 33, "abcd", 44, 55, 66]
# my_list[0:3] = 100  # this is not allowed
# my_list[0:3] = [
#     100
# ]  # this is allowed , because if you want to assign something to slicing it should be a iterable(list,string,tuples)
# my_list[4:6] = 'abcd' # this is allowed

# # my_list[4][1:3] = "xyz"
# 'abc' = 'def'# not allowed as string operator does not support assingment


"""
Write a python program to reverse a list using slicing
"""

# a = [23, 34, 44, 56, 76, 87, 98, 12]
# # b = a[::-1]
# # b = a[-4:-1]
# # b = a[-4:-1:-1]
# # b = a[::5]
# # b = a[1:5:7]
# b = a[-1:-5:-1]
# print(b)


"""
. Write a python program to get every third element from a list using
slicing.
"""

# a = [23, 34, 44, 56, 76, 87, 98, 12]

# b = a[::3]
# print(b)


"""
 Implement a python program to split a list into two equal parts using
slicing. One list should contain 1st half and another list should contain 2nd
half.

"""
# a = [23, 34, 44, 56, 76, 87, 98, 12]

# b = a[: (len(a) // 2)]
# c = a[len(a) // 2 :]

# print(b)
# print(c)


"""
Implement a python program to get the last 'n' elements from a list
using slicing.
"""
# num = int(input("Enter a number = "))
# a = [23, 34, 44, 56, 76, 87, 98, 12]

# if num > len(a) or num < 0:
#     print("Error: Out of index")
# else:
#     b = a[num : len(a) + 1]
#     print(b)


"""
Ask n from user. Create a list of last n elements but in reverse order
using slicing.

"""
# num = int(input("Enter a number = "))
# a = [23, 34, 44, 56, 76, 87, 98, 12]

# if num > len(a) or num < 0:
#     print("Error: Out of index")
# else:
#     b = a[len(a) : num - 1 : -1]
#     print(b)


"""
Ask n from user. Create a list of first n elements but in reverse order
using slicing.
"""
# num = int(input("Enter a number = "))
# a = [23, 34, 44, 56, 76, 87, 98, 12]

# if num > len(a) or num < 0:
#     print("Error: Out of index")
# else:
#     b = a[num::-1]
#     print(b)
