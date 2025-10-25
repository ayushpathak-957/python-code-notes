print("=== Python Basics: The print() Function ===\n")

print("1️⃣  The print() function displays output on the screen.\n")

print("🔎  Syntax note:")
print("  print(*objects, sep=' ', end='\\n') \n")

print("🖨️  Simple examples")
print("➡️  Single value:")
print("Hello, Python!\n")

print("➡️  Multiple values with default separator:")
print("Python", "is", "fun!\n")

print("➡️  Using sep to join values:")
print("2025", "10", "26", sep="-")
print("Hello", "World", sep=" | ", end=" ✅\n\n")

print("➡️  Using end to avoid newline:")
print("Loading", end="... ")
print("Done\n")

print("📜  Triple quotes (''' string ''') for multi-line strings")
print('''Line 1
Line 2
Line 3
      ''')

print("⚠️  Escape sequences (use \\ to escape special characters):")
print("  \\n  -> new line")
print("  \\t  -> tab")
print("  \\'  -> single quote")
print('  \\"  -> double quote')
print("  \\\\  -> backslash\n")

print("🎯  Examples of escape sequences and quotes\n")
print("➡️  print('Hello\\nWorld') -> ")
print("Hello\nWorld\n")
print("➡️  print('Hello\\tWorld') -> ")
print("Hello\tWorld\n")
print("➡️  print('She said \\'Hi\\'') -> ")
print("She said 'Hi'\n")
print("➡️  print(\"He said \\\"Hello\\\"\") -> ")
print('He said "Hello"\n')

print("🔐  Raw strings (useful for paths or regex)")
print(r"C:\newfolder\test\n")
print("\n✅  End of print() note — covers print, quotes, triple quotes, and escape sequences")
