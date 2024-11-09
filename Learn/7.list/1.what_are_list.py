# Parag = [23, 45, 44, 48, 50]

# print(Parag)
# print(type(Parag))


# Details = [23, 44, 89, " ", 78.564, 67.8976, "Parag", [23, 45, 67], (23, 45, "Rahul")]
# print(Details)
# print(type(Details))


x = [45, 32, 65, 75, "Parag", 78.99]

print(x[3])
print(type(x[3]))

y = len(x)
print(y)

print(x[-1])

# multiply
print([2, 3, 4] * 3)

# addition
print([2, 3, 4] + [5, 6, 7])


# we can use both types of iterations

my_list: list[int | str | float] = [45, 32, 65, 75, "Parag", 78.99]

from typing import List

my_list1: List[int | str | float] = [45, 32, 65, 75, "Parag", 78.99]
