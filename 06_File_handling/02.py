import os
new_directory_absolute = r"c:\Users\Dell\Desktop\PYTHON\06_File_handling"
os.chdir(new_directory_absolute)


#this mode will create a new file or deleting the content of previous file and write it fresh
f = open("text.txt","w")
f.write("This is a new file")
f.write("Adding something")#the add will be appended at the end of the line as no \n was given
f.close()

f = open("text.txt","r")
print(f.read())
f.close()

f = open("text.txt","w")
f.write("Adding a new line")
f.close()

f = open("text.txt","r")
print("\ntext.txt is now line")
print(f.read())#note that the previous written things are gone
f.close()