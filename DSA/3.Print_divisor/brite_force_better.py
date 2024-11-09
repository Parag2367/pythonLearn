"""
Time complexity: O(n)
space complexity: O(d) d is the number of divisors as space depends on divisors

"""


def divisor(num: int):
    mylist = []
    n = num
    for a in range(1, num + 1):
        if n % a == 0:
            mylist.append(a)
    return mylist


print(divisor(30))
