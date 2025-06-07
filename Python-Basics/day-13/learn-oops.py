# OOP 
# OOP is a programming paradigm  based on the concept of "objects", which contain data and methods to operate on that data. 
# It promotes code reuse, modularity, and encapsulation.
# Python supports OOP fully — everything is an object.

# Paradigm
# A paradigm is a style or approach of programming — a way of thinking about how to write and organize code.

# Class and Object
# Class: Blueprint for creating objects.
# Object: Instance of a class.

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"{self.color} {self.brand} is driving")

car1 = Car("Toyota", "Red")
car1.drive()

# __init__()
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass 
    pass

# self
# self is a reference to the current instance of the class.
# It is used to access variables, methods, and properties of the current object.
class Car:
    def __init__(self, brand, color):
        self.brand = brand   # instance variable
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.brand} is driving")

# Create object
c1 = Car("Toyota", "Red")
c1.drive()
# The Red Toyota is driving
# self.brand refers to the brand of the current object (c1).
# If you omit self, Python won’t know what variable you're referring to — you'll get an error.
# Behind the scenes:
# When you call:
# c1.drive()
# Python internally does:
# Car.drive(c1)
# So self = c1 in this case.

#  What if we forget self?
# class Test:
#     def show():  # ❌ No 'self'
#         print("Hello")

# t = Test()
# t.show()  # Error: missing 1 required positional argument
# ✅ Fix:
# def show(self):



# Instance Variables and Methods
# Instance Variables: Defined inside __init__ using self.
# Instance Methods: Can access and modify instance variables.

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

# Class Variables and Methods
# Class Variables: Shared across all instances.
# Class Methods: Use @classmethod decorator.
class Employee:
    company = "Google"  # class variable

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

# Static Methods
# Does not access class or instance variables.
class Math:
    @staticmethod
    def add(x, y):
        return x + y

# Encapsulation
# Restricting access to internal data using private/protected access modifiers.
# self.__var: Private
# self._var: Protected (convention only)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

# Inheritance
# Allows a class (child) to inherit attributes and methods from another (parent).
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()

# Types of Inheritance in Python

# Single Inheritance
# ✅ One base class → One derived class
# 📄 Example:
# class Animal:
#     def speak(self):
#         print("Animal speaks")
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
# d = Dog()
# d.speak()
# d.bark()
# 💼 Use Case:
# When one class inherits functionality from a single base class. E.g., Employee from Person.

# Multiple Inheritance
# ✅ One class inherits from more than one base class.
# 📄 Example:
# class Flyable:
#     def fly(self):
#         print("Flying")
# class Swimmable:
#     def swim(self):
#         print("Swimming")
# class Duck(Flyable, Swimmable):
#     pass
# d = Duck()
# d.fly()
# d.swim()
# 💼 Use Case:
# When a class needs combined functionality from multiple unrelated classes, like PrinterScanner.

# Polymorphism
# Same interface, different behavior.
# Method Overriding (Run-time Polymorphism)
class Animal:
    def sound(self):
        print("Some sound")

class Cat(Animal):
    def sound(self):
        print("Meow")

a = Cat()
a.sound()

#  Multilevel Inheritance
# ✅ Derived class inherits from a derived class (chain of inheritance).
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Puppy(Dog):
    def weep(self):
        print("Weeping")

p = Puppy()
p.eat()
p.bark()
p.weep()
# Inheritance hierarchy: Person → Employee → Manager.

# Hierarchical Inheritance
# Multiple derived classes inherit from a single base class.
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Cat(Animal):
    def meow(self):
        print("Meowing")

d = Dog()
c = Cat()
d.eat(); d.bark()
c.eat(); c.meow()
# When you have a common base class with specific derived behaviors (e.g., Vehicle → Car, Bike).

# Hybrid Inheritance
# A combination of two or more types of inheritance.
class A:
    def method_a(self):
        print("A")

class B(A):
    def method_b(self):
        print("B")

class C:
    def method_c(self):
        print("C")

class D(B, C):  # Inherits from both B and C
    def method_d(self):
        print("D")

obj = D()
obj.method_a()
obj.method_b()
obj.method_c()
obj.method_d()
# Used in complex real-world systems, e.g., User → Admin → SuperAdmin + Permissions.

# Duck Typing
# Python cares about behavior, not type.
class Bird:
    def fly(self):
        print("Flying")

class Airplane:
    def fly(self):
        print("Airplane flying")

def lift_off(obj):
    obj.fly()

lift_off(Bird())
lift_off(Airplane())

# Abstraction
# Hiding implementation details, only showing the functionality.
# Abstract Class using abc module
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Engine started")

c = Car()
c.start_engine()

