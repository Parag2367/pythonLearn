"""
Given a list of strings, concatenate them into a single string separated
by spaces. For example, given the input ["Hello", "World", "Python"], the
output should be "Hello World Python".

"""

# def conc(mylist: list) -> str:
#     mystr = ""
#     for a in mylist:
#         if type(a) == str:
#             mystr = mystr + a + " "
#         elif type(a) != str:
#             mystr = mystr + str(a) + " "
#     return mystr


# mylist = ["Hello", "World", "Python"]
# print(conc(mylist))


"""
Write a program to rotate the characters in a string by a given number
of positions. For example, given the input "abcdef" and rotation of 2, the
output should be "efabcd".
Ask string and rotation from the user.
"""


# def rotate(mystr: str, num: int) -> str:
#     new_str = ""
#     if 0 <= num <= len(mystr):
#         a = mystr[-(len(mystr)) : -num]
#         for i in range(-1, -(num + 1), -1):
#             new_str = new_str + mystr[i]
#     else:
#         print("Number is invalid")
#     return new_str + a


# mystr = "abcdef"

# print(rotate(mystr, 2))

# another approach more optimised


# def rotationOfString(string: str, rotation: int) -> str:
#     # We will keep removing last character from the end
#     # and put it to the front. This is one rotation
#     for _ in range(rotation):
#         """
#         string[-1] means last character
#         string[:-1] means from start to end-1
#         """
#         string = string[-1] + string[:-1]
#     return string


"""
Create a dictionary that counts the frequency of words in a given
string. Ask string from user.

"""


def countDict(mystr: str) -> dict:
    mydict = {}
    mylist = mystr.split()
    for a in mylist:
        if a in mydict:
            mydict[a] += 1
        else:
            mydict[a] = 1
    return mydict


mystr = "The cat and the dog played in the park The cat chased the dog"

print(countDict(mystr))
