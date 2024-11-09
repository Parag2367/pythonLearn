"""
Create a class called Employee with attributes such as name, age,
gender, and phone number. Implement a constructor to initialize these
attributes.
Include methods to calculate monthly and yearly salary based on hourly
rate and hours worked. Ask hourly rate and hours worked inside the
method (local variable).

"""

# class Employee:
#     def __init__(self) -> None:
#         self.name = input("Enter your name = ")
#         self.gender = input("Enter your gender = ")
#         self.phone = int(input("Enter your phone = "))

#     def salary(self, workinghours: int, days: list) -> None:
#         yearly_salary = 0
#         for a in days:
#             monthly_salary: float = a * workinghours * 600
#             yearly_salary: float = yearly_salary + monthly_salary
#             print(f"{monthly_salary = }")
#         print(f"{yearly_salary = }")


# e1 = Employee()
# e1.salary(8, [30, 28, 30, 31, 30, 29, 26, 24, 25])


"""
Design a class called Product with properties like name, price,
category, and quantity. Implement a constructor to initialize these
attributes.
Add methods to calculate the total price after applying a discount, ask
discount percent within that method.

"""


# class Product:
#     def __init__(self) -> None:
#         self.name = input("Enter product name = ")
#         self.price = float(input("Enter product price = "))
#         self.category = input("Enter product category = ")
#         self.quantity = int(input("Enter product quantity = "))

#     def discount(self, disc: float) -> None:
#         total_price = self.price * self.quantity
#         final = total_price - ((total_price * disc) / 100)
#         print(f"{final = }")


# p1 = Product()
# p1.discount(20)


"""
Employee Class with Performance Evaluation
"""


class Performance:
    def __init__(self, name: str, age: int, gender: str, phone: int, salary: float):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.salary = salary

    def change_salary(self):
        new_sal = float(input("Enter new salary = "))
        self.salary = new_sal

    def details(self):
        print(f"{self.name = }")
        print(f"{self.age = }")
        print(f"{self.gender = }")
        print(f"{self.phone = }")
        print(f"{self.salary = }")


p1 = Performance("Parag", 28, "Male", 78654, 100000)
p1.details()

print("----------------------")

p1.change_salary()
p1.details()
print(p1.salary)
