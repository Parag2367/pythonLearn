# checking palindrome using recursion
# i: index


# def palindrome(string, i):
#     if i >= len(string) // 2:
#         return True
#     if string[i] != string[len(string) - i - 1]:
#         return False
#     return palindrome(string, i + 1)


"""
self practice
"""


def check(string, i):
    if len(string) == 1:
        return string
    if len(string) > 1:
        if i >= len(string) // 2:
            return True
        if string[i] != string[len(string) - i - 1]:
            return False
        return check(string, i + 1)


print(check("parapg", 8))
