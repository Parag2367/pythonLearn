"""
Ask 2 numbers from user.
Calculate total of 2 numbers.
Print if the sum is odd or even

2- add() , check()
"""


def add(n1, n2):
    total = n1 + n2
    return total


def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


x = int(input("Enter number 1 = "))
y = int(input("Enter number 2 = "))
s = add(x, y)
print(f"Total = {s}")
print(check(s))
