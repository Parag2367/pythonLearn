from random import randint


class Bank:
    def __init__(self):
        self.name = input("Enter your name = ")
        self.__account_no = randint(
            10000, 50000
        )  # Private :"__<variable_name> access modifier"
        self.__balance = 0

    def displaybalance(self):  # getter we write them as get_<name>
        print(f"balance is {self.__balance}")

    def setBalance(self, newAmount):  # setter we write them as set_<name>
        self.__balance = newAmount

    def show_info(self):
        print(f"Name is {self.name}")
        print(f"Account Number is {self.__account_no}")
        print(f"Balance is {self.__balance}")


b1 = Bank()
b1.show_info()
print("-------------------------------")
b1.__balance = 2  # here we can access the balance variable ,
# but it is wrong as we can easily manupulate it, so to put an access limit to sensitive variables we will use access modifiers

# after using access modifier(Private "__") we see that the class variables cannot be change
print(b1.__dict__)  # just a way to print obj in dict
# print(b1._Bank__balance) # name mangling this way we can access protected as well
print("---------------------------------------")
b1.setBalance(10000)
b1.show_info()


### We should never do this , this way we can access private and protected variables
# print(b1._Bank__balance)
