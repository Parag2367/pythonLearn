# . Ask a number from user. Print all the numbers from 1 to that number.

# num = int(input("Enter a number = "))

# i = 1
# while i <= num:
#     print(i,end=" ")
#     i = i+1


# Ask a number (N) from user. Print all the numbers from N to 1.


# def printnum(n):
#     i = n
#     while i >= 1:
#         print(i, end=" ")
#         i = i - 1


# printnum(10)

# another approach

# num1 = int(input("Enter your number = "))
# i = num1
# while i >= 1:
#     print(i, end=" ")
#     i = i - 1

##############################################
# Ask start number and end number from user. Print all the numbers from start to end using while loop.

# start = int(input("Enter start number = "))
# end = int(input("Enter end number = "))

# i = start
# while i <= end:
#     print(i, end=" ")
#     i = i + 1

# another approach


# def printMtoN(start, end):
#     if start > end:
#         i = end
#         while i <= start:
#             print(i, end=" ")
#             i = i + 1
#     elif start == end:
#         print(start)
#     else:
#         i = start
#         while i <= end:
#             print(i, end=" ")
#             i = i + 1


# start = int(input("Enter start number = "))
# end = int(input("Enter end number = "))
# printMtoN(start, end)

# # another approach
# def printNum(n1,n2):
#     start = n1 if n1<n2 else n2
#     end = n2 if n1<n2 else n1
#     while start <=end:
#         print(start,end=" ")
#         start = start + 1

# Calculate the sum of all the numbers from 1 to 10.

# sum = 0
# i = 1
# while i <= 10:
#     sum = sum + i
#     i = i + 1
# print(sum)


# Calculate product of all the numbers from 1 to 10.


# def product():
#     prod = 1
#     i = 1
#     while i <= 10:
#         prod *= i
#         i += 1
#     return prod


# a = product()
# print(a)


# Calculate how many numbers are divisible by 7 from 1 to 100

# i = 1
# count = 0
# while i <=100:
#     if i%7 == 0:
#         count = count + 1
#     i = i+1
# print(count)

# Calculate how many numbers are divisible by both 6 and 7 between 1 to 200.

# i = 1
# count = 0

# while i <=200:
#     if i%6 == 0 and i%7 == 0:
#         count = count +1
#     i = i+1
# print(count)


# Write a program to calculate the sum of all the numbers divisible by 4 from 20 to 50.

# i = 20
# sum = 0

# while i <=50:
#     if i%4 == 0:
#         sum = sum +i
#     i = i+1
# print(sum)


# . Ask a number from user. Print the multiplication table of that number.

# num = int(input("Enter a number = "))

# i = 1

# while i <=10:
#     product = num * i
#     print(f"{num} * {i} = {product}")
#     i = i +1


# Calculate factorial of a number entered by user.

# num1 = int(input("Enter number = "))

# fact = 1
# i = num1
# while i >=1:
#     fact = fact*i
#     i = i-1
# print(fact)


"""Ask to numbers x and y from the user. 
If x<y then print all the numbers from x to y, but if y<x then print all the numbers from y to x."""

# x = int(input("Enter number1 = "))
# y = int(input("Enter number2 = "))

# t = x - y

# if t > 0:
#     while x < y:
#         print(x, end=" ")
#         x = x + 1

# else:
#     while y < x:
#         print(y, end=" ")
#         y = y + 1


"""
Create a function named div_by_3_and_5 which takes 2 integers as a
arguments (n1,n2), and print all the numbers divisible by 3 and 5 between
n1 and n2.
"""


# def div_by_3_and_5(n1, n2):
#     if n1 > n2:
#         i = n2
#         while i <= n1:
#             if i % 3 == 0 and i % 5 == 0:
#                 print(i, end=" ")
#             i = i + 1
#         print()
#     elif n2 > n1:
#         i = n1
#         while i <= n2:
#             if i % 3 == 0 and i % 5 == 0:
#                 print(i, end=" ")
#             i = i + 1
#         print()
#     else:
#         print("they are equal")


# div_by_3_and_5(25, 50)
# div_by_3_and_5(50, 25)


"""
Create a function named multiplicationTable that takes an integer
num as an argument. Print the multiplication table of that number up to 10
numbers.
"""


# def mulTable(n):
#     i = 1
#     while i <= 10:
#         print(f"{n} * {i} = {n*i}")
#         i = i + 1


# mulTable(10)


"""
Create a function named printPattern that takes one integer (num) as
an argument. Print from -num to num. Also keep in mind number passed as
an argument can be negative or positive.
"""


# def printPattern(num):
#     if num > 0:
#         i = -num
#         while i <= num:
#             print(i, end=" ")
#             i = i + 1
#     elif num == 0:
#         print(num)
#     else:
#         i = num
#         while i <= -num:
#             print(i, end=" ")
#             i = i + 1


# printPattern(-10)

"""
Print factor of number,count factor
"""


# def printFactor(num):
#     i = 1
#     while i <= num:
#         if num % i == 0:
#             print(i, end=" ")
#         i = i + 1
#     print()


# def countFactor(num):
#     count = 0
#     i = 1
#     while i <= num:
#         if num % i == 0:
#             count = count + 1
#         i = i + 1
#     print(count)


# printFactor(14)
# countFactor(14)


"""
Prime factor
"""


# def checkPrime(num):
#     count = 0
#     i = 1
#     while i <= num:
#         if num % i == 0:
#             count = count + 1
#         i = i + 1
#     if count == 2:
#         print("It is prime number")
#     else:
#         print("Not a prime number")


# checkPrime(7)

"""
factor sum till (1,n2), which are divisible by n1
"""


# def factorSum(n1: int, n2: int) -> int:
#     i: int = 1
#     sum: int = 0
#     while i <= n2:
#         if i % n1 == 0:
#             sum = sum + i
#         i = i + 1
#     return sum


# x = factorSum(7, 30)
# print(x)


"""
take number continously, when number = 0 break and print sum
"""
total = 0
while True:
    num: int = int(input("Enter a number = "))
    if num != 0:
        total = total + num
    if num == 0:
        break
print(total)
