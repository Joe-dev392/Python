#Dictionary - varName = {key: value,,,,,,}

studentDetails = {
    "ID": "STD-0101",
    "Name": "John Bull",
    "Email": "jbull@google.go",
    "Age": 26,
    "Alumni": False,
    "Courses": ["PMP", "CCNA", "OSD"],
    "Height": 5.4
}
stdName = studentDetails['Name']
# for item in studentDetails['Courses']:
# stdCourses = studentDetails["Courses"][0:]
print("Student" + stdName+ "has email " +studentDetails['Email'])

print(studentDetails.keys())
print(studentDetails.values())
print(studentDetails.items())

studentDetails["Gender"] = "Bob Risky"
studentDetails["Name"] = "Tyler"
if "Gender" in studentDetails:
    print("Gender record exists")
else:
    print("Gender record not found")


print(studentDetails)


studentDetails.update({"Gender": "Male"})
print(studentDetails)

studentDetails.pop("Alumni")
print(studentDetails)

studentDetails.popitem()
print(studentDetails)

studentDetails.popitem()
print(studentDetails)

studentDetails.popitem()
print(studentDetails)

studentDetails.popitem()
print(studentDetails)

del studentDetails["ID"]
# del studentDetails

# studentDetails.clear()


print("The student details are shown below")
for dataItem in studentDetails:

    print(studentDetails[dataItem])

for item in studentDetails.values():
    print(item)

for key, val in studentDetails.items():
    print(key, val)


#Nesting Dictionaries

students = {
    "Student1": {
        "Name": "John Doe",
        "Course": "Computer Science",
        "Email": "jdoe@doe.doe"
    },
    "Student2": {
        "Name": "Jane Doe",
        "Course": "Computer Engineering",
        "Email": "janedoe@doe.doe"
    }
}

student2 = students["Student2"]
print(student2["Course"])

