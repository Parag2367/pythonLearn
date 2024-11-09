"""
time complexity: O(sqrt n)
space complexity : O(sqrt n)

"""


def divisor(num: int) -> list:
    result = []
    n = num
    for a in range(1, int(n**0.5) + 1):
        if n % a == 0:
            result.append(a)
            if a != n // a:
                result.append(n // a)
    result.sort()
    return result


print(divisor(30))
