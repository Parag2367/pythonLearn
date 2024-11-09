class Detail:
    def __init__(self):
        self.name = input("Enter your name =")
        self.__age = 15

    def get_age(self):
        print(f"age is {self.__age}")

    def set_age(self, age):
        self.__age = age
        print(f"age is {self.__age}")


obj = Detail()
obj.get_age()

obj.set_age(30)
