# reversing array


# def reverse(string, length):
#     if length < 1:
#         return ""

#     # Base case
#     if length == 1:
#         return string[0]

#     return string[length - 1] + reverse(string, length - 1)


# if __name__ == "__main__":
#     input_str = "Geeks for geeks"
#     print(reverse(input_str, len(input_str)))


"""
self practice
"""


def rev(string, length):
    if length < 1:
        return ""
    if length == 1:
        return string[0]
    return string[length - 1] + rev(string, length - 1)


if __name__ == "__main__":
    string = "code and debug"
    length = len(string)
    print(rev(string, length))
