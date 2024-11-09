"""
Ask a string from user. Count how many alphabets are there in that
string.
"""

# my_string = input("Enter a string = ")
# count = 0
# for a in my_string:
#     if a.isalpha():
#         count = count + 1
#     else:
#         pass
# print("number of alphabets are ", count)

# WE CAN DO WITH USING ASCII ALSO THAT IS HOW PYTHON DO IT IN BACKGROUND


"""
Ask a string from user. Count the number of uppercase and
lowercase characters in that String.
"""

# my_string = input("Enter a string = ")

# cu = 0
# cl = 0

# for a in my_string:
#     if a.isupper():
#         cu = cu + 1
#     elif a.islower():
#         cl = cl + 1
#     else:
#         pass

# print("uppercase number", cu)
# print("lowercase number", cl)

# we can also use it using ascii values


"""
Ask a string from user. Convert all the alphabets to uppercase
"""

# my_string = input("Enter a string = ")

# for a in my_string:
#     if a.isalpha():
#         my_string = my_string.upper()
#     else:
#         pass
# print(my_string)


# using ascii:
# result = ""
# for a in my_string:
#     ascii = ord(a)
#     if ascii >= 97 and ascii <= 122:
#         new_ascii = ascii - 32
#         char = chr(new_ascii)
#         result = result + char

#     else:
#         result = result + a
# print(result)

"""
Ask a string from user. Convert uppercase to lowercase and convert
lowercase to uppercase and do not change the other letters.
"""

# my_string = input("Enter a string = ")

# for a in my_string:
#     if a.isalpha():
#         my_string = my_string.swapcase()
#     else:
#         pass
# print(my_string)

"""
Count the number of spaces in a string entered by user.
"""

# my_string = input("Enter a string = ")
# count = 0
# for a in my_string:
#     if a.isspace():
#         count = count + 1
#     else:
#         pass
# print(count)


"""
Ask a string from user. Print the count of how many alphabets, digits,
spaces and symbols (everything else) are there in that string.
"""

# my_string = input("Enter a string = ")

# ca = 0
# cn = 0
# cs = 0

# for a in my_string:
#     if a.isalpha():
#         ca = ca + 1
#     elif a.isdigit():
#         cn = cn + 1
#     elif a.isspace():
#         cs = cs + 1
#     else:
#         pass

# cr = len(my_string) - (ca + cs + cn)

# print("alphabets", ca)
# print("digits", cn)
# print("spaces", cs)
# print("rest", cr)

"""
Write a python program to ask a string from user. Then count the
number of vowels and number of consonants in that string.

"""


# def cnt(mystring: str):
#     vowels = "aeiouAEIOU"
#     countv = 0
#     countc = 0
#     for ch in mystring:
#         if ch in vowels:
#             countv = countv + 1
#         else:
#             countc = countc + 1
#     print(f"{countv = }")
#     print(f"{countc = }")


# mystring = "abcdefgHIJK"
# cnt(mystring)


"""
. Ask a string from user. Print the string with first 2 letters and last 2
letters.

"""

# mystr = input("Enter a string = ")
# final = mystr[:2] + mystr[-2:]

# print(final)

"""
Write a python program to only print second half of the string. Ask
string from user
"""


# def second(mystr: str):
#     n = len(mystr) // 2
#     if len(mystr) % 2 == 0:
#         a = mystr[n:]
#     else:
#         a = mystr[n + 1 :]
#     return a


# mystr = "aeroplane"
# print(second(mystr))
# print(second("delhi"))

"""
Ask a string from user. Print how many characters are there which are
not alphabets.
"""


def notAlpha(mystr: str):
    cnt = 0
    for a in mystr:
        # while i < len(mystr):
        if ord(a) not in range(65, 91) and ord(a) not in range(97, 123):
            cnt = cnt + 1
    return cnt


mystr = "AB788&*(^%&*%^&aaaa"
print(notAlpha(mystr))
