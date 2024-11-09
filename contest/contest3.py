"""
Create a python function named isPalindrome which accepts a string
as a parameter and return True if its a palindrome. Palindrome are words
which is same when read from start and same when read from the end.
"""

# def isPalindrome(mystr: str) -> bool:
#     if mystr.lower() == mystr.lower()[::-1]:
#         return True
#     else:
#         return False


# mystr = "ABCcba"
# a = isPalindrome(mystr)
# print(a)


"""
Keep asking characters from user until he presses q on the keyboard.
Change all the capital letters to small, and all the small letters to capital.
"""

# mystr = ""

# while True:
#     char = input("Enter a character = ")
#     ascii_code = ord(char)
#     if char == "q":
#         break
#     else:
#         if ascii_code >= 65 and ascii_code <= 90:
#             small_letter = chr(ascii_code + 32)
#             mystr += small_letter
#         elif ascii_code >= 97 and ascii_code <= 122:
#             capital_letter = chr(ascii_code - 32)
#             mystr += capital_letter
# print(mystr)


"""
Python Program to remove all duplicates from a given string.
"""


# def rDuplicate(mystr: str) -> str:
#     result = ""
#     for a in mystr:
#         if a not in result:
#             result += a
#     return result


# mystr = "aappalone"
# z = rDuplicate(mystr)
# print(z)


"""
Ask a sentence from user. Then ask a integer k from user. Print all the
words which are greater or equal to k.
"""


# def greater(mystr: str, num: int) -> str:
#     lst = mystr.split()
#     chr = []
#     for a in lst:
#         if len(a) >= num:
#             chr.append(a)

#     result = " ".join(chr)

#     return result


# mystr = "python is great to learn"
# z = greater(mystr, 5)
# print(z)


"""
Make a password strength function. It will accept a string from user.
Return True if it is a strong password.
Strong password has these characteristics.
Minimum 8 character
Minimum 1 uppercase alphabet
Minimum 1 lowercase alphabet
Contains at least 1 special symbol (any symbol)
Minimum 1 digit
"""


def strongPwd(mystr: str):
    l, c, d, s = 0, 0, 0, 0
    special = "@_!#$%^&*()<>?/|}{~:"
    if len(mystr) >= 8:
        for ch in mystr:
            if ch.islower():
                l += 1
            if ch.isupper():
                c += 1
            if ch.isdigit():
                d += 1
            if ch in special:
                s += 1
    if l >= 1 and c >= 1 and d >= 1 and s >= 1 and l + c + d + s == len(mystr):
        print("Strong Password")
    else:
        print(
            "Your Password is not strong: it should have\nMinimum 8 character\nMinimum 1 uppercase alphabet\nMinimum 1 lowercase alphabet\nContains at least 1 special symbol (any symbol)\nMinimum 1 digit "
        )


mystr = "parag1234P@"
strongPwd(mystr)

# another approach:


def isStrongPassword(password: str):
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_special = True

    if (
        len(password) >= 8
        and has_uppercase
        and has_lowercase
        and has_digit
        and has_special
    ):
        return True
    else:
        return False


password = input("Enter a password: ")
print(isStrongPassword(password))
