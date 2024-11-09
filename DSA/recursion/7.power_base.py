"""
TC : O(p)
SC: O(p)
"""


# functional way
def result(b, p):
    if type(p) != int or p < 0:
        raise Exception("Inavlid power value")
    elif p == 0:
        return 1
    elif p == 1:
        return b
    return b * result(b, p - 1)


if __name__ == "__main__":
    print(result(5, 3))
