#Python Functions / Methods

def validateInput(strInput):
    if "." not in strInput:
        response = "The file name is invalid. '.' is missing"
    else:
        response = strInput
    return response

def calculate(num1=0, num2=0, operation="sum"):
    if operation == "a":
        result = num1 + num2
    elif operation == "d":
        result = float(num1/num2)
    elif operation == "m":
        result = num1 * num2
    elif operation == "s":
        result = num1 - num2

    return result

def calculator(choice):
    if choice == 1:
        num1 = int(input("Please enter the first operand\t"))
        num2 = int(input("Please enter the second operand\t"))
        retvalue = calculate(num1,num2,"a")
    elif choice == 2:
        num1 = int(input("Please enter the first operand\t"))
        num2 = int(input("Please enter the second operand\t"))
        retvalue = calculate(num1,num2,"d")
    elif choice == 3:
        num1 = int(input("Please enter the first operand\t"))
        num2 = int(input("Please enter the second operand\t"))
        retvalue = calculate(num1,num2,"m")


    elif choice == 4:
        num1 = int(input("Please enter the first operand\t"))
        num2 = int(input("Please enter the second operand\t"))
        retvalue = calculate(num1,num2,"s")
    else:
        retvalue = "Wrong input encountered. Please enter 1 or 2 or 3 or 4"

    return retvalue


# userInput = input("Enter a valid filename")
# if userInput != "":
#     returned = validateInput(userInput)
#     print(returned)
# print(validateInput)

print("My simple calculator. Select an operator to continue")
choice = int(input("1. Addition \n2. Division \n3. Multiplication \n4. Subtraction \n\nEnter choice:\t"))

print(calculator(choice))


