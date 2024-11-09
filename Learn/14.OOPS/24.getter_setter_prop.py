class Detail:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        print("GETTER METHOD CALLED")
        return self.__age

    @age.setter
    def age(self, newage):  # Note : ghetter and setter are only for one arguments
        # TypeError: age() missing 1 required positional argument: 'abc'
        #
        self.__age = newage
        print("setter method called")
        return self.__age


obj = Detail("parag", 30)
print(obj.age)

obj.age = 25
print(obj.age)
