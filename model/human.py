class Human:

    def __init__(self, name, surname, age):
        print("constructor from Human class")
        self.name = name
        self.surname = surname
        self.age = age

    def run(self):
        print(f"Human {self.name} is running", end=" ")