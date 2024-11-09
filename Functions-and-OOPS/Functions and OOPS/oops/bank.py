class Bank:
    def __init__(self) -> None:
        self.__balance = 0

    def display_balance(self):
        print(f"Your balance = {self.__balance}")


obj = Bank()
obj.display_balance()
obj.__balance = 100
obj.display_balance()
