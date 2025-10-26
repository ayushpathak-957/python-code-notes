print("=== 📁  Python OS Module ===\n")

print("🧠  The os module lets us interact with the operating system.")
print("We can manage files, folders, paths, and system information.\n")

print("📦  Importing the module")
print("import os\n")

import os

print("📍  Get Current Working Directory")
print("os.getcwd() =", os.getcwd(), "\n")

print("📂  List all files and folders in current directory")
print("os.listdir() =", os.listdir(), "\n")

print("🗂️  Create and remove a folder")
folder = "demo_folder"
if not os.path.exists(folder):
    os.mkdir(folder)
    print("✅  Folder created:", folder)
else:
    print("⚠️  Folder already exists:", folder)

# Create a test file inside the folder
file_path = os.path.join(folder, "sample.txt")
with open(file_path, "w") as f:
    f.write("This is a demo file created for OS module notes.")

print("📝  File created at:", file_path, "\n")

print("🧩  Check if file exists")
print("os.path.exists(file_path) =", os.path.exists(file_path), "\n")

print("📍  Get absolute path of the file")
print("os.path.abspath(file_path) =", os.path.abspath(file_path), "\n")

print("📄  Split the path into folder and file name")
print("os.path.split(file_path) =", os.path.split(file_path), "\n")

print("🔤  Split file name and extension")
print("os.path.splitext(file_path) =", os.path.splitext(file_path), "\n")

print("✏️  Rename the file")
new_path = os.path.join(folder, "renamed_sample.txt")
os.rename(file_path, new_path)
print("File renamed to:", new_path, "\n")

print("🧱  Get OS type name (posix / nt / etc.)")
print("os.name =", os.name, "\n")

print("🎯  Common os.path functions:")
print("➡️ os.path.basename(path)  = returns file name only")
print("➡️ os.path.dirname(path)   = returns directory name only")
print("➡️ os.path.getsize(path)   = returns file size in bytes")
print("➡️ os.path.exists(path)    = checks if path exists\n")

# Pause before cleanup so you can see the folder/files
input("⏸️  Press Enter when you are ready to delete the demo folder and file...\n")

# Cleanup
os.remove(new_path)
os.rmdir(folder)
print("✅  Cleanup done — deleted file and folder.\n")

print("✅  End of OS module notes — covers paths, files, and directories.")
