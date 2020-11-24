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

class Rectangle:

    def __init__(self, x, y, x2, y2):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2

    def area(self):
        sideA = self.x2 - self.x
        sideB = self.y2 - self.y
        return sideA * sideB

    def cordinates(self):
        return list(self.x, self.y, self.x2, self.y2)

    def perimeter(self):
        sideA = self.x2 - self.x
        sideB = self.y2 - self.y
        return 2 * (sideB) + 2 * (sideA)
