class Student:
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My gender is {self.gender}")

    @classmethod
    def create_student_using_params(cls, name, age, gender):
        obj = cls(name, age, gender)
        return obj

    @classmethod
    def create_student_using_file(cls, filename):
        f = open(filename, "r")
        student_data = f.read()
        name, age, gender = student_data.split()
        f.close()
        obj = cls(name, age, gender)
        return obj


s1 = Student.create_student_using_params("Anirudh", 18, "Male")
s1.display()
print("--------")
s2 = Student.create_student_using_file("student.txt")
s2.display()
