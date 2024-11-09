from random import randint


class Bank:
    def __init__(self) -> None:
        # all these are created by initialiser and are class variables and can be used in the class
        self.account = randint(10000, 99999)
        self.name = input("Enter name = ")
        self.phone_no = int(input("Enter phone number = "))
        self.balance = 0

    def show_info(self) -> None:
        print(f"Account number = {self.account}")
        print(f"Name = {self.name}")
        print(f"Phone number = {self.phone_no}")
        print(f"Balance = {self.balance}\n")

    def show_balance(self) -> None:
        print("Your balance is ", self.balance)

    def withdraw(self) -> None:
        # this is a local variable and can be used in this function
        amount = int(input("Enter amount to withdraw = "))
        if amount > self.balance:
            print("Insufficient balance")

        else:
            self.balance = self.balance - amount
            print("your balance is ", self.balance)

    def deposit(self) -> None:
        # this is a local variablr and can be used in this function
        amount = int(input("Enter amount to deposit = "))
        self.balance = self.balance + amount


# it will call the initialiser function and will do that is written in __init__
# b1 = Bank()
# b1.show_balance()

# b1.deposit()
# b1.withdraw()


## Level up, Function list , solving the problem of creating object one by one

# banks = []
# x = Bank()  # new object
# banks.append(x)
# print(banks)


# x = Bank()  # it will overwrite
# banks.append(x)  # new object
# print(banks)

# banks[0].show_balance()
# banks[1].deposit()
# banks[1].show_balance()

# the above thing is creating a list of objects , but still we are creating one by one, so to overcome that make more optimized we use while loop


####################################

# while loop for object list

banks = []


# did this to check if account exists or not for transfer
# function
def account_check(acc_no: int):
    global banks
    for obj in banks:
        if obj.account == acc_no:
            return obj
    return None


while True:
    print("1. Create Bank Account")
    print("2. Show Bank Details")
    print("3. Deposit Amount")
    print("4. Withdrawl Amount")
    print("5. Transfer Amount")
    print("6. Exit")
    choice = int(input("Enter your choice = "))

    if choice == 1:
        obj = Bank()
        banks.append(obj)
        print(banks)

    elif choice == 2:
        if len(banks) == 0:
            print("No account has been created yet")
        else:
            for acc in banks:
                acc.show_info()

    elif choice == 3:  # this is for deposit
        acc_no = int(input("Enter account number = "))
        if len(banks) == 0:
            print("No account has been created yet")
        else:
            for obj in banks:
                if obj.account == acc_no:
                    obj.deposit()
                    break

    elif choice == 4:
        acc_no = int(input("Enter account no = "))
        if len(banks) == 0:
            print("No account has been created yet")
        else:
            for obj in banks:
                if obj.account == acc_no:
                    obj.withdraw()
                    break

    elif choice == 5:
        from_acc_no = int(input("Enter account no from we have to transfer = "))
        to_acc_no = int(input("Enter account no in which we have to deposit = "))

        from_acc_obj = account_check(from_acc_no)
        to_acc_obj = account_check(to_acc_no)

        if from_acc_obj != None and to_acc_obj != None:
            transfer_amt = int(input("Enter amount to transfer = "))
            if from_acc_obj.balance < transfer_amt:
                print("Insufficient Balance")

            else:
                from_acc_obj.balance = from_acc_obj.balance - transfer_amt
                to_acc_obj.balance = to_acc_obj.balance + transfer_amt
        else:
            print("Account does not exists")

    elif choice == 6:
        break
