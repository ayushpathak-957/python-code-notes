print("=== Python Basics: Variables and Data Types ===\n")

print("1️⃣  Variables in Python")
print("Variables are used to store data values.")
print("You don't need to declare their type explicitly (dynamic typing).\n")

print("🔎  Syntax:")
print("variable_name = value\n")

print("🖨️  Examples:")
x = 10
y = 3.14
name = "Ayush"
is_active = True

print("x =", x)
print("y =", y)
print("name =", name)
print("is_active =", is_active, "\n")

print("📜  Variable naming rules:")
print("• Can contain letters, numbers, and underscores")
print("• Must start with a letter or underscore")
print("• Cannot use Python keywords\n")

print("🎯  Common data types:")
print("➡️  int   -> integers, e.g., 5, -3, 100")
print("➡️  float -> decimal numbers, e.g., 3.14, -0.5")
print("➡️  str   -> text, e.g., 'Hello', \"Python\"")
print("➡️  bool  -> True or False\n")

print("⚠️  Type checking and conversion:")
print("➡️  type(x) -> shows the type of variable")
print("➡️  int(), float(), str(), bool() -> convert between types\n")

print("🖨️  Example of type and conversion:")
print("type(x) ->", type(x))
print("float(x) ->", float(x))
print("str(y) ->", str(y))
print("bool(0) ->", bool(0), "\n")

print("🔗  Multiple assignment:")
a, b, c = 5, 3.2, "Python"
print("a =", a)
print("b =", b)
print("c =", c, "\n")

print("🔄  Swapping variables without a temporary variable:")
x, y = 1, 2
print("Before swap: x =", x, ", y =", y)
x, y = y, x
print("After swap: x =", x, ", y =", y, "\n")

print("✅  End of Variables and Data Types note — covers variables, naming rules, common types, type checking, conversion, multiple assignment, and swapping")
