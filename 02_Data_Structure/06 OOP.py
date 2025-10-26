print("=== Python OOP (Object-Oriented Programming) ===\n")

print("1️⃣  OOP allows structuring programs using classes and objects.\n")

print("🔎  Syntax note:")
print("  class ClassName:")
print("      '''Optional docstring'''")
print("      def __init__(self, parameters):")
print("          # constructor code")
print("      def method_name(self, parameters):")
print("          # method code\n")

print("🖨️  Creating a class and object")
class Person:
    '''Represents a person'''
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old")

# create object
p1 = Person("Ayush", 20)
p1.greet()
print()

print("✏️  Accessing and modifying attributes")
print("Name:", p1.name)
p1.age = 21
print("Modified age:", p1.age, "\n")

print("💡  Class vs instance attributes")
class Student:
    school = "XYZ School"  # class attribute
    def __init__(self, name):
        self.name = name  # instance attribute

s1 = Student("Alice")
s2 = Student("Bob")
print(s1.name, s1.school)
print(s2.name, s2.school)
Student.school = "ABC School"
print("After modifying class attribute:")
print(s1.name, s1.school)
print(s2.name, s2.school, "\n")

print("🔄  Methods")
print("• Instance methods use self to access instance attributes")
print("• Class methods use @classmethod decorator and cls parameter")
print("• Static methods use @staticmethod decorator (no self or cls)\n")

print("🌀  Inheritance and overriding")
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

dog = Dog()
dog.speak()  # method overriding
print()

print("🔐  Encapsulation (private attributes)")
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print("Balance:", acc.get_balance(), "\n")

print("📜  Special methods")
print("• __str__ for readable string representation")
print("• __repr__ for official string representation\n")

print("🎯  Summary of key OOP points")
print("• Class = blueprint, Object = instance")
print("• Use __init__ to initialize objects")
print("• Attributes can be instance or class-level")
print("• Methods can be instance, class, or static")
print("• Inheritance allows reusing code and method overriding")
print("• Encapsulation via private attributes (_ or __ prefix)")
print("• Special methods like __str__ and __repr__ for object representation\n")

print("✅  End of OOP note — covers classes, objects, attributes, methods, inheritance, encapsulation, and special methods.")