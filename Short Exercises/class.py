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
        sideA = self.x2 - self.x if self.x2 > self.x else self.x - self.x2
        sideB = self.y2 - self.y if self.y2 > self.y else self.y - self.y2
        return sideA * sideB

    def coordinates(self):
        return [self.x, self.y, self.x2, self.y2]

    def perimeter(self):
        sideA = self.x2 - self.x if self.x2 > self.x else self.x - self.x2
        sideB = self.y2 - self.y if self.y2 > self.y else self.y - self.y2
        return 2 * (sideB) + 2 * (sideA)

    def __str__(self):
        return str([self.x, self.y, self.x2, self.y2])


rect = Rectangle(3, 9, 11, 3)

print(rect.coordinates())
print(rect.area())
print(rect.perimeter())
print(rect)

class SalesPerson(Person):
    def __init__(self, name, company, age, address):
        Person.__init__(self, name, age, address)
        self.company = company

    def getData(self):
        print("Name: " + str(self.name) + "\n" +
              "Company: " + str(self.company) + "\n" +
              "Age: " + str(self.age) + "\n" +
              "Address: " + str(self.address) + "\n")

laura = SalesPerson("Laura", "Wolkswagem", 22, "Bogota")
laura.getData()

class Animal():
    def __init__(self, name, food, characteristic):
        self.name = name
        self.characteristic = characteristic
        self.food = food
    def printer(self):
        print("I'm a " + str(self.name) + ".")


class Mammal(Animal):
    def __init__(self, name, food):
        Animal.__init__(self,name,food, "warm blooded")
    def printer(self):
        print("I'm warm blooded")


class Carnivore(Mammal):
    def __init__(self, name):
        Mammal.__init__(self, name, "meat")
    def printer(self):
        print("I eat meat")

lion = Carnivore("Lion")
lion.printer()


