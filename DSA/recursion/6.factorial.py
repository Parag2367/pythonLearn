"""
two ways:
parameterized, functional way
"""


# parameterized
def facto(i, fact=1):
    if i < 1:
        print(fact)
        return
    facto(i - 1, fact * i)


if __name__ == "__main__":
    facto(5)


# functional way
def factf(num):
    if num == 0 or num == 1:
        return 1
    return num * factf(num - 1)


if __name__ == "__main__":
    print(factf(5))
