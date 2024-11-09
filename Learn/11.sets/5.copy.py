a = {2, 3, 4, 5, 6, 7}
b = {3, 4, 7, 9, 11}
c = {22, 33, 44, 55, 66}

print(a | b | c)

# x = a
# x.remove(3)
# print(a)
# print(x)


# print(id(a))
# print(id(x))


x = a.copy()

x.remove(4)
print(a)
print(x)


print(id(a))
print(id(x))
