"""
For list, tuple
"""

name, age, gender, *marks = ["Parag", 23, "Male", 23, 45, 67, 88, 99]

print(name)
print(age)
print(gender)
print(marks)


x, *y, z = [2, 3, 5, 7, 8, 6]
print(x)  # first
print(y)
print(z)  # last


*x, y, z = [2, 4, 3, 1, 6, 9, 11]
print(x)
print(y)  # second last
print(z)  # last
