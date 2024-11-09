class Father:
    def __init__(self) -> None:
        self.father_name = input("Enter father name = ")
        self._bank_balance = int(input("Enter father bank balance = "))
        self.__phone_model = input("Enter phone model = ")

    def __str__(self) -> str:
        return f"Father name = {self.father_name}\nFather bank balance = {self._bank_balance}\nFather phone model = {self.__phone_model}"


obj1 = Father()
obj2 = Father()
print("-------")
print(obj1)
print(obj2)
