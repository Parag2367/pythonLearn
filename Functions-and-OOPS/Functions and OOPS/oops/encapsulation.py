# Access modifiers
# Public, Protected, Private
from random import randint


class Bank:
    def __init__(self) -> None:
        self.name = input("Enter name = ")
        self.__account_no = randint(100000, 999999)
        self.__balance = 0

    def displayBalance(self):  # getter
        print(self.__balance)

    def setBalance(self, newAmount):  # setter
        self.__balance = newAmount

    def display(self):
        print(f"Account number = {self.__account_no}")
        print(f"Name = {self.name}")
        print(f"Balance = {self.__balance}")


obj = Bank()
obj.display()
print("---------")
print(obj._Bank__balance)  # Never do this, name mangling
