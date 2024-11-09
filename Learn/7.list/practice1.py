"""
Write a program that prompts the user to specify the length of a list and then requests numbers to populate that list.
 Display the final list as the output.
"""

# length = int(input("Enter length of list = "))
# my_list = []
# for a in range(1, length + 1):
#     value = int(input(f"Enter {a} value = "))
#     my_list.append(value)

# print(my_list)

# using while loop:
# length = int(input("Enter length of list = "))
# my_list = []

# i = 1
# while i <= length:
#     value = int(input(f"Enter {i} value = "))
#     my_list.append(value)
#     i = i + 1
# print(my_list)


"""
Create a list and prompt the user for an 'old number' followed by a
'new number.' If the 'old number' exists in the list, replace it with the 'new
number' provided by the user
"""

# old = int(input("Enter an old number = "))
# new = int(input("Enter a new number = "))

# my_list = [5, 10, 15, 20, 15]

# for i in range(0, len(my_list)):
#     if my_list[i] == old:
#         my_list[i] = new
# print(my_list)

# # removing all the even numbers
# for a in my_list:
#     if a % 2 == 0:
#         my_list.remove(a)
# print(my_list)


"""
Ask the user for a number. Then, from a list of numbers, remove all
the numbers that can be divided by the number the user entered.
"""

# my_list = [5, 10, 15, 20, 25]

# num = int(input("Enter a number = "))

# for a in my_list:
#     if a % num == 0:
#         my_list.remove(a)
# print(my_list)


"""
Generate a list of at least 10 numbers. Then, create two separate
lists called 'odd' and 'even.' Put all the odd numbers from the original list
into the 'odd' list, and all the even numbers into the 'even' list.

"""

# my_list = [2, 3, 5, 4, 7, 8, 9, 10, 13, 25, 17]

# even_list = []
# odd_list = []

# for a in my_list:
#     if a % 2 == 0:
#         even_list.append(a)
#     elif a % 2 == 1:
#         odd_list.append(a)
# print("list of even numbers", even_list)
# print("list of odd numbers", odd_list)


"""
Start by creating two separate lists with random numbers. Then,
create a third list that merges the numbers from the first and second lists
together
"""

l1 = [5, 8, 7, 9, 4]
l2 = [4, 5, 6, 7, 8]
r = l1 + l2  # another way
result = []

for a in l1:
    result.append(a)

for b in l2:
    result.append(b)

print(result)
print(r)
