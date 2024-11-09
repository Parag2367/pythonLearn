"""


"""


def checkprime(num: int) -> bool:
    count = 0
    for a in range(2, int(num**0.5) + 1):
        if num % a == 0:
            count += 1
    if count > 0:
        return False
    return True


def check_prime(num: int) -> bool:
    if num % 2 == 0 or num % 3 == 0:  # excxept 2 or 3
        return False
    else:
        return True


print(checkprime(12))