# Special / Magic Methods
# Start and end with double underscores __.
# | Magic Method   | Purpose                                | Example (Simplified)                                                        | Use Case                             |
# | -------------- | -------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------ |
# | `__init__`     | Constructor                            | `def __init__(self, x): self.x = x`                                         | Initialize instance data             |
# | `__str__`      | String representation                  | `def __str__(self): return f\"Value: {self.x}\"`                            | For `print(obj)`                     |
# | `__repr__`     | Official string representation         | `def __repr__(self): return f\"MyClass({self.x})\"`                         | Debugging, `repr(obj)`               |
# | `__len__`      | Length of object                       | `def __len__(self): return len(self.data)`                                  | Use with `len(obj)`                  |
# | `__getitem__`  | Access using `[]`                      | `def __getitem__(self, key): return self.data[key]`                         | Indexing or dictionary-like access   |
# | `__setitem__`  | Assign using `[]`                      | `def __setitem__(self, key, value): self.data[key] = value`                 | Mutating data via `obj[key] = value` |
# | `__delitem__`  | Delete using `[]`                      | `def __delitem__(self, key): del self.data[key]`                            | For `del obj[key]`                   |
# | `__call__`     | Make instance callable                 | `def __call__(self): print(\"Called\")`                                     | `obj()` syntax                       |
# | `__eq__`       | Equality `==`                          | `def __eq__(self, other): return self.x == other.x`                         | Compare two objects                  |
# | `__ne__`       | Not equal `!=`                         | `def __ne__(self, other): return self.x != other.x`                         | Inequality check                     |
# | `__lt__`       | Less than `<`                          | `def __lt__(self, other): return self.x < other.x`                          | Sorting, comparisons                 |
# | `__le__`       | Less than or equal `<=`                | `def __le__(self, other): return self.x <= other.x`                         | Sorting                              |
# | `__gt__`       | Greater than `>`                       | `def __gt__(self, other): return self.x > other.x`                          | Sorting, comparisons                 |
# | `__ge__`       | Greater than or equal `>=`             | `def __ge__(self, other): return self.x >= other.x`                         | Sorting                              |
# | `__add__`      | Addition `+`                           | `def __add__(self, other): return self.x + other.x`                         | Arithmetic operator overloading      |
# | `__sub__`      | Subtraction `-`                        | `def __sub__(self, other): return self.x - other.x`                         | Overloading `-`                      |
# | `__mul__`      | Multiplication `*`                     | `def __mul__(self, other): return self.x * other.x`                         | Overloading `*`                      |
# | `__truediv__`  | Division `/`                           | `def __truediv__(self, other): return self.x / other.x`                     | Overloading `/`                      |
# | `__mod__`      | Modulo `%`                             | `def __mod__(self, other): return self.x % other.x`                         | `%` operator                         |
# | `__pow__`      | Exponentiation `**`                    | `def __pow__(self, other): return self.x ** other.x`                        | Power operations                     |
# | `__abs__`      | Absolute value `abs(obj)`              | `def __abs__(self): return abs(self.x)`                                     | Math support                         |
# | `__bool__`     | Truth value testing `bool(obj)`        | `def __bool__(self): return self.x != 0`                                    | Conditional logic                    |
# | `__contains__` | `in` operator                          | `def __contains__(self, item): return item in self.data`                    | Membership testing                   |
# | `__iter__`     | Iterator                               | `def __iter__(self): return iter(self.data)`                                | Looping over object                  |
# | `__next__`     | Next value in iteration                | `def __next__(self):` (define logic)                                        | Used with iterators                  |
# | `__enter__`    | Context manager (enter)                | `def __enter__(self): return self`                                          | `with` statement setup               |
# | `__exit__`     | Context manager (exit)                 | `def __exit__(self, *args):` (cleanup code)                                 | `with` statement cleanup             |
# | `__del__`      | Destructor                             | `def __del__(self): print(\"Object deleted\")`                              | Cleanup when object is destroyed     |
# | `__getattr__`  | Called when attribute not found        | `def __getattr__(self, name): return \"Default\"`                           | Dynamic attribute access             |
# | `__setattr__`  | Called when setting attribute          | `def __setattr__(self, name, value): object.__setattr__(self, name, value)` | Track or restrict setting attributes |
# | `__slots__`    | Limit attributes & memory optimization | `__slots__ = ['name']`                                                      | Memory-efficient classes             |

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __len__(self):
        return self.pages

b = Book(300)
print(len(b))  # 300

# Composition
# Using one class as a part of another class.
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car is driving")

c = Car()
c.drive()

# Aggregation
# Weaker relationship than composition (object passed externally).
class Department:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

dept = Department("IT")
emp = Employee("Ketan", dept)

# Data Classes (dataclasses module)
# Simplifies class creation for storing data.
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float

p = Product("Pen", 10.5)
print(p.name, p.price)

# Getter & Setter (Property Decorators)
# Pythonic way to access private variables.
class Student:
    def __init__(self, marks):
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if value < 0:
            raise ValueError("Marks cannot be negative")
        self.__marks = value

# Object Serialization (Pickling)
import pickle

class User:
    def __init__(self, name):
        self.name = name

user = User("Ketan")

# Save
with open("user.pkl", "wb") as f:
    pickle.dump(user, f)

# Load
with open("user.pkl", "rb") as f:
    loaded_user = pickle.load(f)
