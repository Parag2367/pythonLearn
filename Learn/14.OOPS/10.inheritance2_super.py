class Car:
    def __init__(self) -> None:
        self.color = input("Enter car color = ")
        self.type = input("Enter car type = ")
        self.mile = float(input("Enter mileage = "))
        self.seat_capacity = int(input("Enter seat capacity = "))

    def info(self):
        print(f"Color is {self.color}")
        print(f"Type is {self.type}")
        print(f"Mile is {self.mile}")
        print(f"Seat capacity is {self.seat_capacity}")


class Audi(Car):
    def __init__(self, city: str, electric: bool) -> None:
        super().__init__()  # this tells the class Audi to go to class Car and run the init method of that and then run below code
        self.city = city
        self.electric = electric

    def audi_info(self) -> None:
        print(f"City is {self.city}")
        print(f"Electric {self.city}")

    def full_info(self) -> None:
        self.info()
        self.audi_info()


c1 = Audi("Bhopal", True)
c1.full_info()


# c1 = Audi()
# c1.set_info("black", "Petrol", 15, 4)
# # c1.info()
# c1.audi_set_info("Mumbai", True)
# # c1.audi_info()
# c1.full_info()


# c1 = Car("Red", "Manual", 15.6, 5)
# c1.info()
