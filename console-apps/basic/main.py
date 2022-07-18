# print("Welcome to my App")
# print("*****************")
#
# fName = input("Enter your first name\t")
# lName = input("Enter your last name\t")
# age = input("How old are you\t")
#
# print("\n\nThanks for your response, kindly find the summary below\n\n")
# print(f"Your name is {fName} {lName} and you are {age} yrs old")

#Global variable
# price = 25
#
# def getTotalPrice():
#     global price
#     price = 555
#     return price
#
# print(f"Price is {getTotalPrice()}")

#python strings

name = "Tyler joseph"
bio = """
asdsadasdasd
sadsds
dsdfsfd
dfdfdfd
"""
print(name[5]+"\n"+bio[12])

# for letter in name:
#     print(letter)

#getting string lenght len(str)
print(f"My bio contains {len(bio)} letters")

#checking for a value in string "in" | value not in string "not in"
print("onsep"not in name)

#slicing string "[i:i]"
file = "beach-bg.png"
subName = file[-9:]
# print(subName)
if subName == '.png':
    print("Well done")
else:
    print("Mtchewwwww Abeg gettat")

#string modification e.g casing, replacing, split etc.
print(name.capitalize())

print(name.replace("Tylerjoseph", "Nissan"))

print(name.split(" "))

