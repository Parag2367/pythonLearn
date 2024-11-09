my_string = "Python is good"

# a = int(my_string)
# print(a, type(a))

b = list(my_string)
b[0] = "ZZ"

c = "".join(b)
print(c, type(c))
