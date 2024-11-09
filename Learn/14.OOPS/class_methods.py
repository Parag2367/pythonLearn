class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"name is {self.name}")
        print(f"age is {self.age}")
        print(f"gender is {self.gender}")

    ## class methods
    # it will also not take self , it will take cls and other parameter
    # we should always return in this method
    @classmethod
    def create_student_using_params(cls, name, age, gender):
        obj = cls(name, age, gender)
        return obj

    @classmethod
    def create_student_using_file(cls, filename):
        f = open(filename, "r")
        data = f.read()
        name, age, gender = data.split()
        f.close()
        obj = cls(name, age, gender)
        return obj


# this is how we create a instance of class which have a class method, unlike normally(s1 = Student())
s1 = Student.create_student_using_params("Parag", 18, "male")
s1.display()

print("------------------------")

s2 = Student.create_student_using_file("file.txt")
s2.display()
