class Student:
    # Attributes
    # roll_no = 0
    # name = ""
    # age = 0
    # gender = ""

    # Methods (Functions inside a class are called Methods)
    # to access any attributes inside class we have to use 'self.<attribute_name>'

    """
    Note: Important!! We have to Write self for methods always in a class , it is syntax
    """

    def info(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Roll_no = {self.roll_no}")

    def set_info(self):
        self.name = input("Enter name = ")
        self.age = int(input("Enter age = "))
        self.gender = input("Enter gender = ")
        self.roll_no = int(input("Enter roll_no = "))


# explaination of attributes / accessing attributes
# s1 = Student()
# s2 = Student()

# print(s1)
# print(s1.age)
# print(s1.name)

# s1.name = "Parag"
# s1.age = 28
# print(s1.age)
# print(s1.name)

# print("----------------------")
# print(s2.roll_no)
# print(s2.age)


#########################################################
# explanation of methods / accessing methods

s1 = Student()  # object of class Student
s1.info()

print("-------------------------------")
s1.age = 28
s1.name = "Parag"
s1.roll_no = 33

s1.info()

#########################################
# earlier we were setting values for s1, by calling each attributes separately, so to make it more easier we can use a method

# s1 = Student()
# s2 = Student()

# s1.set_info()
# print("--------------------------------------")
# s2.set_info()

# s1.info()
# print("--------------------------------------")
# s2.info()
