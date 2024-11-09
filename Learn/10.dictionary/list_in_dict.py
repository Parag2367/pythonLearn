"""
list in dict
"""

details = {"parag": [23, 34, 156], "ravi": [29, 44, 60], "raju": [20, 44, 70]}

# for k, v in details.items():
#     total = 0
#     for a in v:
#         total = total + a
#     print(f"{k} marks = {total}")

# high = 0
# highest_student = ""
# for k, v in details.items():
#     if sum(v) > high:
#         high = sum(v)
#         highest_student = k

# print(f"{highest_student} hs scored {high}")


"""
max marks in a subject
"""

# student = ""

# for k, v in details.items():
#     high = 0
#     for i in v:
#         if i > high:
#             high = i
#             student = k
#     print(f"{student} has scored {high}")


##################

details["parag"].append(100)

print(details)


#########################

"""
enter name and number and create a dict and list of marks
"""


# def createDic(num: int) -> dict:
#     mydict = {}
#     for i in range(0, num):
#         student = input("enter student name = ")
#         mylist = []
#         for j in range(1, 4):
#             marks = int(input(f"enter marks {j} = "))
#             mylist.append(marks)
#         mydict[student] = mylist
#     return mydict


# print(createDic(3))
