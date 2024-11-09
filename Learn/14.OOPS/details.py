class Father:
    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
        self.phone_model = input("Enter your phone model = ")

    def __str__(self) -> str:  # overriding the str method
        return f"this is a dunder method {self.name} has balance {self.balance}"

    def __add__(
        self, other: "Father"
    ) -> float:  # we have called a class inside a class as an parameter
        total = self.balance + other.balance
        return total

    def display(self):
        """Display all details related to banking"""  # docstring this will be the output of __doc__ documentation dunder method
        print(f"name is {self.name}")
        print(f"bank balance is {self.balance}")
        print(f"phone model is {self.phone_model}")

    def __len__(self):  ## __len__ dunder method it gives the output for len(obj)
        return 10


if __name__ == "__main__":
    obj1 = Father("parag", 20000)
    obj2 = Father("ram", 20000)

    print(obj1.balance + obj2.balance)

    # adding two objects of a class uses a dunder method

    print(obj1 + obj2)  # we will have to define a add dunder method for objects
