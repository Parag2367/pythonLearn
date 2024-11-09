class Student:
    # Attributes
    # roll_no = 0
    # name = ""
    # age = 0
    # gender = ""

    # Methods (Functions inside a class are called Methods)
    # to access any attributes inside class we have to use 'self.<attribute_name>'

    # we have to write self for methods always in a class , it is syntax
    def info(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Roll_no = {self.roll_no}")

    def set_info(self):
        # self.name is creating a class variable, so we need not mention attributes on top for that
        self.name = input("Enter name = ")
        self.age = int(input("Enter age = "))
        self.gender = input("Enter gender = ")
        self.roll_no = int(input("Enter roll_no = "))


# if we call set_info first , the class variables will be created that is why no error

s1 = Student()
s1.set_info()
s1.info()

# but if we call info first it will give error, because in that class variables are not created

s2 = Student()
s2.info()
