from datetime import datetime


class Calendar:
    def __init__(self):
        self.events = []

    def add_events(self, event):
        self.events.append(event)

    def display(self):
        print(f"Events are {self.events}")

    # static methods
    @staticmethod
    def weekend(date: datetime):
        if date.weekday() > 4:
            print("It is Weekend")
        else:
            print("It is Weekday")


obj1 = Calendar()
obj1.add_events("party")
obj1.add_events("python")
obj1.add_events("sql")

obj1.display()
print("-------------------------")

## weekend is a staticmethod , it does not use self , as it is not dependent on class variable ,
# it is just a independent method of Calendar class , it can be called like Calendar.weekend , object is not required
current_date = datetime.now()
Calendar.weekend(current_date)
