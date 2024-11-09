"""
Given a list and dictionary, map each element of list with each item
of dictionary, forming nested dictionary as value
"""

# test_dict = {"parag": 56, "coder": 45, "worker": 55}
# test_list = [23, 34, 45]
# new_dict = {}

# for a in test_list:
#     for k, v in test_dict.items():
#         new_dict[a] = {k: v}
# print(new_dict)


"""
solve questions
"""

# student = {
#     "John": {"Marks": [80, 85, 90]},
#     "Alice": {"Marks": [75, 88, 92]},
#     "Bob": {"Marks": [90, 92, 88]},
# }
# student["Eva"] = {"Marks": [95, 91, 89]}

# print(student)


"""
Write a python program that prints all the students name along with
their average marks.
"""

# for name, details in student.items():
#     num = len(student[name]["Marks"])
#     total = sum(student[name]["Marks"])
#     average = total / num

#     print(f"{name} : {average}")


"""
"""
# student["John"]["Marks"] = [85, 88, 92]
# print(student)


"""
Write a program that displays the name of the student that has
scored highest marks overall.
"""

# highest = 0
# for name, details in student.items():
#     total = sum(student[name]["Marks"])
#     if total > highest:
#         highest = total

# print(f"{name} has scored highest marks : {highest}")


"""
Remove John
"""

# student.pop("John")
# print(student)


"""
Write a Python script to sort (ascending and descending) a dictionary
by value.

"""

# dictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# sorted_dict = dict(
#     sorted(dictionary.items(), key=lambda x: x[1])
# )  # it will give alist, but when we used dict will convert it to dict

# print(sorted_dict)

"""
Write a Python program to count number of items in a dictionary value
that is a list.
"""

# Dict = {"M1": [67, 79, 90, 73, 36], "M2": [89, 67, 84], "M3": [82, 57]}

# count = 0
# for k, v in Dict.items():
#     for i in v:
#         count += 1

# print(count)


"""
Write a Python program to print a dictionary line by line.
"""

# Dict = {"Sam": {"M1": 89, "M2": 56, "M3": 89}, "Suresh": {"M1": 49, "M2": 96, "M3": 89}}

# for k, v in Dict.items():
#     print(k)
#     for a, b in v.items():
#         print(f"{a} : {b} ")


"""
Write a Python program to Convert two lists into a dictionary
"""

# keys = ["One", "Two", "Three", "Four", "Five"]
# values = [1, 2, 3, 4, 5]

# mydict = {}

# for i in range(len(keys)):
#     mydict[keys[i]] = values[i]

# print(mydict)


"""
Write a Python program to find the maximum and minimum value in a
dictionary.

"""


# def maxValue(mydict: dict) -> int | float:  # type: ignore
#     max = float("-inf")
#     key = ""
#     for k, v in mydict.items():
#         if v > max:
#             max = v
#             key = k
#     return max


# mydict = {"b": 2, "a": 1, "c": 3}
# print(maxValue(mydict))


"""
Create a Python program to find the difference between two
dictionaries.

"""

# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 2, "c": 4, "d": 5}
# only_dict1 = []
# only_dict2 = []
# dict1_dict2 = []

# for k in dict1.keys():
#     if k not in dict2.keys():
#         only_dict1.append(k)

#     elif k in dict2.keys():
#         dict1_dict2.append(k)
#         dict2.pop(k)

# for k in dict2.keys():
#     only_dict2.append(k)

# print(f"keys present only in dict2 {only_dict2}")
# print(f"keys present only in dict1 {only_dict1}")
# print(f"keys present only in dict2 {dict1_dict2}")


# # another approach
# def findDifference(dictionary1, dictionary2) -> None:
#     present_in_dict1 = []
#     present_in_both = []
#     for k in dictionary1:
#         if k not in dictionary2:
#             present_in_dict1.append(k)
#         else:
#             present_in_both.append(k)

#     present_in_dict2 = []
#     for k in dictionary2:
#         if k not in dictionary1:
#             present_in_dict2.append(k)

#     print(f"Keys present only in the first dictionary: {present_in_dict1}")
#     print(f"Keys present only in the second dictionary: {present_in_dict2}")
#     print(f"Keys present in both dictionaries: {present_in_both}")


"""
Create a Python function to reverse a dictionary (swap keys and
values). Make sure the values are different
"""


# def revDic(mydict: dict) -> dict:
#     dictt = mydict.copy()
#     new_dict = {}
#     for k, v in dictt.items():
#         new_dict[v] = k
#     return new_dict


# mydict = {"a": 1, "b": 2, "c": 3}
# print(revDic(mydict))


