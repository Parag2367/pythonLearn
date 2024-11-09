class Father:
    def __init__(self) -> None:
        self.name = input("Enter your name = ")
        self.balance = int(input("Enter your bank balance = "))
        self.phone_model = input("Enter your phone model = ")

    def __str__(self) -> str:  # overriding the str method
        return f"this is a dunder method {self.name} has balance {self.balance}"

    def display(self):
        """Display all details related to banking"""  # docstring this will be the output of __doc__ documentation dunder method
        print(f"name is {self.name}")
        print(f"bank balance is {self.balance}")
        print(f"phone model is {self.phone_model}")

    def __len__(self):  ## __len__ dunder method it gives the output for len(obj)
        return 10


# when we print objec that we have created it will internally look for __str__ method, that is why it prints hexadecimal
# <__main__.Father object at 0x0000026BAFD6F090>
# we can change this by using one of the dunder method (__str__(self)) , we should always return something
# this is a dunder method
obj = Father()
print("-----------------------------------")
print(obj)
print("---------------------------")
obj.display()
print(obj.display.__doc__)  # it will print whatever is inside """ """ for this method
print(len(obj))

#####
"""docstring , whatever is wriiten in this will be the output of dunder method __doc__"""
"""
__doc__ dunder method: it gives documentation of object/function
"""
import random

print(random.__doc__)
