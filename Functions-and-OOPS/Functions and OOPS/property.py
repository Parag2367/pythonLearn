class Student:
    def __init__(self, name, age, gender) -> None:
        self._name = name
        self._age = age
        self._gender = gender

    def __del__(self):
        print("Destructor called, Student deleted.")


s1 = Student("Anirudh", 100, "Male")
del s1
