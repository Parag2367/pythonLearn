class Student:
    # we are using __init__ method here which is known as initialiser, it will whatever we are asking when we are creating the object itself
    # we donot have to call for a specific function to create variables etc...

    # self.<variable_name> they are class variable, which can be accessed in the class
    def __init__(self):  # initialiser
        ph = 9998877  # this will be a local variable , which will be only accesible in __init__ function
        self.name = input("Enter name = ")
        self.age = int(input("Enter age = "))
        self.gender = input("Enter gender = ")

    def info(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"gender = {self.gender}")


s1 = Student()
print(s1.info())

print(s1.name)
