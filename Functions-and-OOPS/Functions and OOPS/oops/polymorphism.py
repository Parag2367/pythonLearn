# Many forms


class Animal:
    def sound(self):
        print("Animal speaking")


class Dog(Animal):
    def sound(self):
        print("BHaw bhaw bhaw")


class Cat(Animal):
    def sound(self):
        print("Meow meow meow")


obj = Dog()
obj.sound()
