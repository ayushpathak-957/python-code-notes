import os
new_directory_absolute = r"c:\Users\Dell\Desktop\PYTHON\06_File_handling"
os.chdir(new_directory_absolute)
# 🧭 FILE HANDLING: seek() and tell()

# 📌 tell() → shows current cursor position (in bytes)
f = open("demo.txt", "r")
print(f.tell())       # Shows current position → usually 0 at start
data = f.read(5)      # Reads first 5 characters
print(f.tell())       # Shows new position after reading
f.close()

"""
💡 Explanation:
- Cursor starts at position 0.
- After reading some characters, it moves ahead.
- tell() helps track where you are in the file.
"""


# 🧲 seek(offset, whence) → moves cursor to specific position
f = open("demo.txt", "r")
f.seek(0)             # Moves cursor to start
data = f.read(5)      # Reads first 5 characters
print(data)

f.seek(0)             # Move back to start again
data2 = f.read()      # Reads the entire file again
print("🫴",data2)
f.close()

"""
💡 Explanation:
- seek(0) → moves cursor to beginning.
- seek(10) → moves cursor to 10th byte.
- seek(0, 2) → moves cursor to end of file.
"""


# 🧮 seek() parameters:
"""
seek(offset, whence)

| Parameter  | Meaning                    | Example                   |
|------------|----------------------------|---------------------------|
| offset     | bytes to move              | seek(5) → move 5 bytes    |
| whence     | reference point (default=0)| 0=start, 1=current, 2=end |

📍Examples:
f.seek(0, 2) → Move cursor to end of file
f.seek(0)    → Move cursor to start of file
"""


# ⚙️ Practical Example:
with open("demo.txt", "r") as f:
    print("Initial position:", f.tell())
    content = f.read(5)
    print("After reading 5 chars:", f.tell())

    f.seek(0)  # Move cursor back to start
    print("After seek(0):", f.tell())

    print("Full content again:", f.read())

"""
🧠 Summary:
- tell() → find where the cursor is.
- seek() → control where the cursor goes.
- Together → give you full control of file navigation!
"""
