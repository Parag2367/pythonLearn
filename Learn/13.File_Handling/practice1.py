"""
student and student-data
"""

# with open("student.txt") as file:
#     roll_no = file.read().split()
#     print(roll_no)

# with open("student_data.txt") as file:
#     data = file.readlines()
#     for a in roll_no:
#         for line in data:
#             roll, details = line.strip().split("-")
#             if a == roll:
#                 print(details)


"""
Make a function named copyFileContent which takes 2 filenames
(filename1, filename2) as an argument. Copy the content of filename1 to
filename2.
"""


def copyFile(filename1: str, filename2: str):
    try:
        with open(filename2, "r") as file2:
            data = file2.read()
        with open(filename1, "w") as file1:
            file1.write(data)
    except FileNotFoundError:
        print("file not found")


copyFile("student.txt", "student_data.txt")


"""
There is a file named numbers.txt and the content is given below.
Content (numbers.txt)
Create another file named numbers_result.txt. It should have the following
content in it based on numbers.txt.

"""


# def result(filename1: str, filename2: str):
#     try:
#         with open(filename1, "r") as file:
#             data = file.read()
#         with open(filename2, "w") as file:
#             number = data.split()
#             for a in number:
#                 if int(a) % 2 == 0:
#                     a = a + " EVEN" + "\n"
#                     file.write(a)
#                 else:
#                     a = a + " ODD" + "\n"
#                     file.write(a)
#     except FileNotFoundError:
#         print("File not found error")


# result("number.txt", "number_result.txt")


"""
. Create a function named multiplication which takes 2 parameter which
are filename and a number. Write the multiplication table of that number
"""


# def table(filename: str, number: int):
#     try:
#         with open(filename, "w") as file:
#             for i in range(1, 11):
#                 file.write(f"{number} * {i} = {number*i} \n")
#     except FileNotFoundError:
#         print("File not found")


# table("table5.txt", 5)


"""
Write a Python program to read last n lines of a file. Ask n from user
and read any file you want to. If n is greater than number of lines actually
present in that file, show output like “Not Enough Lines”.

"""


# def lastn(filename: str, number: int):
#     try:
#         with open(filename, "r") as file:
#             data = file.readlines()
#             print(len(data))
#             if len(data) > number:
#                 result = data[-number:]
#                 print("".join(i for i in result))
#             else:
#                 print("not enough lines")

#     except:
#         print("some other error occured")


# lastn("hello.txt", 3)


# def lastn(filename: str):
#     try:
#         with open(filename, "r") as file:
#             data = file.readlines()
#             result = data[::-1]
#             print("".join(i for i in result))

#     except:
#         print("some other error occured")


# lastn("hello.txt")
