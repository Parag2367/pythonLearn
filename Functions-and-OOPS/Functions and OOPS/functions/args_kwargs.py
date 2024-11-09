def add(n1, n2, n3, *args, **kwargs):
    print(f"{n1=}")
    print(f"{n2=}")
    print(f"{n3=}")
    print(f"{args=}")
    print(f"{kwargs=}")
    print(f'{kwargs["name"]=}')


add(5, 10, 15, 100, 200, 300, name="Anirudh")
# add([1, 2], [100, 200], 45, 100)
# add(1, 2, 3)
# add(100, 5, 8, 7, 4, 9)
# add(12, 24)
