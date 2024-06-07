# -*- coding: utf-8 -*-
"""Week 1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ry2vDVJrTV22xknbrc2zWEFQi2WC0Z2L

#**1.Explain Encapsulation with example and write python code**
Encapsulation is a fundamental principle of object-oriented programming (OOP) that involves bundling data and the methods that operate on that data into a single unit, typically a class**
"""

class Car:
    def __init__(self, make, model):
        self.__make = make    # Private attribute
        self.__model = model  # Private attribute

    # Getter method for make
    def get_make(self):
        return self.__make

    # Getter method for model
    def get_model(self):
        return self.__model

    # Setter method for make
    def set_make(self, make):
        self.__make = make

    # Setter method for model
    def set_model(self, model):
        self.__model = model

# Creating an object of the Car class
car = Car("Maruthi", "Swift")

# Accessing and modifying data using getter and setter methods
print(car.get_make())
# Output: Maruthi
print(car.get_model())
# Output: Hyndai

# Modifying the make and model using setters
car.set_make("Mercedes")
car.set_model("G Class")

# Accessing the modified data using getters
print(car.get_make())
# Output: Mercedes
print(car.get_model())
# Output: G Class

"""#**2. Explain Polymorphism with example and write python code.**
Polymorphism is also another fundamental concept in object-oriented programming (OOP). It refers to the ability of different objects to respond to the same method call in different ways.
"""

class Vehicle:  # Parent class
    def make_sound(self):
        print("Generic vehicle sound")

class Car(Vehicle):  # Subclass "Car" inheriting from Vehicle
    def make_sound(self):
        print("Vrooooooom!")

class Motorcycle(Vehicle):  # Subclass "Motorcycle" inheriting from Vehicle
    def make_sound(self):
        print("Brrrrrrrrrm!")

class Bicycle(Vehicle):  # Subclass "Bicycle" inheriting from Vehicle
    def make_sound(self):
        print("Ring ring!!!")

# sound_test - method responsible for polymorphism, vehicle: object
def sound_test(vehicle):
    vehicle.make_sound()

# Create Vehicle objects
car = Car()
motorcycle = Motorcycle()
bicycle = Bicycle()

sound_test(car)
# Output: Vrooooooom!
sound_test(motorcycle)
# Output: Brrrrrrrrrm!
sound_test(bicycle)
# Output: Ring ring!!

"""#**3. Explain Single Level Inheritance with python code.**
Single-level inheritance is a type of inheritance in object-oriented programming where a class inherits from only one other class called as superclass.
"""

# Base class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Derived class
class fish(Animal):
    def swim(self):
        print("Fish Swims")

# Create an instance of Bird
fish = fish()
fish.speak()  # Inherited method
fish.swim()    # Method of fish class

"""#**4. Explain Multiple inheritance with python code.**
Multiple inheritance is a feature of OOP language in which a class can inherit attributes and methods from more than one parent class. This allows a class to combine functionalities from multiple classes into a single subclass.
"""

# Base class 1
class Flyable:
    def fly(self):
        print("This can fly")

# Base class 2
class Swimmable:
    def swim(self):
        print("This can swim")

# Derived class
class duck(Flyable, Swimmable):
    def quack(self):
        print("Duck says quack")

# Create an instance of Duck
duck = duck()
duck.fly()   # Method from Flyable class
duck.swim()  # Method from Swimmable class
duck.quack() # Method from Duck class

"""#**5. Explain Muti-level inheritance with python code**
Multi-level inheritance is a feature of OOP in which a class inherits properties and behavior from a parent class, which in turn inherits from another parent class. This forms a hierarchical relationship among the classes.
"""

# Base class
class Device:
    def power_on(self):
        print("Device is now on")

# Derived class
class Smartphone(Device):
    def make_call(self):
        print("Making a call")

# Further derived class
class Smartwatch(Smartphone):
    def track_steps(self):
        print("Tracking steps")

# Create an instance of Smartwatch
smartwatch = Smartwatch()

smartwatch.power_on()  # Inherited from Device
smartwatch.make_call() # Inherited from Smartphone
smartwatch.track_steps()  # Method of Smartwatch class

"""#**6. What do you mean by conditional statements. Explain with python code**
Conditional statements are used in programming to execute different blocks of code based on certain conditions. These conditions evaluate to either True or False, and the program flow is determined accordingly.

example:

if,else,elif
"""

x = 10

# Check the value of x using the conditional statements
if x > 10:
    print("x is greater than 10")
elif x < 10:
    print("x is less than 10")
else:
    print("x is equal to 10")

"""#**7. What do you mean by decision making statements. Explain with python code.**
Decision-making statements, also known as conditional statements, are used in programming to control the flow of execution based on certain conditions
"""

#lets see if he can vote or not
age = int(input("Enter your age: "))

# Check if the person is eligible to vote
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote yet.")

"""#**8. Write a program of factorial in python**

"""

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

# Taking Input from the user
num = int(input("Enter a number to calculate its factorial: "))

# Check if the input is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}")

"""#**9.What do you understand by Functions? Explain with python code**
Function allow you to break down a program into smaller, more manageable pieces, making it easier to understand the code.

"""

def calculator(operation, x, y):
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        if y == 0:
            return "Error! Division by zero is not allowed."
        else:
            return x / y
    else:
        return "Invalid operation"

# Input from the user
operation = input("Select the operation (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculate and print the result
result = calculator(operation, num1, num2)
print("Result:", result)

"""#**10. How many pillars of Oops we have in Python?**
There are 5 Pillars in Object Oriented Programming in Python

**Objects**: Objects are like things in the real world, each with its own characteristics (attributes) and actions (methods).

**Classes**: Classes are like templates that define how objects should be created. They specify what attributes and methods an object should have.

**Inheritance**: Inheritance allows a new class to inherit characteristics from an existing class. It helps in reusing code and creating relationships between classes.

**Polymorphism**: Polymorphism lets objects of different classes be treated as if they are of the same type. It allows methods to behave differently based on the object they are called on.

**Encapsulation**: Encapsulation means bundling data and methods together within a class. It keeps data safe from outside interference and helps in organizing code.
"""