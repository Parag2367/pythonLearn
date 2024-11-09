"""
. Create a function named oddCharacters which takes a string as a
parameter. Now return a list of characters which appears odd times in that
string.

"""

# def oddChar(mystr: str) -> list:
#     mylist = []
#     for a in mystr:
#         if mystr.count(a) % 2 != 0:
#             mylist.append(a)
#     return mylist


# print(oddChar("hello"))
# print(oddChar("aeroplane"))

### another approach better logic

# def oddChar(mystr: str) -> list:
#     char_count = {}
#     for ch in mystr:
#         char_count[ch] = char_count.get(ch, 0) + 1
#     result = []
#     for char, count in char_count.items():
#         if count % 2 != 0:
#             result.append(char)
#     return result


# print(oddChar("hello"))
# print(oddChar("aeroplane"))


"""
Create a function named arrangeChars which takes a string as a
parameter. Now return a string with max frequency chars at start.

'aaeroplane'
 output: aaaeeropln
"""


# def arrangeChars(mystr: str) -> str:
#     result = {}
#     for ch in mystr:
#         # result[ch] = 0
#         # result[ch] += 1 # same as below
#         result[ch] = result.get(ch, 0) + 1  # used result.get(ch,0) to make value zero
#     final = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
#     mys = ""
#     for k, v in final.items():
#         mys = mys + k * v
#     return mys


# print(arrangeChars("aaeroplane"))


"""
Given a string S, containing numeric words, the task is to convert the
given string to the actual number.

"""


# def numeric(mystr: str):
#     mydict = {
#         "zero": 0,
#         "one": 1,
#         "two": 2,
#         "three": 3,
#         "four": 4,
#         "five": 5,
#         "six": 6,
#         "seven": 7,
#         "eight": 8,
#         "nine": 9,
#     }
#     mylist = mystr.split()
#     res = ""
#     for a in mylist:
#         num = mydict[a]
#         res = res + str(num)
#     return res


# print(numeric("zero four zero one"))

# # optimized:
# help_dict = {
#     "one": "1",
#     "two": "2",
#     "three": "3",
#     "four": "4",
#     "five": "5",
#     "six": "6",
#     "seven": "7",
#     "eight": "8",
#     "nine": "9",
#     "zero": "0",
# }

# string = "zero four zero one"


# res = "".join(help_dict[ele] for ele in string.split())

# print(res)


"""
. Write a Python program to generate two strings from a given string. For
the first string, use the characters that occur only once, and for the
second, use the characters that occur multiple times in the said string.

aaabbcdef
str1 = ab
str2 = cdef
"""


# def twoStr(mystr: str):
#     result = {}
#     mystr1 = ""
#     mystr2 = ""
#     for ch in mystr:
#         result[ch] = result.get(ch, 0) + 1
#     for k, v in result.items():
#         if v == 1:
#             mystr1 = mystr1 + k
#         else:
#             mystr2 = mystr2 + k
#     print(mystr1)
#     print(mystr2)


# twoStr("aaabbcdef")


"""
Convert a list of Tuples into Dictionary

"""


# def toDict(mylist: list):
#     mydict = {}
#     for a in mylist:
#         mydict[a[0]] = [a[1]]
#     print(mydict)


# toDict(
#     [
#         ("akash", 10),
#         ("gaurav", 12),
#         ("anand", 14),
#         ("suraj", 20),
#         ("akhil", 25),
#         ("ashish", 30),
#     ]
# )


# ## another way

# def convert(tup, di):
#     for a, b in tup:
#         di.setdefault(a, []).append(b)
#     return di


"""
Write a Python program to capitalize the first and last letters of each
word in a given string.

"""


def convert(mystr: str):
    result = []
    mylist = mystr.split()
    for ch in mylist:
        a = ch[:-1].title() + ch[-1].upper()
        result.append(a)
    final = " ".join(i for i in result)
    print(final)


convert("python is a great language")
convert("PythoN ExerciseS PracticE SolutioN")


# another approach


def capitalize_first_last_letters(str1):
    str1 = result = str1.title()
    result = ""
    for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
    return result[:-1]
