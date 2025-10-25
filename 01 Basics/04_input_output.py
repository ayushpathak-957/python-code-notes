print("=== Python Basics: Input / Output ===\n")

print("1️⃣  Input from the user")
print("Python uses the input() function to get user input as a string.\n")

print("🔎  Syntax:")
print("variable = input('Enter something: ')\n")

print("🖨️  Example: Get user name")
name = input("Enter your name: ")
print("Hello,", name, "\n")

print("⚠️  Type of input:")
print("All input values are strings by default.\n")
age = input("Enter your age: ")
print("type(age) = ", type(age),"\n")
print("You can convert it to int or float if needed:")
height = float(input("Enter you height in meters "))
print("type(height) = ", type(height),"\n")

print("🖨️  Output with print():")
print("You can print multiple values separated by comma:")
print("Name:", name, "Age:", age,"Height: ",height,"\n")

print("✅  End of Input / Output note — covers input(), default string type, and simple print examples\n")