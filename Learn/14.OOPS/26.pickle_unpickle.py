import pickle


class Student:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def display(self):
        print(f"name is {self.name}")
        print(f"age is {self.age}")


s = Student("Parag", 18)  # object
# print(s)  # it will print the object location not actual object
# print(s.name)


# Note: write always takes string datatype as input
# if we want to pt some other types of datatypes and want it to stick same way we should use pickle
# when we use pickle we should always use binary example('wb','rb')
# pickle.dump will always append the data

dict = {"name": "Parag", "Age": 30}
with open("test.txt", "wb") as f:
    pickle.dump(dict, f)  # pickle


with open("test.txt", "rb") as p:
    data = pickle.load(p)  # unpickle
    print(data)
    data.display()
    print(type(data))
