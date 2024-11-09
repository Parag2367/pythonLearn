"""
if age < 18 raise error
"""

# try:
#     age = int(input("Enter age of voter = "))
#     if age < 18:
#         raise ZeroDivisionError  # we are raising any random error not realted
#     print("You can vote")
# except ZeroDivisionError:  # referencing line 8
#     print("You can not vote")
# except ValueError:
#     print("Enter proper age value")
# except:
#     print("Some other error occured")


"""
Write a Python function that takes two numbers as input and returns
the result of their division. Handle the ZeroDivisionError exception if the
second number is zero. If there is ZeroDivisionError, the function should
return -1.
"""

# try:
#     a = int(input("Enter a number = "))
#     b = int(input("Enter a number = "))
#     print(a / b)
# except ZeroDivisionError:
#     print(-1)
# except:
#     print("Some error occured")


"""
Write a function that takes a list as input and prints the element at
index 5. Handle the IndexError exception if the list doesn't have enough
elements.

"""


# def listindex(mylist: list):
#     try:
#         print(mylist[5])
#     except IndexError:
#         print("there are only few elements in list")


# mylist = [23, 33, 44, 55, 66, 23]

# listindex(mylist)

"""
Write a function divide that takes two numbers as input and returns
their division. Call this function with invalid input arguments (e.g., strings
instead of numbers) and handle any exceptions that may occur
"""


def divv(a, b) -> float:
    try:
        z = a / b
        return z
    except TypeError:
        return -1
    except ZeroDivisionError:
        return -2


print(divv(3, 4))
print(divv(3, "abc"))
