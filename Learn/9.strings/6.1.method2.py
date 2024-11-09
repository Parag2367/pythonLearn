my_string = "hello welcome to world of python"

# count
c = my_string.count("e")
print(c)


# startswith and endswith
a = my_string.startswith("hello")
print(a)

b = my_string.endswith("hello")
print(b)


# index
d = my_string.index("h")
print(d)

# f = my_string.index("z")  # it willgive error
# print(f)


# find : similar to index

e = my_string.find("h")
print(e)

g = my_string.find("z")  # it will give -1
print(g)


# replace

h = my_string.replace("e", "E")
print(h)


# strip:
new_string = "@@@@@@@@@hello world       "
s = new_string.strip("@")
print(new_string)
print(s)
