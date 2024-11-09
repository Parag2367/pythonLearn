"""

"""

# without backtracking:


# def print_num(i, n):
#     if i > n:
#         return
#     print(i)
#     print_num(i + 1, n)


# if __name__ == "__main__":
#     print_num(1, 3)


# # with backtracking


# def print_num_back(i, n):
#     if i < 1:
#         return
#     print_num_back(i - 1, n)
#     print(i)


# print_num_back(5, 5)


# self practice
# def printnum(start, end):
#     if start > end:
#         return
#     print(start)
#     printnum(start + 1, end)


# printnum(1, 10)


def printnumb(start, end):
    if start > end:
        return
    printnumb(start, end - 1)
    print(end)


printnumb(1, 10)
