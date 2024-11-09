class Parent1:
    def func1(self):
        print("this is func1 of parent1")


class Parent2:
    def func2(self):
        print("this is func2 of parent2")


class Child1(Parent1):
    def func3(self):
        print("This is func3 of child1")


class Child2(Child1, Parent2):
    def func4(self):
        print("This is func4 of child2")


obj = Child2()
obj.func4()
