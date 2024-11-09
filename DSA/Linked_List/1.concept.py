class ABC:
    def __init__(self) -> None:
        self.value = None


class XYZ:
    def __init__(self) -> None:
        self.obj = None


A = ABC()
A.value = 200
print(A.value)


Z = XYZ()
print(Z.obj)

Z.obj = A
print(Z.obj)  # similar
print(A)  # similar
print(Z.obj.value)  # similar
