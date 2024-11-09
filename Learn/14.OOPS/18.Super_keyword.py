class GrandParent:
    def func1(self):
        print("i am func1 of grandparent")

    def func3(self):
        print("i am fun3 of parent you have called me inside")


class Parent(GrandParent):
    def func1(self):
        self.func3()
        super().func1()  # super always calls the parent class function which is mentioned usual if function name is same in parent and child
        print("i am func2 of parent")


obj = Parent()
obj.func1()
