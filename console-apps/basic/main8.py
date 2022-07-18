import os

stdFNames = []
stdLNames = []
stdEmails = []
stdPasswords = []
stdCourses = []
courseFees = []

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def getValue(msg, listvar):
    lK = True
    while lK == True:
        val = input(f"Enter {msg}\t")
        if val != "":
            print(f"{msg} added successfully")
            listvar.append(val)
            lK = False
        else:
            print(f"{msg} cannot be empty")

def getEmail():
    lK = True
    while lK == True:
        val = input(f"Enter email ")
        if val != "":
            if val not in stdEmails:
                stdEmails.append(val)
                print(f"Email added successfully")
                lK = False
            else:
                print("Email already exists. Try again")
        else:
            print(f"email cannot be empty")

def fetchStdDetails():
    print("Find the student list below")
    if len(stdFNames) < 1:
        print("No student registered yet")
    else:
        lK = 0
        while lK < len(stdFNames):
            print(f"First Name: {stdFNames[lK]} | Last Name: {stdLNames[lK]} | Email: {stdEmails[lK]}")
            lK += 1
    restart = input("Please press enter key to restart")


def confirmUpdate(item, list, index):
    cUpd = input(f"would you like to update the {item}? y/n\t")
    if cUpd == "y" or cUpd == "Y":
        val = input("Enter the new value")
        lK = True
        while lK == True:
            if val == "":
                print("You must enter a value. Try again")
            else:
                list[index] = val
                print(f"{item} updated successfully")
                lK = False
    elif cUpd == "n" or cUpd == "N":
        pass

def doUpdate(email):
    if len(stdEmails) < 1:
        print("No student registered yet")
    else:
        lK = 0
        while lK < len(stdEmails):
            if email == stdEmails[lK]:
                confirmUpdate("first name", stdFNames, lK)
                confirmUpdate("last name", stdLNames, lK)
                confirmUpdate("password", stdPasswords, lK)
            else:
                print("email not found")

            lK += 1

def updateFee(email):
    if len(stdEmails) < 1:
        print("No student registered yet")
    else:
        lK = 0
        while lK < len(stdEmails):
            if email == stdEmails[lK]:
                confirmUpdate("fee", courseFees, lK)
            else:
                print("email not found")

            lK += 1

def removeStd(email):
    if len(stdEmails) < 1:
        print("No student registered yet")
    else:
        lK = 0
        while lK < len(stdEmails):
            if email == stdEmails[lK]:
                stdFNames.pop(lK)
                stdLNames.pop(lK)
                stdEmails.pop(lK)
                del stdPasswords[lK]
                del stdCourses[lK]
                del courseFees[lK]
                print("Student removed successfully")
            else:
                print("email not found")

            lK += 1

while True:
    print("___________________AFRIHUB Institute_____________________")
    print("Hi, what would you like to do today?")
    print("1. Add student \n2. View Students \n3. Update Student \n4. Update Fee \n5. Remove Student \n6. Quit")
    userChoice = input("Please enter your choice\t")

    if userChoice == "1":
        getValue("first name", stdFNames)
        getValue("last name", stdLNames)
        getEmail()
        getValue("password", stdPasswords)
        getValue("course", stdCourses)
        getValue("fee", courseFees)
        fetchStdDetails()

    elif userChoice == "2":
        fetchStdDetails()

    elif userChoice == "3":
        stdEmails = input("enter student email to continue \t")
        chkEmail = doUpdate(stdEmails)

    elif userChoice == "4":
        stdEmails = input("enter student email to continue \t")
        chkEmail = updateFee(stdEmails)

    elif userChoice == "5":
        stdEmails = input(" enter email to continue \t")
        chkEmail = removeStd(stdEmails)
        fetchStdDetails()

    elif userChoice == "6":
        print("See you later")
        exit()
    else:
        print("You entered a wrong input, Try again")
        restart = input("Please press enter key to restart")




