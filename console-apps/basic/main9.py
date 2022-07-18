import os, platform
global stdList
stdList = ["Nisan Dave", "John Doe", "Jane Doe"]

def runApp():
    x = "#" * 30
    y = "=" * 30
    global exitMsg
    exitMsg = f"\n{x} \n{y} \n==> Built by <==\n==> Joseph Yakubu <== \n{x} \n{y}"
    print("""
        --------------------------------------------
        |__________________________________________|
        |====== Welcome User, How can we help =====|
        |==========================================|
        ********************************************
        Enter 1: To View all Students
        Enter 2: To Add new Student
        Enter 3: To Remove Student
        Enter 4: To Find Student(s)
        """)

    try:
        userInput = int(input("Please enter an option "))
    except ValueError:
        exit("Idiot. You are supposed to type a number \nCome back when you've had yourself checked @ Aro")
    else:
        print("\n")

    if(userInput == 1): #view
        print("Student list\n")
        for std in stdList:
            print(f"=> {std}")
    elif(userInput == 2): #add
        newStd = input("Enter student name ")
        if newStd in stdList:
            print(f"Student with name {newStd} exists")
        else:
            stdList.append(newStd)
            print(f"\nStudent {newStd} added successfully as shown in the list below ")
            for std in stdList:
                print(f"=> {std}")

    elif(userInput == 3): #remove
        stdName = input("Enter the student name ")
        if stdName in stdList:
            stdList.remove(stdName)
            print(f">= Student {stdName} removed successfully")
            for std in stdList:
                print(f"=> {std}")
        else:
            print(f"Student {stdName} not found")

    elif(userInput == 4): #find
        stdName = input("Enter the student name ")
        if stdName in stdList:
            print(f"Student {stdName} exists")
        else:
            print(f"Student {stdName} not found")

    elif(userInput < 1 or userInput > 4):
        print("Invalid option encountered")

runApp()

def restartApp():
    restart = input("Restart app? y/n ")
    if restart.lower() == 'y':
        if platform.system() == 'Windows':
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        runApp()
        restartApp()
    else:
        quit(exitMsg)
restartApp()