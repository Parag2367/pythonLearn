class Student:
    # Methods
    def __init__(self):  # Initializer
        ph = 100000
        self.name = input("Enter name = ")
        self.age = int(input("Enter age = "))
        self.gender = input("Enter gender = ")
        self.roll_no = int(input("Enter roll number = "))

    def info(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")


s1 = Student()
s1.info()

s2 = Student()
s2.info()
