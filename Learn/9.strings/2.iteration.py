"""ITERATION"""

my_string = "code and debug"

# By Index
for index in range(0, len(my_string)):
    print(my_string[index])

# By Value
for ch in my_string:
    print(ch, end=" ")


# By both

for i, ch in enumerate(my_string):
    print(i, ch)
