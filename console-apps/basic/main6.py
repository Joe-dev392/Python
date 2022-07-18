import os
#File Handling
file = open("Sample.txt", "r")

print(file.read())

myTxt = open("c:\\Users\\Tyler\\Music\\DDYtxt.txt ", "r")



file.close()

file = open("Sample.txt", "a")
file.write("\nI will be appended at the end of the file")
file.close()
file = open("sample.txt", "r")
print(file.read())
file.close()

if os.path.exists("sample.txt"):
    os.remove("sample.txt")
else:
    print("No such file encountered")