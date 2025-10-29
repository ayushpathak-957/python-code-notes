print("🏫\tMethods in Python Classes\n")

# 1️⃣ Instance Method
print("1️⃣\tInstance Method\n")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_details(self):   # Instance method
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Ayush", 95)
s2 = Student("Riya", 89)

s1.show_details()
s2.show_details()

print("-" * 50)


# 2️⃣ Class Method
print("2️⃣\tClass Method\n")

class Student:
    school_name = "ABC School"   # Class variable

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

print("Before change:", Student.school_name)
Student.change_school("XYZ School")
print("After change:", Student.school_name)

print("-" * 50)


# 3️⃣ Static Method
print("3️⃣\tStatic Method\n")

class MathOps:
    @staticmethod
    def add(a, b):
        return a + b

print("Sum:", MathOps.add(5, 3))

print("-" * 50)


# 4️⃣ Summary and Key Notes
print("💡\tKey Points:\n")
print("• Instance methods → Access and modify object (instance) data.")
print("• Class methods → Work with class variables (shared by all objects).")
print("• Static methods → Utility functions; don’t use self or cls.")
print("• Use 'self' for instance data and 'cls' for class data.\n")

print("📘\tSummary Table\n")
print("| Method Type      | Decorator       | First Arg | Access Instance? | Access Class? | Use Case |")
print("|------------------|----------------|------------|------------------|----------------|-----------|")
print("| Instance Method  | (none)          | self       | ✅ Yes           | ✅ Yes (via class) | Work on object data |")
print("| Class Method     | @classmethod    | cls        | ❌ No            | ✅ Yes           | Modify class data |")
print("| Static Method    | @staticmethod   | None       | ❌ No            | ❌ No            | Utility/helper |")
