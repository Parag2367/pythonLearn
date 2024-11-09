from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def sound(self):
        print("abc")
        pass


class Audi(Car):
    def __init__(self, engine) -> None:
        self.engine = engine

    def sound(self):
        print("SPORTS SOUND")


# obj = Audi("1200cc")
# obj.sound()
obj = Car()
