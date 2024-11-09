# fibonacci series using recursion
"""
TC : O(2**N) very bad
"""


# def fib(num):
#     if num == 1:
#         return 1
#     if num == 0:
#         return 0
#     return fib(num - 1) + fib(num - 2)


# if __name__ == "__main__":
#     print(fib(20))


"""
another way using nested for loop
1
2 3
5 8 13
21 34 55 89
"""

# limit = 7

# num = 1
# next_num = 2

# for i in range(1, limit):
#     for j in range(1, i):
#         print(num, end=",")
#         temp = next_num
#         next_num += num
#         num = temp
#     print()
