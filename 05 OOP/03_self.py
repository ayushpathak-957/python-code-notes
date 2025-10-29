class Student:
    def get_data(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 75:
            return "A"
        else:
            return "B"

    def show(self):
        print(f"Name: {self.name}, Marks: {self.marks}, Grade: {self.grade()}")

s1 = Student()
s1.get_data("Ayush", 95)
s1.show()

s2 = Student()
s2.get_data("Divya", 87)
s2.show()

'''Python always passes the object automatically as the first argument, and your function must accept it — usually named as self.
every method inside a class must have self as the first parameter (unless it’s a static method'''