# Function ki duniya apni hi alag hote hai, uske variables uske hi hote hai alag donot get confused, if variable name is same


# def addition():
#     num1: int = int(input("Enter number 1 = "))
#     num2: int = int(input("Enter number 2 = "))
#     print(f"Answer is {num1 + num2}")


# def subtraction():
#     num1: int = int(input("Enter number 1 = "))
#     num2: int = int(input("Enter number 2 = "))
#     print(f"Answer is {num1 - num2}")


# def mul():
#     num1: int = int(input("Enter number 1 = "))
#     num2: int = int(input("Enter number 2 = "))
#     print(f"Answer is {num1 * num2}")


# def div():
#     num1: int = int(input("Enter number 1 = "))
#     num2: int = int(input("Enter number 2 = "))
#     print(f"Answer is {num1 /num2}")


# num1 = 10
# addition()
# subtraction()
# print(num1)

# # scope of the variables which are created inside a function is limited to that function only
# # it cannot be called outside of that function
# # example see below


# # see it is showing num1 is not defined , but it is under function so the scope of the variable is limited to the function
# # print(num1)
# # print(num2)  # as it is inside function


# # more example on scopping
# def greet():
#     name = input("Enter your name = ")
#     print(f"Welcome to the session {name}")


# name = "xyz"

# greet()  # this will give its own output as it is already defined

# print(
#     name
# )  # this will give the output for name variable which is defined at this level


"""
Function with parameter
"""


def add(a: int, b: int, c: int, d: int):
    print(a + b + c + d)


add(23, 34, 45, 24)


#############################
def mul(a: int, b: int, c: int):
    print(a * b * c)


mul(23, 22, 21)


############################
def mul1(a, b, c):
    print(a * b * c)


a: int = int(input("Enter number = "))
b: int = int(input("Enter number = "))
c: int = int(input("Enter number = "))

mul1(a, b, c)
