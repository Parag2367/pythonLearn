"""
Make a function which takes filename as a parameter. Return the
number of words present in that file.

"""

# def charFile(name: str) -> int:
#     f = open(name, "r")
#     x = f.read()
#     count = 0
#     for ch in x:
#         if ch != " " and ch != "\n":
#             count += 1

#     f.close()
#     return count


# print(charFile("hello.txt"))


"""
Make a function which takes filename as a parameter. Return the
number of lines present in that file.

"""


# def numLine(name: str) -> int:
#     try:
#         f = open(name, "r")
#         lines = f.readlines()
#         f.close()
#         if len(lines) == 0:
#             raise FileExistsError
#         else:
#             return len(lines)
#     except FileNotFoundError:
#         return -1
#     except FileExistsError:
#         return -1


# print(numLine("hello.txt"))


"""
Make a function which takes filename as a parameter. Return the
number of lines present in that file which does not start with T or t.
"""


# def torT(name: str) -> int:
#     try:
#         f = open(name, "r")
#         lines = f.readlines()
#         f.close()
#         count = 0
#         for line in lines:
#             if line.strip().lower().startswith("t"):
#                 count += 1

#         return len(lines) - count
#     except FileNotFoundError:
#         return -1


# print(torT("hello.txt"))


"""
Make a function which takes filename as a parameter. Return the
number of time the word the has appeared in that file.
"""


# def nothe(filename: str) -> int:
#     try:
#         f = open(filename, "r")
#         lines = f.readlines()
#         f.close()
#         count = 0
#         for line in lines:
#             words = line.split()
#             for a in words:
#                 if a.lower() == "the":
#                     count += 1
#         return count
#     except FileNotFoundError:
#         return -1

# another way


# def nothe(filename: str) -> int:
#     try:
#         f = open(filename, "r")
#         data = f.read()
#         words = data.split()
#         f.close()
#         count = 0
#         for word in words:
#             if word.lower() == "the":
#                 count += 1
#         return count
#     except FileNotFoundError:
#         return -1


# print(nothe("hello.txt"))


"""
Make a function which takes filename as a parameter. Print the words
in that file which has length greater than 4.

"""


# def more4(filename: str):
#     try:
#         f = open(filename, "r")
#         lines = f.readlines()
#         f.close()

#         for line in lines:
#             words = line.split()
#             print(" ".join(a for a in words if len(a) >= 4))
#     except FileNotFoundError:
#         return -1


# more4("hello.txt")


"""
Make a function which takes filename as a parameter. Return the count
of words which end with e.

"""


# def endse(filename: str) -> int:
#     try:
#         f = open(filename, "r")
#         data = f.read()
#         f.close()
#         words = data.split()

#         count = 0
#         for a in words:
#             if a.lower().endswith("e"):
#                 count += 1
#         return count

#     except FileNotFoundError:
#         return -1


# print(endse("hello.txt"))


"""
. Aditi has used a text editing software to type some text. After saving
the article as WORDS.TXT, she realized that she has wrongly typed
alphabet J in place of alphabet I everywhere in the article.
Write a function definition for JTOI() in Python that would display the
corrected version of entire content of the file WORDS.TXT with all the
alphabets "J" to be displayed as an alphabet "I" on screen.
Note: Assuming that WORD.TXT does not contain any J alphabet otherwise.

"""


# def JTOI(filename):
#     try:
#         file = open(filename, "r")
#         data = file.read()
#         corrected_data = data.replace("J", "I")
#         print(corrected_data)
#         file.close()
#     except FileNotFoundError:
#         print("File not found!")


# JTOI("words.txt")


"""
There is a file having numbers in each line of that file. Calculate the
total of all numbers.

"""


# def total(filename: str) -> int:
#     try:
#         f = open(filename, "r")
#         total = 0
#         for line in f:
#             total += int(line.strip())

#         return total
#     except FileNotFoundError:
#         return -1
#     except ValueError:
#         return -2


# filename = "words.txt"
# tot = total(filename)
# if tot != -1 and tot != -2:
#     print(f"Total = {tot}")
# else:
#     print(tot)


"""
Print each word of the file in reverse order.

"""


def rever(filename: str):
    try:
        f = open(filename, "r")
        lines = f.readlines()
        f.close()

        for line in lines:
            words = line.strip().split()[::-1]
            final = " ".join(i[::-1] for i in words)
            print(final)
    except FileNotFoundError:
        print("File not found")


rever("hello.txt")
