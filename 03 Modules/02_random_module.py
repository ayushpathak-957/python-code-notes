print("=== Python Modules: The random Module ===\n")

print("1️⃣  The random module is used to generate random numbers or make random selections.\n")

print("🔎  Importing the module")
print("import random\n")

print("🎯  Basic random number functions")
print("➡️  random.random() = generates a random float between 0.0 and 1.0")
import random
print("Result =", random.random(), "\n")

print("➡️  random.randint(a, b) = random integer between a and b (both inclusive)")
print("Example:", random.randint(1, 10), "\n")

print("➡️  random.uniform(a, b) = random float between a and b")
print("Example:", random.uniform(10, 20), "\n")

print("🎲  Working with sequences (like lists)")
numbers = [10, 20, 30, 40, 50]
print("➡️  random.choice(seq) = randomly select one item")
print("Example:", random.choice(numbers), "\n")

print("➡️  random.choices(seq, k=n) = randomly select n items (with replacement)")
print("Example:", random.choices(numbers, k=3), "\n")

print("➡️  random.sample(seq, k=n) = randomly select n unique items (no repetition)")
print("Example:", random.sample(numbers, k=3), "\n")

print("➡️  random.shuffle(seq) = shuffle elements of the list in place")
print("Before shuffle:", numbers)
random.shuffle(numbers)
print("After shuffle:", numbers, "\n")

print("🧮  Controlling randomness with random.seed()")
print("➡️  random.seed(value) = makes results reproducible")
random.seed(10)
print("Seeded random number =", random.randint(1, 100))
random.seed(10)
print("Repeating seed gives same number =", random.randint(1, 100), "\n")

print("⚙️  Other useful functions")
print("➡️  random.randrange(start, stop, step) = like range(), but returns one random number")
print("Example:", random.randrange(0, 20, 5), "\n")

print("✅  End of random module note — covers number generation, sequences, seeding, and shuffle.")
