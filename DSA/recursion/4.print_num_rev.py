# without backtracking
def printn(i, n):
    if i < n:
        return
    print(i)
    printn(i - 1, n)


if __name__ == "__main__":
    printn(10, 1)


# with backtracking
def printnu(i, n):
    if i < n:
        return
    printn(i, n + 1)
    print(i)


printn(10, 1)


# self practice
def printnumrev(start, end):
    if start > end:
        return
    print(end)
    printnumrev(start, end - 1)


printnumrev(1, 10)


def printnumrevb(start, end):
    if start > end:
        return
    printnumrevb(start + 1, end)
    print(start)


printnumrevb(1, 10)
