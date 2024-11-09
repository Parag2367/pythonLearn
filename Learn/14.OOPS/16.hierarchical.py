class Parent:
    def func1(self):
        print("this is func1 of parent")


class Child1(Parent):
    def func2(self):
        print("This is func2 of child1")


class Child2(Parent):
    def func2(self):
        print("This is func2 of child2")


obj1 = Child1()
obj1.func2()
