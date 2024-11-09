# Example of pass by value
# they are only passed as value so it will not be changed


def xyz(a: int):
    a = 100
    print(a)


a = 10
xyz(a)  # 100
print(a)  # 10 ( as it will give output of a = 10)


# Mutable objects (only List) are passed as
# pass by reference
# As mutable objects are passed by reference which means they are passed to memory of that variable that is why it will update


def xyz1(lst: list):
    lst[0] = 100


lst = [10, 20, 30, 40, 50]
xyz1(lst)
print(lst)

# finding id
b = 20
print(id(b))

c = "Parag"
print(id(c))

d = [10, 20, 30, 40, 50, 20]
print(id(d))
