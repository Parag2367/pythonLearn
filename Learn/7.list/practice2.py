"""
Make a list of your own. And remove all the duplicates element from
that list.
"""

# my_list = [23, 34, 56, 76, "Parag", 56.655, True, 56, 34]
# new_list = []

# for a in my_list:
#     if a not in new_list:
#         new_list.append(a)
# print(new_list)


"""
Make a list. Then ask a number from user. If number exists in that list
then print the position of the element else print -1.
"""

# num = int(input("Enter a number = "))
# my_list = [23, 34, 56, 76, 56.655, 56, 34]

# if num in my_list:
#     print(my_list.index(num))
# else:
#     print(-1)


"""
Take 10 integer inputs from user and store them in a list. Now, copy
all the elements in another list but in reverse order.

"""
# my_list = []
# for a in range(1, 11):
#     value = int(input(f"Enter {a} valu = "))
#     my_list.append(value)

# print(my_list)

# my_list.reverse()
# new_list = my_list.copy()
# print(new_list)

# result = []
# for a in range(len(my_list), -1, -1):
#     result.append(a)
# print(result)

"""
Write a program to find the average of all the numbers present in the
list
"""
# my_list = [23, 34, 56, 76, 56.655, 56, 34]
# sum = 0

# for a in my_list:
#     sum = sum + a
# print(sum / len(my_list))


"""
Write a Python code to find the occurrence of each element in a list
and print the element with the highest occurrence.

"""

# my_list = [23, 34, 56, 76, 56.655, 56, 34, 23, 34, 56, 56, 23]
# result = []  # if we directly count they will repeat again and again
# for a in my_list:  # we did this because it will create a unique list
#     if a not in result:
#         result.append(a)

# highest_occ = 0
# highest_occ_element = 0

# for a in result:
#     c = my_list.count(
#         a
#     )  # counting the elements of unique list in original list(they will only give one value)
#     if c > highest_occ:
#         highest_occ = c
#         highest_occ_element = a

# print(
#     f"{highest_occ_element} is the highest occurence element which occured for {highest_occ} times"
# )

"""
Write a program that has two lists and make a new list that contains
only the common elements between them without duplicates.
"""
# l1 = [2, 3, 4, 5, 6, 6, 6]
# l2 = [5, 6, 7, 8, 9]

# new_list = []

# for a in l1:
#     if a in l2:
#         if a not in new_list:  # this is to avoid duplicate
#             new_list.append(a)
# print(new_list)


"""
. Write a Python code to find the second largest element in a list
without sorting.
"""


# my_list = [23, 34, 56, 76, 56.655, 56, 34]

# largest = my_list[0]

# for a in my_list:
#     if a > largest:
#         largest = a

# my_list.remove(largest)

# second_largest = my_list[0]
# for b in my_list:
#     if b > second_largest:
#         second_largest = b
# print(second_largest)

############################################
# optimized solution:

# largest = float("-inf")
# second_largest = float(
#     "-inf"
# )  # value in list can be zero that is why we have taken -inf

# for a in my_list:
#     if a > largest:
#         second_largest = largest
#         largest = a
#     elif a > second_largest and a < largest:
#         second_largest = a

# print(second_largest)


"""
Make a program that takes a list of integers and returns the product
of all the elements.
"""

# my_list = [23, 34, 56, 76, 56.655, 56, 34]

# product = 1

# for a in my_list:
#     product = product * a
# print("Product of all numbers are", product)


"""
Write a program to find and print all prime numbers within a given
list.
"""

# my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# for a in my_list:
#     factors = 0
#     for i in range(1, a + 1):
#         if a % i == 0:
#             factors += 1
#     if factors == 2:
#         print(a, end=" ")


"""
Write a program that swaps the first and last elements of a given list
"""
# my_list = [23, 34, 56, 76, 56.655, 56, 34, "Parag"]

# my_list[0] = my_list[0] + my_list[-1]
# my_list[-1] = my_list[0] - my_list[-1]
# my_list[0] = my_list[0] - my_list[-1]

# print(my_list)

# another approach
# new_list = my_list.copy()

# new_list[0] = my_list.pop(-1)
# new_list[-1] = my_list.pop(0)
# print(new_list)


"""
split the list into two halves
"""

# my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# l1 = []
# l2 = []
# if len(my_list) % 2 == 0:
#     for i in range(
#         0, (len(my_list) // 2) + 1
#     ):  # used // because it will always give integer
#         l1.append(my_list[i])
#     for i in range((len(my_list) // 2) + 1, len(my_list)):
#         l2.append(my_list[i])

# else:
#     for i in range(0, ((len(my_list) + 1) // 2)):
#         l1.append(my_list[i])
#     for i in range(((len(my_list) + 1) // 2), len(my_list)):
#         l2.append(my_list[i])

# print(l1)
# print(l2)


#########################

# my_list = [1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 7]
# new_list = []

# for a in my_list:
#     if a not in new_list:
#         new_list.append(a)
#     else:
#         continue
# print(new_list)


"""
Write a Python function that takes two lists and returns True if they
have at least one common element.

"""


# def common(lst1, lst2):
#     for a in lst1:
#         if a in lst2:
#             return True


# lst1 = [23, 34, 45, 56, 76]
# lst2 = [34, 45, 56]

# common(lst1, lst2)


"""
Write a program to put all the common elements (in 2 lists) in another
list and print it using function
"""


# def common2(lst1, lst2):
#     lst3 = []
#     for a in lst1:
#         if a in lst2:
#             lst3.append(a)
#         else:
#             continue
#     print(lst3)


# lst1 = [23, 34, 45, 56, 76]
# lst2 = [34, 45, 56, 44, 55, 66, 78, 76]
# common2(lst1, lst2)


"""
Write a program to remove the nth index element from a list using a
function.
"""


# def remN(lst: list, num: int) -> list | str:
#     if num in range(0, len(lst)):
#         lst.pop(num)
#     else:
#         return "Index is not in range"
#     return lst


# lst = [34, 45, 56, 44, 55, 66, 78, 76]
# num = 10

# print(remN(lst, num))


"""
Write a python program which prints all the values whose count is
greater than 3. (Make sure to make a list with at least 15 numbers)
"""


# def countN(lst: list):
#     lst1 = []
#     for a in lst:
#         if a not in lst1:
#             lst1.append(a)

#     for i in lst1:
#         if lst.count(i) > 3:
#             print(i, end=" ")


# lst = [
#     34,
#     45,
#     56,
#     44,
#     55,
#     66,
#     78,
#     76,
#     45,
#     45,
#     45,
#     44,
#     44,
#     44,
#     34,
#     34,
# ]

# countN(lst)


"""
Make a list. Write a simple program for addition of the 2nd element
from start and 2nd element from the end.
"""


def addition(lst: list):
    if len(lst) > 3:
        add = lst[1] + lst[-2]
        print(add)
    elif len(lst) == 3:
        print("Both elements are same")
    else:
        print("not enough numbers")
    # return add


addition([23, 34, 43, 45, 56])
# (addition([23, 34, 54]))
# (addition([12, 23]))
