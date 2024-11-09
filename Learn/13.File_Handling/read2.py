"""
readline : reads one line it will always give a string
"""

# f = open("hello.txt", "r")
# a = f.readline()  # this takes the cursor to start of the next line
# print(a)

# f.close()


"""
readlines : reads all the lines, it will give a list of different lines as element
"""

# doing withou using readlines : it will give us strings
# file = open("hello.txt", "r")
# for a in file:
#     print(a)

# file.close()

# Using readlines from here : it gives a list of each line as element

# f = open("hello.txt", "r")
# a = (
#     f.readlines()
# )  # it always gives the list in which each element is a line along with\n
# # this takes the cursor to start of the end of the last line
# print(a)

# f.close()


"""
print len()
"""
# f = open("hello.txt", "r")
# a = f.readlines()
# print(len(a))

# f.close()


"""
how many words
"""
# f = open("hello.txt", "r")
# lines = f.readlines()

# count = 0
# for line in lines:
#     words = line.strip().split()
#     # words will have [word1,word2,word3] on each line
#     # strip will remove the spaces,\n from start and begining and split will convert it to list of words
#     count = count + len(words)
# print(count)

# f.close()


"""
how many characters
"""

# f = open("hello.txt", "r")
# x = f.read()

# count = 0

# for ch in x:
#     if ch != " " and ch != "\n":
#         count += 1
# print(count)


# f.close()


"""
change trhe order of words in each line
"""

# f = open("hello.txt", "r")

# lines = f.readlines()
# for line in lines:
#     words = line.strip().split()[::-1]
#     final = " ".join(words)
#     # print(" ".join(i for i in words))
#     print(final)


# f.close()


"""
merge two files
"""


data = data2 = ""

with open("student.txt", "r") as file1:
    data = file1.read()

with open("student_data.txt", "r") as file2:
    data2 = file2.read()

data = data + "\n"
data = data + data2

with open("file3.txt", "w") as fil:
    fil.write(data)
