"""
Objective:
Your task is to create a Python class to manage student information. The
class should have attributes for the student's name, age, gender, and a list
of marks. Additionally, you need to implement various methods to
manipulate and display this information.

"""


class Student:
    def __init__(self, name: str, age: int, gender: str, marks: list):
        self.name = name
        self.age = age
        self.gender = gender
        self.marks = marks

    def displayAllInfo(self):
        print(f"{self.name = }")
        print(f"{self.age = }")
        print(f"{self.gender = }")
        print(f"{self.marks = }")

    def onlyMarks(self):
        for a in self.marks:
            print(a, end=" ")
        print()

    def getTotal(self):
        total = 0
        for a in self.marks:
            total += a
        print(f"Total marks are {total}")

    def getMax(self):
        maxx = self.marks[0]

        for a in self.marks:
            if a > maxx:
                maxx = a
        print(maxx)

    def getMin(self):
        minn = self.marks[0]

        for a in self.marks:
            if a < minn:
                minn = a
        print(minn)

    def getAvg(self):
        total = 0
        cnt = 0

        for a in self.marks:
            total += a
            cnt += 1

        print(total / cnt)

    def addMark(self, mark):
        self.marks.append(
            mark
        )  # for append we dont need to store it in a new parameter
        print(self.marks)

    def removeMark(self):
        self.marks.pop()
        print(self.marks)


# s1 = Student("Parag", 29, "Male", [44, 55, 66, 77])

# s1.displayAllInfo()
# s1.onlyMarks()
# s1.getTotal()
# s1.getMax()
# s1.getMin()
# s1.getAvg()
# s1.addMark(88)
# s1.removeMark()


"""
Your task is to create a Python class to manage bank accounts. The class
should have attributes for the account holder's name, account number,
balance, and account type. Additionally, you need to implement various
methods to manipulate and display this information.
"""

from random import randint
from typing import List


class Bank:
    def __init__(self):
        self.name = input("Enter account holder name = ").title()
        self.account_num = randint(10000, 999999)
        self.balance = 100
        self.type = input("Enter your account type = ").lower()

    def displayAllInfo(self):
        print(f"Account holder name : {self.name}")
        print(f"Account number : {self.account_num}")
        print(f"current balance : {self.balance}")
        print(f"Account type : {self.type}")

    def deposit(self, amt: float):
        self.balance += amt
        print(f"Your balance is {self.balance}")

    def withdraw(self, amt: float):
        if amt > self.balance:
            print("Not sufficient balance")
        else:
            self.balance -= amt
            print(f"Your balance is {self.balance}")

    def getBalance(self):
        print(f"Your balance is {self.balance}")


accounts: List[Bank] = []

while True:
    print(
        """
          1.Add Account
          2.Display all accounts
          3.Search accounts
          4.Get Balance
          5.Deposit
          6.Withdraw
          7.Exit"""
    )

    choice = int(input("Enter your choice = "))

    if choice == 1:
        obj = Bank()
        accounts.append(obj)
        print("Account created")
        obj.displayAllInfo()

    elif choice == 2:
        if len(accounts) == 0:
            print("No accounts have been created yet")
        else:
            for a in accounts:
                a.displayAllInfo()

    elif choice == 3:
        acct = int(input("Enter account number"))
        for a in accounts:
            if a.account_num == acct:
                a.displayAllInfo()
                break  # this will break out of for loop only
        else:  # this will only run when for loop is ended
            print("No account found")

    elif choice == 5:
        acct = int(input("Enter account number = "))
        for a in accounts:
            if a.account_num == acct:
                amt = int(input("Enter amount to deposit = "))
                a.deposit(amt)
                break
        else:
            print("No account found")

    elif choice == 7:
        break
