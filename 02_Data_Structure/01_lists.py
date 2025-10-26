print("=== Python Data Structures: Lists ===\n")

print("1️⃣  A list is an ordered, mutable collection that can hold multiple items.\n")

print("🧱  Creating lists")
print("fruits = ['apple', 'banana', 'cherry']")
print("numbers = [1, 2, 3, 4, 5]")
print("mixed = [1, 'apple', True, 3.14]\n")

fruits = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3, 4, 5]
mixed = [1, 'apple', True, 3.14]

print("📏  Accessing elements")
print("fruits[0] =", fruits[0])
print("fruits[-1] =", fruits[-1], "\n")

print("🔍  Slicing lists")
print("fruits[0:2] =", fruits[0:2], " (elements from index 0 to 1)")
print("fruits[:2] =", fruits[:2], " (from start to index 1)")
print("fruits[1:] =", fruits[1:], " (from index 1 to end)")
print("fruits[::2] =", fruits[::2], " (every 2nd element)\n")

print("🧩  Modifying lists")
print("➡️  Changing elements")
print("Before:", fruits)
fruits[1] = "mango"
print("After:", fruits)
print(" (alters original list)\n")

print("➕  Adding elements")
print("append(x)  – adds to end (alters original)")
fruits.append("orange")
print("After append:", fruits)
print("insert(i, x)  – inserts at index (alters original)")
fruits.insert(1, "kiwi")
print("After insert:", fruits, "\n")

print("➖  Removing elements")
print("remove(x)  – removes first occurrence (alters original)")
fruits.remove("apple")
print("After remove:", fruits)
print("pop()  – removes and returns last element (alters original)")
print("Popped item =", fruits.pop())
print("After pop:", fruits)
print("del  – deletes by index or slice (alters original)")
del fruits[0]
print("After del:", fruits)
print("clear()  – empties the list (alters original)")
fruits.clear()
print("After clear:", fruits, "\n")

fruits = ['apple', 'banana', 'cherry', 'banana']

print("🔁  Searching in a list")
print("in  – checks if element exists (returns boolean)")
print("'banana' in fruits =", 'banana' in fruits)
print("'grape' in fruits =", 'grape' in fruits)
print("index(x)  – returns first index of value (raises error if not found)")
print("fruits.index('banana') =", fruits.index('banana'))
print("find()  – does not exist for lists, only for strings (index gives error if not found)\n")

print("🔢  Counting elements")
print("count(x)  – returns number of occurrences (returns integer)")
print("fruits =", fruits)
print("fruits.count('banana') =", fruits.count('banana'), "\n")

numbers = [5, 2, 9, 1, 5, 6]
print("⚙️  Sorting and reversing")
print("sort()  – sorts list in place (alters original)")
numbers.sort()
print("After sort:", numbers)
print("sorted(list)  – returns new sorted list (does not alter original)")
print("sorted(numbers, reverse=True) =", sorted(numbers, reverse=True))
print("reverse()  – reverses list (alters original)")
numbers.reverse()
print("After reverse:", numbers, "\n")

print("🧮  Other useful methods")
nums = [1, 2, 3]
print("extend(iterable)  – adds elements from another list (alters original)")
nums.extend([4, 5])
print("After extend:", nums)
print("copy()  – returns shallow copy (does not alter original)")
nums_copy = nums.copy()
print("nums_copy =", nums_copy, "\n")

print("🧠  List comprehension (shorter way to create lists)")
print("squares = [x**2 for x in range(5)]")
squares = [x**2 for x in range(5)]
print("Result =", squares, "\n")

print("🎯  Quick recap")
print("•  append(x)- adds at end (alters)")
print("•  insert(i, x)- adds at index (alters)")
print("•  remove(x), pop(), del- remove items (alters)")
print("•  clear()- empties list (alters)")
print("•  copy() - returns new list")
print("•  extend()- merges lists (alters)")
print("•  sort(), reverse()- alter original list")
print("•  count(x), index(x)- return values (don’t alter)\n")

print("✅  End of list notes — covers creation, access, slicing, modification, searching, sorting, and comprehension.")
