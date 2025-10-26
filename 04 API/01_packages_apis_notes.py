print("=== 📦 Python Packages & APIs ===\n")

print("🧠  Packages in Python are collections of modules organized in directories.")
print("They help organize code logically and allow reuse.\n")

print("📦  Using packages")
print("You can import modules from packages using:")
print("➡️ import package_name.module_name")
print("➡️ from package_name import module_name\n")

# Example: Using a built-in package
print("📌 Example: Using 'os' module from standard package")
import os
print("Current working directory using os module:", os.getcwd(), "\n")

print("🛠️  Installing third-party packages")
print("➡️ pip install package_name\n")

print("📌 Example: Using 'requests' package for APIs")
try:
    import requests
except ImportError:
    print("⚠️  'requests' package not installed. You can install it using pip.\n")

print("🌐  APIs (Application Programming Interfaces)")
print("APIs allow your Python program to interact with external services or software.")
print("For example, you can fetch data from websites, databases, or other apps.\n")

print("🔗  Using APIs with 'requests' package")
print("Syntax to make a GET request:")
print("➡️ response = requests.get('https://api.example.com/data')\n")

# Example of GET request (pseudo-code, can run if requests installed)
if 'requests' in globals():
    print("Fetching data from example API (dummy test)...")
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json(), "\n")

print("📌  Common API response handling")
print("➡️ response.status_code   # check HTTP status")
print("➡️ response.json()       # parse JSON data")
print("➡️ response.text         # get raw response text\n")

print("📝  Summary")
print("1️⃣  Packages are collections of modules.")
print("2️⃣  APIs allow interaction with external systems.")
print("3️⃣  Use 'requests' or similar packages to call APIs.")
print("4️⃣  Always handle API responses and errors properly.\n")

print("✅  End of Packages & APIs notes — ready for practical API exercises.")
