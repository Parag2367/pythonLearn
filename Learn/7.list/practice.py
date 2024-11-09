# my_list = [345, 56, 78, "Praga", 78.99]

# for i in range((len(my_list) - 1), -1, -1):
#     print(my_list[i])

##################

# my_list = [34, 45, 67, 88, 98, 56, 23, 33]

# for a in my_list:
#     if a % 2 == 0:
#         print("even number", a)
#     elif a % 2 == 1:
#         print("odd number", a)

##############################

# my_list = [34, 45, 67, 88, 98, 56, 23, 33]

# for i in range(0, len(my_list)):
#     if i % 2 == 0 and i != 0:
#         print(my_list[i])


#################################

# my_list = [34, 45, 67, 88, 98, 56, 23, 33]
# sum = 0
# for a in my_list:
#     sum = sum + a
# print(sum)


#####################

# my_list = [34, 45, 67, 88, 98, 56, 23, 33]

# count = 0

# for a in my_list:
#     if a % 2 == 0 and a != 0:
#         count = count + 1
# print(count)


############################

# my_list = [34, 45, 67, 88, 98, 56, 23, 33, 200, 3000]

# count = 0

# for a in my_list:
#     if a % 2 == 0 and a % 5 == 0:
#         count = count + 1
# print(count)


######################

# my_list = [34, 45, 67, 88, 98, 56, 23, 33, 200, 3000]

# sum = 0
# for a in my_list:
#     if a % 2 == 0 and a != 0:
#         sum = sum + a
# print(sum)


##########################

# my_list = [34, 45, 67, 88, 98, 56, 23, 33, 200, 3000]

# sum = 0
# for a in my_list:
#     if a % 3 == 0 or a % 4 == 0:
#         sum = sum + a
# print(sum)


###############################

# my_list = [0, -1, -234, 45, 67, 88, 98, 56, 23, 33, 200, 3000]
# count = 0
# countn = 0
# for a in my_list:
#     if a >= 0:
#         count = count + 1
#     else:
#         countn = countn + 1
# print("positive numbers count", count)
# print("negative numbers count", countn)

#############################
# find the largest number in a list
# my_list = [0, -1, -234, 45, 67, 88, 98, 56, 23, 33, 200, 3000]

# largest = my_list[0]

# for i in range(0, len(my_list)):
#     if my_list[i] > largest:
#         largest = my_list[i]
# print(largest)

# # iterating through values:

# for a in my_list:
#     if a > largest:
#         largest = a
# print(largest)


# find the smallest number in a list
# my_list = [0, -1, -234, 45, 67, 88, 98, 56, 23, 33, 200, 3000]

# smallest = my_list[0]

# for a in my_list:
#     if a < smallest:
#         smallest = a
# print(smallest)

"""
Find largest number in a list
"""


# def largest(my_list: list) -> list:
#     largest = my_list[0]
#     for a in my_list:
#         if a > largest:
#             largest = a
#     return largest


# my_list = [10000, -1, -234, 45, 67, 88, 98, 56, 23, 33, 200, 3000]

# print(largest(my_list))


"""
 Create a function updateOddEven that accepts an List of Integers and
update all the even numbers to 0 and update all the odd numbers to 1.
"""


# def updateOddEven(my_list: list) -> list:
#     for i in range(0, len(my_list)):
#         if i % 2 == 0:
#             my_list[i] = 0
#         else:
#             my_list[i] = 1
#     return my_list


# my_list = [2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 12, 15, 16]
# print(updateOddEven(my_list))


"""
Create a function updateOddEven that accepts an List of Integers and
update all the even numbers to increment by 1 and update all the odd
numbers to decrement by 1.
"""


# def updateOddEven(my_list: list) -> list:
#     for i in range(0, len(my_list)):
#         if i % 2 == 0:
#             my_list[i] += 1
#         else:
#             my_list[i] -= 1
#     return my_list


# my_list = [2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 12, 15, 16]
# print(updateOddEven(my_list))


"""
Create a function calculatePrime that accepts an List of Integers and
print all the prime numbers in that list.
"""


def calculatePrime(mylist: list):
    for a in mylist:
        count = 0
        for i in range(1, a + 1):
            if a % i == 0:
                count = count + 1
        if count == 2:
            print(a, end=" ")


mylist = [2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 12, 15, 16]
calculatePrime(mylist)
