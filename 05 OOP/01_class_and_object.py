class Student:  #Creating a class

    Clg_name = "KIET" # class variable
    # These are shared by all objects of that class.
    # They are defined outside any method — directly inside the class.

    def __init__(self, name, age):  #Adding attributes (data)
        self.name = name # instance variable
        self.age = age
        # ✅ self refers to the current object being created.
        # So self.name means “this object's name”.
    def greet(self): #Adding a method (behavior) - Instance Method
        print(f"Hello, I'm {self.name} and I'm {self.age} years old.")
    # ✅ A method is just a function inside a class that uses self to access the object.

s1 = Student("Ayush", 18) #Creating an object
print(s1.name) # internally it is like Student.name(s1) , this is the use of self 
print(s1.age)
s1.greet()
print()
s2 = Student("Diya",20)#this way multiple objects can be created 
print(s2.name)
print(s2.age)
s2.greet()
print()

s1.hobby = "codding"
print(s1.hobby,"new instance variable for that object can also be defined like this\n")

print(s1.Clg_name,s2.Clg_name,Student.Clg_name,"They will print the same name because it's shared by the class.")
Student.Clg_name = "IIT Ghaziabad" #Changing class variable , will affect everyone
print(s1.Clg_name,s2.Clg_name,Student.Clg_name,"The name can also be changed")

s1.Clg_name = "KIET"
print(s1.Clg_name,s2.Clg_name,Student.Clg_name,"only changed for s1\n")
#if you change it through an object, it creates a new instance variable for that object only. Now s1 has its own copy (not shared anymore).

# 🧠 OOP (Object Oriented Programming) — Recap

# • OOP helps organize code using classes and objects.
# • A Class is a blueprint or template.
# • An Object is a real instance (created from a class).
# • 'self' refers to the current object itself.
# • The __init__() method is called automatically when an object is created (used to initialize instance variables).

# 🔹 Instance Variables
# • Defined inside __init__() using self.
# • Unique for each object.
# • Example: self.name, self.age

# 🔹 Class Variables
# • Defined directly inside the class, outside any method.
# • Shared by all objects of the class.
# • Example: Clg_name = "KIET"

# 🔹 Changing Variables
# • Changing a class variable through the class name affects all objects.
# • Changing it through an object creates a new instance variable for that object only.

# 🧩 Summary Table
# | Type              | Defined In             | Belongs To        | Shared? | Example                    |
# |--------------------|------------------------|-------------------|---------|-----------------------------|
# | Instance Variable  | Inside __init__ (self) | Individual Object | No      | self.name                   |
# | Class Variable     | Directly inside class  | The whole Class   | Yes     | ClassName.variable_name     |

# ✅ In short:
# Class → Blueprint
# Object → Real thing
# self → Refers to current object
# __init__ → Initializes object data
# Instance variable → Personal data of object
# Class variable → Shared data of the class
