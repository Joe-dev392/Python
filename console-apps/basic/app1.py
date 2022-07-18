"""
search and replace console app
"""
while(True):

    print("################# Search & Replace ####################")
    userString = input("Please enter your desired string to continue:\n")

    userChoice = input("Would you like to replace anything in your string?" 'y/n')
    if userChoice == 'y':
        oldString = input("Please provide the string to be replaced\t")
        newString = input("Please provide the new string\t")
        newUserStr = userString.replace(oldString, newString)
        print("The replacement was done successfully.  See the summary below")
        print(f"OLD String({len(userString)} chars):\n {userString}")
        print(f"NEW string({len(newUserStr)} chars):\n {newUserStr}")
    elif userChoice =='n' or userChoice == 'N' :
        print("Kindly find your string below:\n"+userString)
        print("\n\nThank you for using our app, see you soon")
    else:
        print("You are expected to enter 'y' or 'n'")
    restart = input("Press 'c' or 'q' to terminate or press 'enter' to continue:\n ")
    if restart == "c" or restart == "q":
        break