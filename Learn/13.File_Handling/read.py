"""
read file
"""

# f = open("hello.txt", "r")
# print(f)

# # reading the contents of file
# a = f.read()
# print(a)


# f.close()  # this is necessary as we have to close the file always when we open

##################################
f = open("hello.txt", "r")
print(f)

# reading the contents of file , we can read characters, it act like a cursor
a = f.read(6)  # cursor has moved to 6
print(a)
b = f.read(6)  # cursor will start from 7 go till 6 more unless there are characters
print(b)


f.close()

# f.read()  # we cannot read file againg when it is closed, we have to open it


##################
