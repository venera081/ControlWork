class Person:
    def __init__(self):
        self.__age = None

    def set_age(self, age):
        if age < 0:
            raise ValueError("Возраст не должен быть отрицательным")
        self.__age = age

    def get_age(self):
        return self.__age


p = Person()
p.set_age(16)
print(p.get_age())

# p.set_age(-1)





print("-----------------")



class Animal():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return"I am an animal"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"


dog = Dog("Buddy")
cat = Cat("Kitty")
print(dog.name, dog.speak())
print(cat.name, cat.speak())




print("-----------------")




class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

def move(vehicle):
    return vehicle.move()



car = Car()
bike = Bicycle()
print(move(car))
print(move(bike))





print("-----------------")





from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pi = 3.14
        return pi * self.radius ** 2


rect = Rectangle(12, 4)
circle = Circle(5)
print(rect.area())
print(circle.area())



