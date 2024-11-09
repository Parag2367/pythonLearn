"""
Ask subject name and marks from the user and keep adding it to
dictionary
"""

# number = int(input("Enter number of subjects = "))
# my_dict = {}

# # for i in range(1, number + 1):
# #     subject = input("Enter name of subject = ")
# #     marks = int(input(f"Enter {subject} marks = "))
# #     my_dict.update({subject: marks})

# # print(my_dict)

# # alternative way

# for _ in range(1, number + 1):  # used _ because we dont need i anywhere in loop
#     subject = input("Enter name of subject = ")
#     marks = int(input(f"Enter {subject} marks = "))
#     my_dict.update({subject: marks})
#     # my_dict[subject] = marks   # another way


"""
Convert two lists into a dictionary. Make two list on your own of
same length, and convert them to dictionary.
"""

# l1 = ["Ten", "Twenty", "Thirty"]
# l2 = [10, 20, 30]

# my_dict = {}

# for i in range(0, len(l1)):
#     my_dict[l1[i]] = l2[i]

# print(my_dict)


"""
Write a Python program to sum all the items in a dictionary.
"""

# my_dict = {"maths": 55, "english": 45, "hindi": 50}
# total = 0
# for k, v in my_dict.items():
#     total = total + v

# print("Sum of all subjects are = ", total)

# # another way
# print(sum(list(my_dict.values())))


"""
Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the highest marks scored.

"""

mydict = {
    "pysics": 54,
    "maths": 70,
    "english": 60,
    "hindi": 65,
    "sanskrit": 65,
    "pe": 20,
}


# highest = 0
# for a in mydict.values():
#     if a > highest:
#         highest = a
# print(f"{highest = }")

"""
Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the name of the subject with highest marks
scored.

"""
# high = 0
# for k in mydict.keys():
#     if mydict[k] > high:
#         high = mydict[k]
#         subject = k

# print(f"subject {subject} has highest {high}")

"""
Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the name of the subject which has marks
more than passing marks (above 33).
"""

# for k in mydict.keys():
#     if mydict[k] > 33:
#         print(f"subject which has marks more than passing are {k}")


"""
 Write a Python program to generate and print a dictionary that
contains a number (between 1 and n) in the form (x, x*x).
"""


# def mydict(num: int) -> dict:
#     myd = {}
#     for i in range(1, num + 1):
#         myd[i] = i * i
#     return myd


# print(mydict(5))


"""
Python program to find the size of a Dictionary. Basically print how
many total key-value pair are there.

"""
# count = 0
# for k in mydict.keys():
#     count = count + 1

# print(count)

# another method

# def countKeys(dictionary: Dict) -> int:
#     return len(dictionary.keys())


"""
check for empty dict
"""
from typing import Dict


def isEmpty(dictionary: Dict) -> bool:
    # Method 1 (Best way)
    if not dictionary:
        return True
    return False


print(isEmpty(mydict))
