class GrandParent:
    def func1(self):
        print("i am func1 of grandparent")


class Parent(GrandParent):
    def func2(self):
        print("i am func2 of parent")


class Child(Parent):
    def func3(self):
        print("i am func3 of child")


obj = Child()
obj.func3()
obj.func1()
obj.func2()
