class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def getData(self):
        print("Name: " + str(self.name) + "\n" +
                "Age: " + str(self.age) + "\n" +
                "Address: " + str(self.address) + "\n")

a = Person("Sauron", 854, "Mordor")

a.getData()

print(a.address)