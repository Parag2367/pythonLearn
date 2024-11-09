class Car:
    def __init__(self) -> None:
        self.color = input("Enter car color = ")
        self.type = input("Enter type = ")
        self.mileage = float(input("Enter mileage = "))
        self.seat_capacity = int(input("Enter seat capacity = "))

    def base_info(self):
        print(f"color = {self.color}")
        print(f"type = {self.type}")
        print(f"mileage = {self.mileage}")
        print(f"seat_capacity = {self.seat_capacity}")


class Audi(Car):
    def __init__(self) -> None:
        super().__init__()
        self.electric = input("Enter electric = ")
        self.city = input("Enter city = ")

    def audi_info(self):
        print(f"Electric = {self.electric}")
        print(f"City = {self.city}")

    def show_full_info(self):
        self.base_info()
        self.audi_info()


c1 = Audi()
# c1.base_info()
# c1.audi_info()
print("----------")
c1.show_full_info()
