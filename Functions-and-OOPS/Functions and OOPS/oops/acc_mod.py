# Protected


class Father:
    def __init__(self) -> None:
        self.father_name = input("Enter father name = ")
        self._bank_balance = int(input("Enter father bank balance = "))
        self.__phone_model = input("Enter phone model = ")

    def displayFather(self):
        print(f"Father name = {self.father_name}")
        print(f"Father bank balance = {self._bank_balance}")
        print(f"Father phone model = {self.__phone_model}")


class Child(Father):
    def __init__(self) -> None:
        super().__init__()
        self.child_name = input("Enter child name = ")

    def displayChildInfo(self):
        print(f"Child name = {self.child_name}")
        print(f"My father has {self._bank_balance} amount")


child = Child()
child.displayChildInfo()
