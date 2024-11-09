a = 15


def change():
    global a
    a = 30
    print(a)


print(a)
change()
print(a)

"""
15
30
15
"""
