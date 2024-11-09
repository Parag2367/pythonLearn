def add(n1, n2):
    total = n1 + n2
    return total


def check(num):
    if num % 2 == 0:
        print("Total is even")
    else:
        print("Total is odd")


# if we have use print for add() it would have given us none , we cannot use that value
s = add(20, 30)
check(s)
