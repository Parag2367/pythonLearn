class Student:
    def __init__(self):
        self.name = input("Enter your name = ")
        self.age = int(input("Enter your age = "))
        self.physics = int(input("Enter physics marks = "))
        self.maths = int(input("Enter maths marks = "))
        self.chemistry = int(input("Enter chemistry marks = "))

    def info(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
        print(f"Physics marks is {self.physics}")
        print(f"Maths marks is {self.maths}")
        print(f"Chemistry marks is {self.chemistry}")

    def chnage_name(self, new_name: str):
        self.name = new_name

    def updateMarks(self, physics=None, maths=None, chemistry=None):
        if physics:
            self.physics = physics
        elif maths:
            self.maths = maths
        elif chemistry:
            self.chemistry = chemistry

    def getTotal(self) -> float:
        return self.physics + self.chemistry + self.maths


s1 = Student()
s1.info()
print("------------------")
s1.chnage_name("Parag")
print("------------------")
s1.info()
