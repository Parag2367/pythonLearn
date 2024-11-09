"""SLICING"""

a = "code and debug"

b = a[0:4]
print(b)

c = a[::]
print(c)

z = a[-5:-1]

d = a[-5:]  # by default step is +1(left to right)
print(d)

e = a[::-1]
print(e)

# methods in string
f = a.capitalize()
print(f)
