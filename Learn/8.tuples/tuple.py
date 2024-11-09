"""
tuples are immutable
"""

my_tuple = (34, 67, 87, [45, 56, 12], "Prag", True)

new_tuple = (34, 44, 55, 66, 76, 88.99)
print(sum(new_tuple))
print(len(new_tuple))
print(min(new_tuple))
print(max(new_tuple))


"""
two methods available
"""

"""1. count """

# c = my_tuple.count(56)
# print(c)

"""2 index"""

# d = my_tuple.index(67)
# print(d)

# e = my_tuple.index([45, 56, 12])
# print(e)


"""tuple unpacking: """

# a, b, c, d, e, f = my_tuple
# print(d)


# we can convert tuples to list and vice versa

my_list = list(my_tuple)
print(my_list)

# my_list.append(45)  # no error
# print(my_list)

my_tuple = tuple(my_list)  # overwrite is happening here
print(my_tuple)
