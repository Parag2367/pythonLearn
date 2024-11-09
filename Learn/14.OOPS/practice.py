from random import randint

# bank: account,info,deposit,withdrawl,transfer


class Bank:
    def __init__(self) -> None:
        self.account_no = randint(10000, 50000)
        self.name = input("Enter your name = ")
        self.phone_no = int(input("Enter your phone_no = "))
        self.balance = 0

    def info(self) -> None:
        print("Account Details")
        print("--------------------------")
        print(f"name is {self.name}")
        print(f"Your phone_no is {self.phone_no}")
        print(f"Your account number is {self.account_no}")
        print(f"your balance is {self.balance}")

    def show_balance(self, account) -> None:
        self.account_no = account
        print(f"Your balance is {self.balance}")

    def deposit(self) -> None:
        amt = int(input("Enter amount you want to deposit = "))
        self.balance = self.balance + amt
        print(f"Your balance now is {self.balance}")

    def withdraw(self) -> None:
        amt = int(input("Enter the amount that you want to withdraw = "))
        if amt > self.balance:
            print("Insufficient Balance")
        else:
            self.balance = self.balance - amt
            print(f"Your balance now is {self.balance}")


banks = []


# checking account number
def account_check(acc: int):
    global banks
    for obj in banks:
        if obj.account_no == acc:
            return obj
    return None


while True:
    print("1. Create Bank Account")
    print("2. Show Details")
    print("3. Deposit")
    print("4. Withdrawl")
    print("5. Show Balance")
    print("6. Transfer")
    print("7. Exit")
    choice = int(input("Enter your choice = "))

    if choice == 1:
        obj = Bank()
        banks.append(obj)
        print(banks)
        obj.info()

    elif choice == 2:
        if len(banks) == 0:
            print("No account has been created")
        else:
            for obj in banks:
                obj.info()

    elif choice == 3:
        acc = int(input("Enter your account number = "))
        acc1 = int(input("Please re-enter your account number = "))
        if len(banks) == 0:
            print("No account has been created yet")
        elif acc == acc1:
            for obj in banks:
                if obj.account_no == acc:
                    obj.deposit()
                    break
        else:
            print("Account number did not matched")

    elif choice == 4:
        acc = int(input("Enter your account number = "))
        acc1 = int(input("Please re-enter your account number = "))
        if len(banks) == 0:
            print("No account has been created yet")
        elif acc == acc1:
            for obj in banks:
                if obj.account_no == acc:
                    obj.withdraw()
                    break
        else:
            print("Account number did not matched")

    elif choice == 5:
        acc = int(input("Enter your account number = "))
        if len(banks) == 0:
            print("No account has been created now")
        else:
            for obj in banks:
                if obj.account_no == acc:
                    obj.show_balance(acc)
                    break
    elif choice == 6:
        send_acc_no = int(input("Enter sender's account number = "))
        rec_acc_no = int(input("Enter reciever's account number = "))

        sender = account_check(send_acc_no)
        reciever = account_check(rec_acc_no)
        if sender != None and reciever != None:
            amt = int(input("Enter amount to transfer = "))
            if amt > sender.balance:
                print("insufficient funds")
            else:
                sender.balance = sender.balance - amt
                reciever.balance = reciever.balance + amt
        else:
            print("Please check the account number entered")

    elif choice == 7:
        break
