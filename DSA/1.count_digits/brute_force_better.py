# count number of digits:


def count_digit(num: int) -> int:
    return len(str(num))


"""
Time complexity : O(logn)
Space coplexity : O(1)

"""


def count_dig(num: int) -> int:
    count = 0
    n = num
    while n > 0:
        count += 1
        n = n // 10
    return count


print(count_dig(12345))
