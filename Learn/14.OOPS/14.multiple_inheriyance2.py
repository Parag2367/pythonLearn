class ABC:
    def func1(self):
        print("i am ABC func1")


class PQR:
    def func1(self):
        print("i am PQR func1")


class XYZ(PQR, ABC):
    def func(self):
        print("example of multiple inheritance")


obj = XYZ()
obj.func()
obj.func1()  # it will give priority to the first class which is passed to child
