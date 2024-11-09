"""
Time complexity : O(logn)
space complexity = O(1)
"""


def reverse(num: int) -> int:
    n = num  # this is the space that we are using
    reversed_number = 0  # constant
    while n > 0:
        last_digit = n % 10  # constant
        reversed_number = (reversed_number * 10) + last_digit

        n = n // 10
    return reversed_number


print(reverse(12345))
