print("=== Python OOP Path: Understanding Modules ===\n")

print("1️⃣  What is a Module?")
print("A module is simply a Python file (.py) that contains definitions — functions, classes, or variables.")
print("It allows code reusability, organization, and better maintainability.\n")

print("🧩  Why use Modules?")
print("- To organize large codebases into smaller logical parts.")
print("- To reuse code across multiple programs.")
print("- To prevent name conflicts by creating namespaces.\n")

print("📥  Importing a Module")
print("We use the 'import' keyword to load existing modules.\n")

print("➡️  Example:")
print("import math")
print("print(math.sqrt(25))  # uses sqrt() from math module\n")
import math
print("Output:")
print(math.sqrt(25), "\n")

print("🔹  Accessing Specific Members")
print("We can access functions or variables using dot notation.\n")
print("➡️  Example:")
print("print(math.pi)   # value of π\n")
print(math.pi, "\n")

print("🧭  Aliasing Modules (using 'as')")
print("You can rename a module while importing it.\n")
print("➡️  Example:")
print("import math as m")
print("print(m.factorial(5))\n")
import math as m
print("Output:")
print(m.factorial(5), "\n")

print("🎯  Importing Specific Items")
print("You can import only what you need from a module.\n")
print("➡️  Example:")
print("from math import sqrt, pow")
print("print(sqrt(49))")
print("print(pow(2, 3))\n")
from math import sqrt, pow
print("Output:")
print(sqrt(49))
print(pow(2, 3), "\n")

print("🚫  Importing Everything (Not Recommended)")
print("You can import all members of a module using '*', but this is discouraged because it can cause name conflicts.")
print("➡️  Example:")
print("from math import *")
print("print(sin(0))\n")

from math import sin
print("Output:")
print(sin(0), "\n")

print("🛠️  Creating Your Own Module")
print("You can create your own module by simply saving a Python file with functions or variables.")
print("➡️  Example:")
print("File: mymodule.py")
print("def greet(name):")
print("    return f'Hello, {name}!'")
print("Now, you can import and use it in another file.\n")

print("➡️  Example Usage:")
print("import mymodule")
print("print(mymodule.greet('Ayush'))\n")

print("🧠  Behind the Scenes:")
print("- When you import a module, Python executes it once and caches it in sys.modules.")
print("- The module search path is stored in sys.path.\n")

print("➡️  Example:")
print("import sys")
print("print(sys.path)  # shows directories Python searches for modules\n")
import sys
print("Output (partial):")
print(sys.path[:3], "\n")

print("⚙️  Reloading a Module (Advanced)")
print("If you modify a module while your program is running, use importlib.reload() to re-import it.\n")

print("➡️  Example:")
print("import importlib")
print("importlib.reload(mymodule)\n")

print("🧩  Summary of Module Keywords:")
print("• import module_name")
print("• from module_name import function_name")
print("• from module_name import *")
print("• import module_name as alias\n")

print("✅  End of Module Notes — You now understand importing, aliasing, custom modules, and sys.path!")
