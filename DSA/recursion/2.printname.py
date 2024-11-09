# recursion tree
"""
TC: O(n)
SC: O(n)
"""


# without backtracking
def pri(i, n):
    if i > n:
        return
    print("Parag")
    pri(i + 1, n)


if __name__ == "__main__":
    pri(1, 3)


# self_practice
# def name(i, n):
#     if i > n:
#         return
#     print("Parag")
#     name(i + 1, n)


# name(1, 5)


# with backtracking:
# def nameb(i, n):
#     if i > n:
#         return
#     nameb(i + 1, n)
#     print("parag")


# nameb(1, 5)
