print("=== Python Data Structures: Dictionaries ===\n")

print("1️⃣  A dictionary is an unordered collection of key-value pairs.\n")

print("🔎  Syntax note:")
print("  my_dict = {'key1': value1, 'key2': value2}\n")
print("  Keys must be immutable (str, int, tuple, etc.)")
print("  Values can be any type (mutable or immutable)\n")

print("🖨️  Creating dictionaries")
print("➡️  Simple dictionary:")
person = {'name': 'Ayush', 'age': 20, 'city': 'Delhi'}
print("person =", person, "\n")

print("➡️  Using dict() constructor:")
info = dict(name="Alice", age=25, city="Mumbai")
print("info =", info, "\n")

print("📏  Accessing elements")
print("➡️ Using key indexing:")
print("person['name'] =", person['name'])
print("➡️ Using get() method (safe access, can provide default):")
print("person.get('age') =", person.get('age'))
print("person.get('country', 'Not specified') =", person.get('country', 'Not specified'), "\n")

print("✏️  Adding or modifying elements")
person['age'] = 21
print("Modified age:", person)
person['country'] = 'India'
print("Added country:", person, "\n")

print("➖  Removing elements")
print("➡️ Using del:")
del person['city']
print("After del person['city']:", person)
print("➡️ Using pop() (returns the removed value):")
popped_value = person.pop('age')
print("popped_value =", popped_value)
print("After pop('age'):", person)
print("➡️ Using popitem() (removes last inserted key-value pair):")
last_item = person.popitem()
print("popitem() returned:", last_item)
print("After popitem():", person)
print("➡️ Using clear():")
person.clear()
print("After clear():", person, "\n")

print("🔄  Dictionary methods")
person = {'name': 'Ayush', 'age': 20, 'city': 'Delhi'}
print("person =", person)
print("➡️ keys() -> returns all keys:", person.keys())
print("➡️ values() -> returns all values:", person.values())
print("➡️ items() -> returns key-value pairs:", person.items())
print("➡️ copy() -> returns a shallow copy:", person.copy())
print("➡️ len() -> number of items:", len(person))
print("➡️ 'key' in person -> membership test:", 'name' in person, "\n")

print("🌀  Iterating through dictionary")
print("➡️ Using keys():")
for key in person.keys():
    print(key, "->", person[key])
print("\n➡️ Using values():")
for value in person.values():
    print(value, end=" ")
print("\n\n➡️ Using items():")
for key, value in person.items():
    print(key, "->", value)
print()

print("📦  Nested dictionaries")
nested_dict = {
    'student1': {'name': 'Alice', 'age': 21},
    'student2': {'name': 'Bob', 'age': 22}
}
print("nested_dict =", nested_dict)
print("nested_dict['student1']['name'] =", nested_dict['student1']['name'])
print("nested_dict['student2']['age'] =", nested_dict['student2']['age'], "\n")

print("🧠  Dictionary comprehension")
squares = {x: x**2 for x in range(6)}
print("squares =", squares)
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
age_dict = {name: age for name, age in zip(names, ages)}
print("age_dict (from two lists using zip) =", age_dict, "\n")

print("🎯  Summary of key dictionary points")
print("• Dictionaries store key-value pairs (keys immutable, values can be anything)")
print("• Access using [] (may raise KeyError) or get() (safe, can set default)")
print("• Add/modify using key assignment")
print("• Remove using del, pop(), popitem(), or clear()")
print("• Methods: keys(), values(), items(), copy(), len(), 'in' for membership")
print("• Iteration: via keys(), values(), or items()")
print("• Can be nested for complex structures")
print("• Dictionary comprehensions allow quick creation from iterables or zipped lists\n")

print("✅  End of Dictionaries note — covers creation, access, modification, removal, methods, iteration, nesting, and comprehension.")
