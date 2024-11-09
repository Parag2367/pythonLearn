"""
Ask a string from user. Display the dictionary where each key is a
character and value is the frequency of that character that comes in that
string.
"""

# a = input("Enter a string = ")
# my_dict = {}
# for i in a:
#     keys = i
#     value = a.count(i)
#     my_dict.update({keys: value})

# print(my_dict)

# another approach

# for ch in a:
#     if ch in my_dict:
#         my_dict[ch] += 1
#     else:
#         my_dict[ch] = 1

# print(my_dict)


"""
Store “name” of a student as Key,
“list of 5 marks” of that student as
a Value. Store atleast 5 student names. Print the sum and percentage of all
the students.
"""

# my_dict = {}

# for i in range(1, 6):
#     my_list = []
#     name = input("Enter student name = ")
#     for j in range(1, 6):
#         marks = int(input(f"Enter marks of subject {j}"))
#         my_list.append(marks)
#     my_dict.update({name: my_list})
# print(my_dict)


# for a in my_dict.keys():
#     total = 0
#     total = sum(my_dict[a])
#     print(f"total marks for {a} is {total}")


# another way

# for name, marks in my_dict.items():
#     total = sum(marks)
#     percentage = (total / 500) * 100
#     print(f"total marks for {name} is {total} and percentage = {percentage:2f}")


# finding topper

# largest = 0
# topper = ""

# for name, marks in my_dict.items():
#     total = sum(marks)
#     if total > largest:
#         largest = total
#         topper = name

# print(f"{topper} is topper with marks {largest}")


"""
Write a Python program to combine two dictionary by adding values
for common keys.
"""

# d1 = {"a": 200, "b": 300, "c": 400}
# d2 = {"a": 100, "e": 300, "c": 300}

# result = {}

# for k, v in d1.items():
#     result[k] = v

# for k, v in d2.items():
#     if k in result:
#         result[k] = result[k] + v
#     else:
#         result[k] = v
# print(result)


"""
Write a Python function that takes a dictionary as input where the
values are lists. The function should return a new list containing all the
elements from all the lists in the dictionary.

"""


# def newList(mydict: dict) -> list:
#     mylist = []
#     for a in mydict.values():
#         for i in range(len(a)):
#             mylist.append(a[i])
#     return mylist


# details = {"parag": [23, 34, 156], "ravi": [29, 44, 60], "raju": [20, 44, 70]}

# print(newList(details))

"""
Create a function named countChar which will accept a string as a
parameter. Create a dictionary having frequency of each character.

"""


# def countChar(mystr: str) -> dict:
#     mydict = {}
#     for ch in mystr:
#         if ch in mydict:
#             mydict[ch] += 1
#         else:
#             mydict[ch] = 1

#     return mydict


# mystr = "hello"
# print(countChar(mystr))


"""
Write a Python function that takes a dictionary as input where the
values are lists of integers. The function should return a new dictionary
where the values are lists containing only the even integers from the
original lists.
"""


# def newDict(mydict: dict) -> dict:
#     newDict = {}
#     for k, v in mydict.items():
#         mylist = []
#         for a in v:
#             if a % 2 == 0:
#                 mylist.append(a)
#         newDict[k] = mylist

#     return newDict


# mydict = {"a": [2, 4, 3], "b": [3, 6, 8], "c": [11, 12, 24]}
# print(newDict(mydict))


"""
Write a Python function that takes two dictionaries as input, where the
values are lists. The function should merge the lists corresponding to the
same keys in both dictionaries into a single list and return a new dictionary
with these merged lists.
"""


# def mergeDict(dict1: dict, dict2: dict) -> dict:
#     mydict = {}
#     for k, v in dict1.items():
#         for a, b in dict2.items():
#             if k == a:
#                 mydict[k] = v + b

#     return mydict


# dict1 = {"a": [2, 4, 3], "b": [3, 6, 8], "c": [11, 12, 24]}
# dict2 = {"a": [5, 6, 3], "d": [3, 6, 8], "c": [13, 15, 24]}

# print(mergeDict(dict1, dict2))


"""
access fifth element from the list
"""
# mydict = {
#     "x": [11, 12, 13, 14, 15, 16, 17, 18, 19],
#     "y": [21, 22, 23, 24, 25, 26, 27, 28, 29],
#     "z": [31, 32, 33, 34, 35, 36, 37, 38, 39],
# }


# for k, v in mydict.items():
#     print(v[4])


"""
Given a dictionary with key-value pairs, remove all the keys with values
greater than K, including mixed values
"""

mydict = {"Gfg": 3, "is": 7, "best": 10, "for": 6, "xyzx": "CS"}
# a = 7
# new = {}
# keysTo_delete = []
# for k, v in mydict.items():
#     if type(v) == int and v < a:
#         new[k] = v
#     elif type(v) != int:
#         new[k] = v
# print(new)


# another approach
# def keyRemove(mydict: dict, num: int) -> dict:
#     dictt = mydict.copy()
#     keysTo_delete = []

#     for k, v in dictt.items():
#         if type(v) == int and v >= num:
#             keysTo_delete.append(k)

#     for k in keysTo_delete:
#         dictt.pop(k)

#     return dictt


# print(keyRemove(mydict, 7))


"""
A Python dictionary contains List as a value. Write a Python program to
clear the list values in the said dictionary.
"""
# myd = {"C1": [10, 20, 30], "C2": [20, 30, 40], "C3": [12, 34], "C4": 34}
# new = {}

# for k, v in myd.items():
#     if type(v) == list:
#         new[k] = []
#     else:
#         new[k] = v
# print(new)
