#Conditionals (if, elif, else) & (break, continue)
times = 0
limit = 5
# while(times < 5):
#     while limit > 0:
#         print("Note that the program will run for 5 times\n")
#         print(f"You have {limit} attempts left")
#         today = ""
#         choice = input("Enter the day")
#         if "mon" in choice or "Mon" in choice in choice:
#             response = input("Do you have basic programming knowledge? y/n")
#             if response  == "y":
#                 print("We have Python class today and you are eligible to attend")
#             elif response == "n":
#                 print("We have Python class today and you are not eligible")
#             else:
#                 print("You dey craze,Can't you read?")
#         elif choice == "tue" or choice == "Tue":
#             print("No Python class today")
#         elif choice == "wed" or choice == "Wed":
#             response = input("Do you have basic programming knowledge? y/n")
#             if response == "y":
#                 print("We have Python class today and you are eligible to attend")
#             elif response == "n":
#                 print("We have Python class today and you are not eligible")
#             else:
#                 print("You dey craze,Can't you read?")
#         else:
#             print(f"Your response '{choice}' is invalid. Try again")
#         limit -= 1
#     times += 1


#loops (while, for)

#
# l = 1
# print("\n\nAll odd numbers between 0 and 100")
# while(l <= 100):
#     if l > 0:
#         print(f"{l} is a sequence of 10 number")
#     l += 2
#
# l = 0
# print("\n\nAll sequence numbers between 0 and 700")
# while(l <= 700):
#     if l > 0:
#         print(f"{l} is a sequence of 10")
#     l += 10
#
# l = 0
# print("\n\nAll odd numbers between 0 and 350")
# while(l <= 350):
#     if l > 0:
#         print(f"{l} is an even number")
#     l += 25

fNames = ["Johh","Mark","Patrick","Nathan"]
lNames = ["Doe","Holding","Stones","Gordon"]

for fname in fNames:
    print(f"The first name is {fname}")

x = 0
while x < len(fNames):
    if x == 2:
        break
    print(f"The full names are {fNames[x]} {lNames[x]}")
    x += 1

x = 0
while x < len(fNames):
    x += 1
    if x == 2:
        continue
    print(f"The full names are {fNames[x]} {lNames[x]}")


