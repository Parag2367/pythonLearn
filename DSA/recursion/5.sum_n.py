"""
Two ways:
1.Parameterized way : No return
2. Function way : return is used

"""

# Parameterized way
# def addn(i, sum):
#     if i < 1:
#         print(sum)
#         return
#     addn(i - 1, sum + i)


# if __name__ == "__main__":
#     addn(5, 0)


# # Functional way
# def add(num):
#     if num == 1:
#         return 1
#     return num + add(num - 1)


# if __name__ == "__main__":
#     print(add(5))


"""
self practice
"""
# def add(num, sum):
#     if num < 1:
#         print(sum)
#         return
#     add(num - 1, sum + num)


# add(5, 0)


# def addf(num):
#     if num == 0:
#         return 0
#     if num > 0:
#         if num == 1:
#             return 1
#         return num + addf(num - 1)
#     if num < 0:
#         if num == -1:
#             return -1
#         return num + addf(num + 1)


# print(addf(-5))
