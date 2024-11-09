a = {2, 3, 4, 5, 6}
b = {5, 6, 7, 9, 11}

# union : all elements without duplicates
x = a.union(b)
print(x)


# intersection : elements in both
y = a.intersection(b)
print(y)

# difference : available in a not in b
z = a.difference(b)
print(z)


# difference_update
# print(f"{a = }")
# print(f"{b = }")

# a.difference_update(b)  # it will remove the elemnts of difference from a
# print(f"{a = }")
# print(f"{b = }")


# intersection update
print(f"{a = }")
print(f"{b = }")

a.intersection_update(
    b
)  # it will update the intersection elements in a, that is a will change into intersection result
print(f"{a = }")
print(f"{b = }")
