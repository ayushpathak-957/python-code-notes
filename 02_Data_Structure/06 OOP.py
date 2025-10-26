print("=== Python OOP (Object-Oriented Programming) ===\n")

print("1️⃣  What is OOP?")
print("  Object-Oriented Programming allows structuring code into classes and objects,")
print("  modeling real-world entities, promoting reusability, modularity, and maintainability.\n")

print("🔎  Key Concepts of OOP:")
print("  • Class: Blueprint for objects")
print("  • Object: Instance of a class")
print("  • Attributes: Data stored in objects (instance/class)")
print("  • Methods: Functions defined inside classes")
print("  • Inheritance: Reusing code from parent class")
print("  • Encapsulation: Hiding internal data")
print("  • Polymorphism: Using a single interface for multiple implementations\n")

print("🖨️  Creating a Class and Object")
class Person:
    '''Represents a person with name and age'''
    species = "Homo sapiens"  # class attribute, shared among all objects

    def __init__(self, name, age):
        '''Constructor to initialize instance attributes'''
        self.name = name  # instance attribute
        self.age = age

    def greet(self):
        print("Hello! My name is", self.name, "and I am", self.age, "years old")

# Creating objects
p1 = Person("Ayush", 20)
p2 = Person("Alice", 25)

p1.greet()
p2.greet()
print("Class attribute species:", p1.species, "\n")

print("✏️  Accessing and Modifying Attributes")
print("➡️ Access instance attribute:", p1.name)
p1.age = 21
print("➡️ Modified age:", p1.age)
print("➡️ Access class attribute:", Person.species)
Person.species = "Human"
print("➡️ Modified class attribute:", p2.species, "\n")

print("💡  Instance vs Class Attributes")
print("• Instance attributes: unique per object")
print("• Class attributes: shared among all instances")
print("• Example:")
print("p1.name =", p1.name, ", p2.name =", p2.name)
print("p1.species =", p1.species, ", p2.species =", p2.species, "\n")

print("🔄  Methods in Depth")
print("➡️ Instance methods: use 'self', can access/modify instance attributes")
print("➡️ Class methods: use @classmethod and 'cls', can access/modify class attributes")
print("➡️ Static methods: use @staticmethod, no self or cls, utility functions\n")

class Student:
    school = "XYZ School"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(self.name, "scored", self.marks)

    @classmethod
    def set_school(cls, new_school):
        cls.school = new_school

    @staticmethod
    def welcome():
        print("Welcome to the school!")

s1 = Student("Bob", 85)
s2 = Student("Charlie", 90)

s1.show()
Student.set_school("ABC School")
print("Updated school for s2:", s2.school)
Student.welcome()
print()

print("🌀  Inheritance")
print("• Single inheritance: Child inherits from one parent")
print("• Multi-level inheritance: Child inherits from parent, grandchild inherits from child")
print("• Multiple inheritance: Child inherits from multiple parents\n")

class Animal:
    def speak(self):
        print("Some generic sound")

class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")  # overriding parent method

dog = Dog()
dog.speak()
print()

print("🔐  Encapsulation")
print("• Use _ or __ prefix to indicate protected/private attributes")
print("• Access private attributes via methods")

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print("Balance after deposit:", acc.get_balance(), "\n")

print("📜  Special Methods (__str__, __repr__, __len__, __add__)")
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}, Pages: {self.pages}"

    def __len__(self):
        return self.pages

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book("Python 101", 150)
b2 = Book("OOP Deep Dive", 200)

print(b1)
print("Length of b2:", len(b2))
print("Total pages of b1 + b2:", b1 + b2, "\n")

print("🧠  Polymorphism")
print("• Ability to use same method on different objects/classes")
print("• Example: speak() in Dog and Cat can behave differently but called similarly\n")

print("🎯  Composition vs Aggregation")
print("• Composition: has-a relationship, object contains another object")
print("• Aggregation: has-a but independent lifecycle\n")

print("✅  Summary of Python OOP Concepts")
print("• Class = blueprint, Object = instance")
print("• Attributes = instance/class variables")
print("• Methods = instance/class/static methods")
print("• self = reference to current object")
print("• Inheritance allows reusing code and overriding methods")
print("• Encapsulation hides data (_ or __)")
print("• Special methods allow custom behavior")
print("• Polymorphism = same interface, different behavior")
print("• Composition/Aggregation = relationships between objects")
print("• Object lifetime managed by __init__ and __del__\n")

print("✅  End of detailed OOP notes — covers everything from classes to polymorphism and special methods.")
