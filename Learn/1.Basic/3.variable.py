"""
Rules for variables:
1. It should always start with a-z,A-Z,_
2. It can contain a-z, A-Z, 0-9, _
3. It cannot contain symbols
4. It connot contain reserved keywords if,else,int,etc...
5. It is case sensitive
"""
# x = 5
# y = 34
# z = x+y

# print(x)
# print(y)
# print(z)

name = "Parag"
age = 30
gender = "M"

print(name, age, gender)

# printing variables
# method2
print("my name is", name)
print("my age is", age)
print("my gender is", gender)

print("my name is", name, "my age is", age, "my gender is", gender)


# method3 (f-string)
print(f"my name is {name}")
print(f"my age is {age}")
print(f"my gender is {gender}")

print(f"my name is {name} my age is {age} my gender is {gender}")

print(f"{name = }")  # a way to print a variable along with its name


# method 4 (identifiers)

# %s = String
# %d = Integer
# %f = Float

print("my name is %s" % (name))
print("my age is %d" % (age))
print("my name is %s" % (gender))
print("my name is %s, my age is %d, my gender is %s" % (name, age, gender))
