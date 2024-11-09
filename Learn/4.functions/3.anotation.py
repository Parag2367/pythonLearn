# we do not have to mention the types , but it is a good practice to mention them
# def add(x: int, y: int) -> int:
#     total = x + y
#     return total


# a = add(10, 20)
# print(a)


# ##
# def greet(name: str, age: int, percentage: float):
#     print(name)
#     print(age)
#     print(percentage)


# greet(
#     233, 23, 34.5
# )  # this will still work but it is good to mention, as it is not strict

# greet("parag", 23, 45)


###################
from typing import *


def sum_of_list(x: List[int]):
    print(sum(x))


sum_of_list([23, 34, 45, 65])
sum_of_list([23, 34, 45, 56, 78])
