import os
new_directory_absolute = r"c:\Users\Dell\Desktop\PYTHON\06_File_handling"
os.chdir(new_directory_absolute)

print("""All the modes
| Mode  | Description                  | Readable    | Writable   | Cursor Position | Truncates File |
|--------|-----------------------------|-------------|------------|-----------------|----------------|
| 'r'    | Read only                   | ✅ Yes     | ❌ No      | Start           | ❌ No          |
| 'r+'   | Read and write              | ✅ Yes     | ✅ Yes     | Start           | ❌ No          |
| 'w'    | Write only (creates new)    | ❌ No      | ✅ Yes     | Start           | ✅ Yes         |
| 'w+'   | Read and write (creates new)| ✅ Yes     | ✅ Yes     | Start           | ✅ Yes         |
| 'a'    | Append only                 | ❌ No      | ✅ Yes     | End             | ❌ No          |
| 'a+'   | Read and append             | ✅ Yes     | ✅ Yes     | End*            | ❌ No          |
""")



f = open("text.txt","r+")#will read and add data
f.write("Hello There !")#this will over write on the previous content
print(f.read())