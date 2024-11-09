from random import randint


class Bank:
    def __init__(self) -> None:
        self.account = randint(100000, 999999)
        self.full_name = input("Enter name = ")
        self.phone_number = int(input("Enter phone number = "))
        self.balance = 0

    def show_info(self):
        print(f"Accout number = {self.account}")
        print(f"Full name = {self.full_name}")
        print(f"Balance = {self.balance}\n")

    def show_balance(self) -> None:
        print(f"Current balance = {self.balance}")

    def withdraw(self) -> None:
        amount = int(input("Enter amount to withdraw = "))
        if amount > self.balance:
            print("Insufficient balance")
        else:
            # self.balance = self.balance - amount
            self.balance -= amount

    def deposit(self) -> None:
        amount = int(input("Enter amount to deposit = "))
        self.balance = self.balance + amount


banks = []  # Pickle
# FILE READ


def check_account_exists(acc_no: int):
    global banks
    for obj in banks:
        if obj.account == acc_no:
            return obj
    return None


while True:
    print("1. Create account")
    print("2. Show all bank details")
    print("3. Deposit amount")
    print("4. Withdraw amount")
    print("5. Transfer amount")
    print("6. Exit")
    choice = int(input("Enter choice = "))
    if choice == 1:
        obj = Bank()
        banks.append(obj)
        print(banks)
    elif choice == 2:
        if len(banks) == 0:
            print("No accounts have been created yet")
        else:
            for account in banks:
                account.show_info()
    elif choice == 3:
        if len(banks) == 0:
            print("No accounts have been created yet")
        else:
            acc_no = int(input("Enter account number to deposit = "))
            for obj in banks:
                if obj.account == acc_no:
                    obj.deposit()
                    break
    elif choice == 4:
        if len(banks) == 0:
            print("No accounts have been created yet")
        else:
            acc_no = int(input("Enter account number to withdraw = "))
            for obj in banks:
                if obj.account == acc_no:
                    obj.withdraw()
                    break
    elif choice == 5:
        from_acc_no = int(
            input("Enter account number from which you want to transfer = ")
        )
        to_acc_no = int(input("Enter account number to which you want to transfer = "))
        from_acc_obj = check_account_exists(from_acc_no)
        to_acc_obj = check_account_exists(to_acc_no)
        if from_acc_obj != None and to_acc_obj != None:
            transfer_amount = int(input("Enter transfer amount = "))
            if from_acc_obj.balance < transfer_amount:
                print("Insuffcient balance")
            else:
                from_acc_obj.balance -= transfer_amount
                to_acc_obj.balance += transfer_amount
        else:
            print("Account does not exists")

    elif choice == 6:
        break
    else:
        print("Invalid Choice")
