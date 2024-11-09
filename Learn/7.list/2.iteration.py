x = [45, 65, 76, 78.999, "Parag", [89, 98, 76], (45, "Ram", 78)]

# y = len(x)  # inbuild function
# print(y)

# # iterating through index:

# for i in range(0, len(x)):
#     print(x[i])


# # iteration through value:

# for a in x:
#     print(a, end=" ")

# # both ways are okay to use

# print()
# for i in range(len(x) - 1, -1, -1):
#     print(x[i], end=" ")

# print()

# for i in range(-1, -(len(x) + 1), -1):
#     print(x[i], end=" ")


# Iteration using both ways

# enumerate

for a in enumerate(x):
    print(a, end=" ")


for i, j in enumerate(x):
    print(j, end=" ")
