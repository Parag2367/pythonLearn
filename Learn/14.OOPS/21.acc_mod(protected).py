# Protected, Private , Public(default)  : they are not strict, we can access them outside


class Father:
    def __init__(self):
        self.name = input("Enter your Father's name = ")
        self._bank_balance = int(
            input("Enter your bank balance = ")
        )  # Protected access modifiers
        self.__phone_model = input("Enter your phone model = ")

    def display(self):
        print(f"Name is {self.name}")
        print(f"Balance is {self._bank_balance}")  # Protected access modifiers
        print(f"Phone model is {self.__phone_model}")


class Child(Father):
    def __init__(self):
        super().__init__()
        self.childname = input("Enter your name = ")

    def displaychild(self):
        print(f"name is {self.childname}")
        print(
            f"My father's balance is {self._bank_balance}"
        )  # this will print as it is Protected
        # print(f"My father's phone model is {self.__phone_model}")
        # this will give error as __phone_model is private which is only available to its class only not even child class


abc = Child()
abc.displaychild()
