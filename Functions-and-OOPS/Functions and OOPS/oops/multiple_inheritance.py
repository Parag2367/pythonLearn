class Father:
    def __init__(self) -> None:
        print("FATHER INIT")

    father_name = ""

    def displayFatherName(self):
        print(self.father_name)


class Mother:
    def __init__(self) -> None:
        print("MOTHER INIT")

    mother_name = ""

    def displayMotherName(self):
        print(self.mother_name)


class Child(Father, Mother):
    def __init__(self) -> None:
        super().__init__()
        print("CHILD INIT")

    child_name = ""

    def displayChildName(self):
        print(self.child_name)


c1 = Child()
c1.father_name = "Sanjay"
c1.mother_name = "Muskan"
c1.child_name = "Anirudh"
c1.displayFatherName()
c1.displayMotherName()
c1.displayChildName()
