print("=== Python Basics: Operators (In-Depth) ===\n")

print("1️⃣  What are Operators?")
print("Operators are symbols that perform operations on values or variables.\n")

print("🔎  Categories of Operators:")

print("🧮  1. Arithmetic Operators")
print("Used for mathematical operations:")
a = 10
b = 3
print("a =", a, ", b =", b)
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b, " # floor division")
print("a % b =", a % b, " # modulus")
print("a ** b =", a ** b, " # exponent")
print("Unary plus/minus: +a =", +a, ", -b =", -b, "\n")

print("⚖️  2. Comparison Operators")
print("Compare two values and return True/False:")
print("a == b ->", a == b)
print("a != b ->", a != b)
print("a > b  ->", a > b)
print("a < b  ->", a < b)
print("a >= b ->", a >= b)
print("a <= b ->", a <= b, "\n")

print("🔄  3. Assignment Operators")
print("Used to assign values to variables:")
c = 5
print("c =", c)
c += 2
print("c += 2 ->", c)
c -= 1
print("c -= 1 ->", c)
c *= 3
print("c *= 3 ->", c)
c /= 2
print("c /= 2 ->", c)
c %= 4
print("c %= 4 ->", c)
c //= 2
print("c //= 2 ->", c)
c **= 3
print("c **= 3 ->", c,"\n")

print("🔗  4. Logical Operators")
print("Used to combine conditional statements:")
x = True
y = False
print("x and y ->", x and y)
print("x or y  ->", x or y)
print("not x   ->", not x, "\n")

print("🧩  5. Membership Operators")
print("Check if value exists in a sequence:")
fruits = ['apple', 'banana', 'mango']
print("'apple' in fruits ->", 'apple' in fruits)
print("'grape' not in fruits ->", 'grape' not in fruits, "\n")

print("⚠️  6. Identity Operators")
print("Check if two variables point to the same object:")
m = [1, 2, 3]
n = m
o = [1, 2, 3]
print("m is n ->", m is n)
print("m is o ->", m is o)
print("m is not o ->", m is not o, "\n")

print("🖥️  7. Bitwise Operators")
print("Operate on bits of integers:")
p = 5    # 0b0101
q = 3    # 0b0011
print("p =", p, "->", bin(p))
print("q =", q, "->", bin(q))
print("p & q  ->", p & q, " # AND", bin(p & q))
print("p | q  ->", p | q, " # OR", bin(p | q))
print("p ^ q  ->", p ^ q, " # XOR", bin(p ^ q))
print("~p     ->", ~p, " # NOT", bin(~p))
print("p << 1 ->", p << 1, " # Left shift", bin(p << 1))
print("p >> 1 ->", p >> 1, " # Right shift", bin(p >> 1), "\n")

print("✅  End of Operators note — covers arithmetic, comparison, assignment, logical, membership, identity, and bitwise operators in detail")
