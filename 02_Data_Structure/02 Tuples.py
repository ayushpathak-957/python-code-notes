print("=== Python Data Structures: Tuples ===\n")

print("1️⃣  Tuples are ordered, immutable collections used to store multiple items.\n")

print("🔎  Syntax note:")
print("  my_tuple = (item1, item2, item3)\n")

print("🖨️  Creating tuples")
print("➡️  Simple tuple:")
t = (1, 2, 3, 4)
print("t =", t, "\n")

print("➡️  Tuple with mixed data types are also allowed:")
mixed = (1, "apple", 3.5, True)
print("mixed =", mixed, "\n")

print("➡️  Single-element tuple (needs a comma) otherwise will be stored as an int:")
single = (5,)
print("single =", single)
print("Type of single =", type(single), "\n")

print("➡️  Tuple without parentheses (tuple packing):")
packed = 10, 20, 30
print("packed =", packed, "\n")

print("➡️  Tuple unpacking:")
print("packed =", packed, "\n")
a, b, c = packed
print("a, b, c = packed")
print("a =", a, " b =", b, " c =", c, "\n")
print("Note:- \na, b,c,d = packed  --> ValueError: not enough values to unpack (expected 4, got 3)\
      \na, b = packed --> ValueError: too many values to unpack (expected 2)\n")


print("📦  Accessing tuple elements (like lists)")
t = (1, 2, 3, 4)
print("t =", t)
print("t[0] =", t[0])
print("t[-1] =", t[-1])
print("t[1:3] =", t[1:3], "\n")

print("⚙️  Tuple operations:")
print("➡️  Length =", len(t))
print("➡️  Repetition =", t * 2)
print("➡️  Membership =", 3 in t, "\n")

print("❌  Tuples are immutable:")
print("  You cannot modify, add, or remove items once created.\n")

print("🎯  However, you can create new tuples from existing ones:")
print("new_t = t + (5, 6)")
new_t = t + (5, 6)
print("new_t =", new_t, "\n")

print("🔄  Tuple methods:")
print("  count(value) -> returns how many times a value appears")
print("  index(value) -> returns the first index of value\n")

nums = (1, 2, 2, 3, 3, 4)
print("nums =", nums)
print("nums.count(2) =", nums.count(2))
print("nums.index(3) =", nums.index(3), "\n")

print("🧩  More on index() method")
print("  - index() returns only the index of the first occurrence of the given value.")
print("  - You can also specify start and stop positions: index(value, start, stop)\n")

nums = (1, 2, 3, 2, 4, 2, 5)
print("nums =", nums)
print("nums.index(2) =", nums.index(2))
print("nums.index(2, 2) =", nums.index(2, 2))
print("nums.index(2, 3, 6) =", nums.index(2, 3, 6), "\n")

print("🔍  Getting all indexes of a value using enumerate()")
print("  - enumerate(iterable) returns pairs (index, value) while iterating.")
print("  - We can filter indexes where the value matches the target.\n")

# Using list comprehension
indexes = [i for i, val in enumerate(nums) if val == 2]
print("All indexes of 2 (list comprehension) =", indexes)

# Using a simple loop
positions = []
for i, val in enumerate(nums):
    if val == 2:
        positions.append(i)
print("All indexes of 2 (loop method) =", positions, "\n")
print("enumerate(nums) produces (index, value) for each element.\
      \nList comprehension [i for i, val in enumerate(nums) if val == 2] collects all indexes where value is 2.\\nWorks with tuples, lists, or strings.\
      \nUseful when index() alone is insufficient because it only returns the first occurrence.\n")


print("📜  Nested tuples (tuple inside another tuple):")
nested = (1, (2, 3), (4, (5, 6)))
print("nested =", nested)
print("nested[1][1] =", nested[1][1])
print("nested[2][1][0] =", nested[2][1][0], "\n")

print("🧠  Tuple advantages:")
print("  ✅ Faster than lists")
print("  ✅ Can be used as dictionary keys (hashable)")
print("  ✅ Good for fixed data (coordinates, config, etc.)\n")

print("✅  End of Tuples note — covered creation, access, operations, methods, nesting, and properties.")
