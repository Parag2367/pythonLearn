"""

"""


def check_prime(num: int) -> bool:
    count = 0
    for a in range(1, num + 1):
        if num % a == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


print(check_prime(7))
