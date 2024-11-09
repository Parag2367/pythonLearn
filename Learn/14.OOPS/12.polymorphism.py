# Many forms
# Method overriding
# here we can see method name is same but it has multiple forms
class Animal:
    def sound(self):
        print("This is Animal sound")


class Dog(Animal):
    def sound(self):
        print("Bhaw Bhaw Bhaw")


class Cat(Animal):
    def sound(self):
        print("Meow Meow Meow")


obj2 = Animal()
obj2.sound()
print("------------------------------")
obj = Dog()
obj.sound()
print("------------------------------")
obj1 = Cat()
obj1.sound()
