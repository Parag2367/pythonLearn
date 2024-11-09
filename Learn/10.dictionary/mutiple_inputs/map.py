"""
if we want to take multiple inputs
"""

# a = int(input("Enter a number = "))
# b = int(input("Enter a number = "))
# c = int(input("Enter a number = "))


# another way:

# a, b, c = input(
#     "Enter numbers = "
# ).split()  # as input gives value in string so we can split it, and that gives list, unpacking
# a = int(a)
# b = int(b)
# c = int(c)

# print(a)
# print(b)
# print(c)


# another way is using map method

a, b, c = map(
    int, input().split()
)  # map takes one function and iterables split gives a iterable
print(a)
print(b)
print(c)