"""
Write a Python program to sort a dictionary by its keys in ascending
order.

"""

# mydict = {"b": 2, "a": 1, "c": 3}
# sorted_key = dict(sorted(mydict.items(), key=lambda x: x[0]))

# print(sorted_key)


# mydict1 = {"apple": 2, "banana": 3, "pear": 4, "orange": 5}
# sorted_key = dict(sorted(mydict1.items(), key=lambda x: len(x[0])))

# print(sorted_key)


"""
Display the name of student and total marks in ascending order.
"""

# student_data = {
#     "Alice": [85, 90, 88, 92, 89],
#     "Bob": [78, 82, 79, 81, 80],
#     "Charlie": [92, 95, 88, 85, 91],
#     "Diana": [76, 80, 79, 82, 85],
#     "Eva": [88, 92, 85, 90, 87],
#     "Frank": [83, 85, 80, 86, 88],
#     "Gina": [90, 87, 92, 88, 86],
# }


# # for k, v in student_data.items():
# #     print(f"{k} has scored ", sum(v))


# result = dict(sorted(student_data.items(), key=lambda x: sum(x[1])))
# print(result)

# for k, v in result.items():
#     print(f"{k} has scored {sum(v)}")


"""
Genrate outcome of data
Liam has scored 402
"""

# student_data = {
#     "Ella": {"age": 20, "marks": [85, 78, 92, 89, 91]},
#     "Max": {"age": 22, "marks": [79, 85, 88, 90, 87]},
#     "Sophia": {"age": 21, "marks": [92, 95, 88, 85, 91]},
#     "Liam": {"age": 23, "marks": [76, 80, 79, 82, 85]},
#     "Ava": {"age": 20, "marks": [88, 92, 85, 90, 87]},
#     "Noah": {"age": 22, "marks": [83, 85, 80, 86, 88]},
#     "Emma": {"age": 21, "marks": [90, 87, 92, 88, 86]},
# }

# result = dict(sorted(student_data.items(), key=lambda x: sum(x[1]["marks"])))
# # print(result)

# for k, v in result.items():
#     total = sum(v["marks"])
#     print(f"{k} has scored {total}")


"""
Sort this list according to total marks and print it.

"""

# student_data = [
#     ["Samantha", 18, "New York", 420],
#     ["David", 25, "Los Angeles", 380],
#     ["Sophie", 22, "Chicago", 390],
#     ["Michael", 20, "Houston", 410],
#     ["Liam", 19, "Phoenix", 430],
#     ["Olivia", 21, "Philadelphia", 400],
#     ["Daniel", 23, "San Antonio", 375],
# ]

# result = sorted(student_data, key=lambda x: x[3])
# print(result)


"""
Heres a student data, Sort this data via total marks and print it
"""
student_data = [
    {"Sophia": {"age": 21, "marks": [92, 95, 88, 85, 91]}},
    {"Max": {"age": 22, "marks": [79, 85, 88, 90, 87]}},
    {"Liam": {"age": 23, "marks": [76, 80, 79, 82, 85]}},
    {"Ava": {"age": 20, "marks": [88, 92, 85, 90, 87]}},
    {"Noah": {"age": 22, "marks": [83, 85, 80, 86, 88]}},
    {"Emma": {"age": 21, "marks": [90, 87, 92, 88, 86]}},
    {"Olivia": {"age": 24, "marks": [82, 86, 90, 87, 84]}},
]

# mydict = {}

# for a in student_data:
#     mydict.update(a)

# # print(mydict)

# result = dict(sorted(mydict.items(), key=lambda x: sum(x[1]["marks"])))

# for k, v in result.items():
#     total = sum(v["marks"])
#     print(f"{k} has scored {total}")

sorted_student_data = sorted(
    student_data, key=lambda x: sum(x[list(x.keys())[0]]["marks"])
)
print(sorted_student_data)


"""
Heres a student data. The first 3 elements are marks of student. Sort
this list and print it.
"""

# student_data = [
#     [78, 92, 85, "Alice"],
#     [82, 79, 81, "Bob"],
#     [92, 88, 85, "Charlie"],
#     [80, 79, 82, "Diana"],
#     [92, 85, 90, "Eva"],
#     [85, 80, 86, "Frank"],
#     [87, 92, 88, "Gina"],
# ]


# result = sorted(student_data, key=lambda x: (x[0] + x[1] + x[2]))
# # print(result)

# for details in result:
#     total = details[0] + details[1] + details[2]
#     name = details[3]
#     print(f"{name} has scored {total}")
