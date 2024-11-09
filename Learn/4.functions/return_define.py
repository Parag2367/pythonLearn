# return gives you a value so you have to stare it or you can directly print that separately
# print wll directly print when you call the function


# def addition(n1: int, n2: int) -> int:  # n1,n2 are parameters
#     sum = n1 + n2
#     return sum


# # using return is a good practice

# # this will not give any output, we have to store it in a variable as it is returning something
# addition(20, 30)

# # this will give us the output
# b = addition(20, 30)
# print(b)  # it will give output


# ####################################################
# # another explanation
# def subtraction(n1, n2):
#     sub = n1 - n2
#     print(sub)


# x = subtraction(300, 100)  # as it is not RETURNING anything x will be None
# print(x)  # this will print None


"""
check if total is odd/even
"""


def total(n1: int, n2: int) -> int:
    return n1 + n2


def check(n1: int) -> None:
    if n1 % 2 == 0:
        print("Even")
    else:
        print("odd")


num1: int = int(input("Enter number ="))
num2: int = int(input("Enter number ="))
a = total(num1, num2)
print(a)
check(a)
