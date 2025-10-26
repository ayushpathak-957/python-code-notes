print("=== Python Data Structures: Sets ===\n")

print("1️⃣  A set is an unordered collection of unique elements.\n")

print("🔎  Syntax note:")
print("  my_set = {item1, item2, item3}\n")

print("🖨️  Creating sets")
print("➡️  Simple set:")
fruits = {"apple", "banana", "cherry", "apple"}
print("fruits =", fruits, "  # duplicates removed automatically\n")

print("➡️  Using set() constructor:")
numbers = set([1, 2, 3, 2, 4])
print("numbers =", numbers, "\n")

print("📏  Accessing elements")
print("  Sets are unordered, so indexing/slicing is not supported.")
print("  You can loop through elements:")
for item in fruits:
    print(item, end=" ")
print("\n")

print("➕  Adding elements")
fruits.add("mango")
print("After add('mango'):", fruits)
fruits.update(["kiwi", "orange"])
print("After update(['kiwi','orange']):", fruits, "\n")

print("➖  Removing elements")
fruits.remove("banana")
print("After remove('banana'):", fruits)
fruits.discard("pineapple")  # no error if element not present
print("After discard('pineapple'):", fruits)
popped_item = fruits.pop()
print("Popped item =", popped_item)
print("After pop():", fruits, "\n")

print("🔄  Set operations")
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("A =", A, " B =", B)
print("Union: A | B =", A | B)
print("Intersection: A & B =", A & B)
print("Difference: A - B =", A - B)
print("Symmetric Difference: A ^ B =", A ^ B, "\n")

print("🎯  Useful methods")
print("len(set) -> number of elements")
print("in -> membership test")
print("clear() -> empties set")
print("copy() -> returns shallow copy")
print("isdisjoint(), issubset(), issuperset() -> set relationships\n")

print("🧠  Advanced Set Operations\n")

print("➡️  Set comprehension (creating sets in one line)")
squares = {x**2 for x in range(6)}
print("squares =", squares, "\n")

print("➡️  frozenset – immutable set (cannot add/remove elements)")
immutable_set = frozenset([1, 2, 3, 2])
print("immutable_set =", immutable_set, "\n")

print("➡️  Converting between list and set")
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)
print("From list to set (removes duplicates):", unique_set)
new_list = list(unique_set)
print("From set back to list:", new_list, "\n")

print("➡️  Checking relationships between sets")
A = {1, 2, 3}
B = {2, 3, 4}
print("A =", A, " B =", B)
print("A.isdisjoint(B) ->", A.isdisjoint(B))
print("A.issubset(B) ->", A.issubset(B))
print("B.issuperset(A) ->", B.issuperset(A), "\n")

print("🎯  Summary of key set points")
print("• Sets are unordered, mutable, and only store unique elements")
print("• No indexing or slicing")
print("• Use add(), update(), remove(), discard(), pop() to modify")
print("• Union(|), Intersection(&), Difference(-), Symmetric Difference(^)")
print("• frozenset is immutable")
print("• Set comprehension for concise creation")
print("• Convert list -> set to remove duplicates, set -> list to restore order\n")

print("✅  End of Sets note — covers creation, access (iteration), modification, operations, advanced operations, comprehension, frozenset, and conversions.")
