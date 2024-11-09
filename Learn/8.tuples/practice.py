"""
Write a Python program to get the 4th element from the last element
of a tuple.
"""

# def fourth(tup: tuple):
#     if len(tup) >= 4:
#         a = tup[-4]
#         print(a)


# tup = (2, 3, 4, 5, 6, 7)
# fourth(tup)

"""
Write a Python program to find repeated items in a tuple.
"""


# def repeat(tups: tuple):
#     cnt = 0
#     mylist = []
#     for a in tups:
#         if tups.count(a) > 1:
#             if a not in mylist:
#                 mylist.append(a)
#     print(tuple(mylist))


# tups = (1, 2, 3, 2, 1, 4, 3, 5)
# # repeat(tups)


# # another way:
# def repeat(tups: tuple):
#     repeated = []
#     for i in range(0, len(tups)):
#         if tups[i] in tups[i + 1 :] and tups[i] not in repeated:
#             repeated.append(tups[i])
#     return repeated


# rep = repeat(tups)

# if len(rep) > 0:
#     print(f"{rep = }")
# else:
#     print("Not Repeated")

"""
Write a Python program to check whether an element exists within a
tuple. Ask something from user, if that exists in tuple, then print “YES” else
print “NO”
"""


# def exists(tups: tuple, ch):
#     a = tups.index(ch)
#     if a in range(0, len(tups)):
#         return "Yes"
#     return "No"


# tups = (1, 2, 3, 4, "Parag")
# print(exists(tups, "Para"))

"""
. Write a Python program to reverse a tuple.
"""

# mytups = (1, 2, 4, 3, 2)
# tup = mytups[::-1]
# print(tup)

# # also

# for i in range(-1, -(len(mytups) + 1), -1):
#     print(mytups[i], end=",")
