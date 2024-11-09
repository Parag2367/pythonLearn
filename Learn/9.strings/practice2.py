"""
. Ask a string from user. If the length of string is odd, then change all the
capital letters to small and vice versa, but if the length of string is even,
reverse the string. Do this using a function and return the output.

"""

# def misc(mystr: str) -> str:
#     if len(mystr) % 2 == 0:
#         return mystr[::-1]
#     else:
#         a = mystr.swapcase()
#         return a


# mystr = "aeroPlaNE"
# print(misc(mystr))

# print(misc("paraga"))


"""
 Write a function which accepts a String as a parameter and return the
reversed words as a String.

"""


def rev(mystr: str) -> str:
    a = mystr.split()
    reverse = " , ".join(a[i] for i in range(len(a) - 1, -1, -1))
    # reverse = " ".join(i for i in a[::-1])
    return reverse


print(rev("python is great"))

"""
Ask 5 integers from user. Then ask a single character from user. Print
those integers separated by that character entered by user.
"""


# def misc():
#     mylist = []
#     for i in range(0, 6):
#         a = str(input("Enter a number = "))
#         mylist.append(a)

#     ch = input("Enter a characte = ")

#     result = ch.join(mylist)
#     print(result)


# misc()


# mystr = "pytrhon is great"
# a = mystr[::-1]
# print(a)


"""
Write a function which accepts a String and another string (which will
be a single character) as a parameter. Join that string along with that
character.

"""


# def misc(mystr: str, a: str) -> str:
#     b = mystr.split()
#     if len(b) % 2 == 0:
#         result = a.join(b)
#     else:
#         result = a.join(b[i] for i in range(len(b) - 1, -1, -1))
#         # result = a.join(i for i in b[::-1])
#     return result


# mystr = "python is great language"

# print(misc(mystr, "#"))
