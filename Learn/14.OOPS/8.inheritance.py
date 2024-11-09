class Car:
    def __init__(self, color: str, type: str, mile: float, seat_capacity: int) -> None:
        self.color = color
        self.type = type
        self.mile = mile
        self.seat_capacity = seat_capacity

    def info(self):
        print(f"Color is {self.color}")
        print(f"Type is {self.type}")
        print(f"Mile is {self.mile}")
        print(f"Seat capacity is {self.seat_capacity}")


class Audi(Car):
    def __init__(self):
        print("Audi is here")


c1 = Audi()
c1.color = "Black"
c1.mile = 12.2
c1.seat_capacity = 6
c1.type = "Diesel"

c1.info()

# c1 = Car("Red", "Manual", 15.6, 5)
# c1.info()
