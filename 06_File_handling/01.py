import os

# Get the current working directory (optional, for verification)
current_directory = os.getcwd()
# print(f"Current working directory: {current_directory}")

# Change to a new directory (example with an absolute path)
new_directory_absolute = r"c:\Users\Dell\Desktop\PYTHON\06_File_handling"  # Replace with your desired path
os.chdir(new_directory_absolute)
# print(f"Changed to: {os.getcwd()}")


f = open("demo.txt", "r")
data = f.read()
print(data)
print("Data type = ",type(data),"\n")
f.close()# closing file is important

#if you don't want to close it 
with open("demo.txt", "r") as f:
    cont = f.read()
    print(cont,"\n")

#for reading some characters only 
f = open("demo.txt", "r")
data = f.read(6)
print("f.read(6) =",data)
print()
f.close()

#for reading line by line
f = open("demo.txt","r")
data = f.readline()
print("First line = ",data)#will come with \n by defalut
data = f.readline()
print("Next line = ",data)#cursor will move forward
data = f.readline()
print("Next line = ",data)#if no data to print then it will be empty 