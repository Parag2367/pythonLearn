# Static Methods
# Class Methods
from datetime import datetime


class Calender:
    def __init__(self) -> None:
        self.events = []

    def add_event(self, event_name):
        self.events.append(event_name)

    def display_events(self):
        print(f"Events = {self.events}")

    @staticmethod
    def is_weekend(date: datetime):
        if date.weekday() > 4:
            print("It is a weekend")
        else:
            print("It is a weekday")


obj1 = Calender()
obj1.add_event("party")
obj1.add_event("dsa")
obj1.add_event("coding")
obj1.display_events()

current_date = datetime.now()
Calender.is_weekend(current_date)
