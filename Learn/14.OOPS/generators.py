# yield


def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


x = numbers()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

for i in numbers():
    print(i)
