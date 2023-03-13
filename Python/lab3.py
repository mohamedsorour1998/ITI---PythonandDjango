# Question 1:
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Example usage
rect = Rectangle(4, 5)
print(rect.area())  # Output: 20
# Question 2:

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius

# Example usage
circ = Circle(2)
print(circ.circumference())  # Output: 12.566370614359172
# Question 3:

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def raise_salary(self, percentage):
        self.salary *= (1 + percentage/100)

# Example usage
emp = Employee('John', 25, 5000)
emp.raise_salary(10)
print(emp.salary)  # Output: 5500.0
# Question 4:

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Title: {self.title}\nAuthor: {self.author}")

# Example usage
book = Book('The Great Gatsby', 'F. Scott Fitzgerald')
book.display()  # Output: Title: The Great Gatsby Author: F. Scott Fitzgerald
# Question 5:

class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, distance):
        self.mileage += distance

# Example usage
car = Car('Toyota', 'Camry', 2020, 5000)
car.drive(100)
print(car.mileage)  # Output: 5100
# Question 6:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"{self.name} object is destroyed")

# Example usage
person = Person('John', 25)
del person  # Output: John object is destroyed
# Question 7:
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def __del__(self):
        print("The account has been deleted")

# Example usage
account = BankAccount(123456, 5000)
del account  # Output: The account has been deleted
# Question 8:
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class Car(Vehicle):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand

    def get_brand_and_speed(self):
        return f"{self.brand} - {self.speed}"

# Example usage
car = Car(100, 'Toyota')
print(car.get_brand_and_speed())  # Output: Toyota - 100
# Question 9:
class Animal:
    def __init__(self, name):
        self.name = name

class Pet:
    def __init__(self, owner):
        self.owner = owner

# Example usage
animal = Animal('dog')
pet = Pet('John')
# Question 10:

class Dog(Animal, Pet):
    def __init__(self, name, owner, breed):
        Animal.__init__(self, name)
        Pet.__init__(self, owner)
        self.breed = breed

    def get_info(self):
        return f"{self.name} - {self.owner} - {self.breed}"

# Example usage
dog = Dog('Buddy', 'John', 'Labrador')
print(dog.get_info())  # Output: Buddy - John - Labrador
# Question 11:
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_info(self):
        return f"{self.name} - {self.salary} - {self.department}"

# Example usage
manager = Manager('John', 5000, 'IT')
print(manager.get_info())  # Output: John - 5000 - IT
# Question 12:
class Shape:
    def __init__(self, color):
        self.color = color

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
# Question 13:
import math

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Example usage
circle = Circle('red', 5)
print(circle.area())  # Output: 78.53981633974483

rectangle = Rectangle('blue', 10, 5)
print(rectangle.area())  # Output: 50
# Question 14:
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

# Example usage
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500

account.withdraw(2000)  # Output: Insufficient balance
account.withdraw(1000)
print(account.get_balance())  # Output: 500
# Question 15:
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

# Example usage
dog = Dog()
dog.speak()  # Output: Woof

cat = Cat()
cat.speak()  # Output: Meow
# Question 16:
class Calculator:
    @classmethod
    def add(cls, a, b):
        return a + b

# Example usage
result = Calculator.add(5, 10)
print(result)  # Output: 15