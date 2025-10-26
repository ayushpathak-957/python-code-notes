print("=== Python Functions ===\n")

print("1️⃣  Functions are reusable blocks of code that perform a specific task.\n")

print("🔎  Syntax note:")
print("  def function_name(parameters):")
print("      '''Optional docstring'''")
print("      # code block")
print("      return value\n")

print("🖨️  Simple function")
def greet():
    print("Hello, Ayush!")
greet()
print()

print("✏️  Function with parameters")
def add(a, b):
    return a + b
print("add(5, 3) =", add(5, 3), "\n")

print("💡  Types of parameters")
print("➡️  Positional parameters: values passed in order")
print("➡️  Default parameters: provide default values if not passed")
print("➡️  Keyword parameters: specify name=value")
print("➡️  Variable-length (*args, **kwargs): for flexible number of arguments\n")

print("🖨️  Examples")
def greet_person(name="Friend"):
    print("Hello,", name)
greet_person("Alice")
greet_person()
print()

def multiply(*numbers):
    result = 1
    for n in numbers:
        result *= n
    return result
print("multiply(2,3,4) =", multiply(2,3,4), "\n")

def print_info(**info):
    for key, value in info.items():
        print(key, "->", value)
print_info(name="Ayush", age=20)
print()

print("📜  Docstrings and help()")
def square(n):
    '''Returns the square of n'''
    return n**2
print(square.__doc__)
print("square(5) =", square(5), "\n")

print("🌐  Scope: local vs global")
x = 10  # global
def test_scope():
    x = 5  # local
    print("Inside function x =", x)
test_scope()
print("Outside function x =", x, "\n")

print("🧠  Lambda functions (anonymous single-line functions)")
double = lambda x: x*2
print("double(5) =", double(5))
sum_lambda = lambda a, b: a + b
print("sum_lambda(3, 4) =", sum_lambda(3, 4), "\n")

print("🌀  Nested functions")
def outer():
    print("Outer function")
    def inner():
        print("Inner function")
    inner()
outer()
print()

print("🎯  Summary of key function points")
print("• Use def to define a function")
print("• Functions can take parameters (positional, default, keyword, variable-length)")
print("• Return values using return")
print("• Local variables exist only inside the function; global outside")
print("• Lambda functions are concise, single-expression anonymous functions")
print("• Nested functions can exist inside outer functions")
print("• Use docstrings for documentation (access via __doc__ or help())\n")

print("✅  End of Functions note — covers definition, parameters, return, scope, lambda, docstrings, and nested functions.")
