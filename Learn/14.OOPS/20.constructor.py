class Company:
    def __init__(self):
        self._project = "video calling app"
        print("i am a constructor of company")


class Emp(Company):
    def __init__(self, name):
        self.name = name
        print("i am a constructor of employee")
        super().__init__()


obj1 = Emp("Parag")
print(
    obj1._project
)  # as it is protected , we can still access it, But for the developers it is there
# it is not at all strict
