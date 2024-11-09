"""ITERATION"""

# x = (2, 3, 4, 5, 6, 7)

# # BY VALUE
# for a in x:
#     print(a, end=" ")

# # BY INDEX
# for i in range(0, len(x)):
#     print(i, end=" ")


# # By both

# for index, value in enumerate(x):
#     print(index, value)


"""CONVERSION"""

# y = (2, 3, 5, 4, 7, 9)

# a = list(y)
# a.append(200)
# a.append(100)

# y = tuple(a)
# print(y)


"""UNPACKING"""


x = (10, 20, 30, 50)
print(type(x))

y = 10, 20, 30, 44  # also Tuple , by default it is tuple
print(type(y))


z = (100,)


a, b, c = (12, 20, 30)
