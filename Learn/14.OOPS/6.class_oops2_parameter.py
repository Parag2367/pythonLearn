class Student:
    def __init__(self):
        self.name = input("Enter your name = ")
        self.marks = {"physics": 88, "maths": 78, "chemistry": 89}

    def addWithParam(self, new_marks, new_subject):
        if new_subject in self.marks:
            print("Subject is already added")
            return

        self.marks[new_subject] = new_marks

    def addWithoutParam(self):
        new_subject = input("Enter new subject to add = ")
        new_marks = int(input(f"Enter marks for {new_subject} = "))

        self.marks[new_subject] = new_marks

    def updateMarks(self):
        subject = input("Enter subject name to update = ")
        if subject in self.marks:
            mark = int(input("Enter marks"))
            self.marks.update({subject: mark})
        else:
            print("Subject is not added please add !!")
            self.addWithoutParam()

    def display(self):
        for subject, marks in self.marks.items():
            print(f"{subject = } : {marks = }")


s1 = Student()
# s1.updateMarks()
s1.display()
