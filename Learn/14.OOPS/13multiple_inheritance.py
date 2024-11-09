class Father:
    father_name = ""

    def display_fathername(self):
        print(f"{self.father_name}")


class Mother:
    mother_name = ""

    def display_mathername(self):
        print(f"{self.mother_name}")


class Child(Father, Mother):
    child_name = ""

    def display_childname(self):
        print(f"{self.child_name}")


c1 = Child()
c1.father_name = "vivek"
c1.mother_name = "sandhya"
c1.child_name = "parag"
c1.display_fathername()
c1.display_mathername()
c1.display_childname()
