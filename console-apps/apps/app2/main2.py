import os
pID = []
pName = []
pCategory = []
pPrice = []


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def getInfo(msg,provar):
    pr = True
    while pr == True:
        val = input(f'Enter {msg} \t')
        if val != '':
            print(f'{msg} added succesfully')
            provar.append(val)
            pr = False
        else:
            print(f'{msg} cannot be empty')

def getID():
    pr = True
    while pr == True:
        val = input(f"Enter product Id\t")
        if val != "":
            if val not in pID:
                pID.append(val)
                print(f"product Id added successfully")
                pr = False
            else:
                print("product Id already exists alaye. Try again")
        else:
            print(f"product Id cannot be empty")

def getPrDetails():
    print('Find the product details below')
    if len(pName) < 1:
        print('There has been no registered product')
    else:
        pr = 0
        while pr < len(pName):
            print(f'Product ID: {pID[pr]} | Product Name: {pName[pr]} | Product Category: {pCategory[pr]} | Product Price: {pPrice[pr]}')
            pr += 1
    restart = input('Please press the enter key to restart')

def confirmPrUpdate(item, list, index):
    cUpd =input(f'would you like to update {item}? y/n\t')
    if cUpd == 'Y' or cUpd == 'y':
        val = input('Enter your value boss\t')
        pr = True
        while pr == True:
            if val == '':
                print('dondore you must enter a value. Try again')
            else:
                list[index] = val
                print(f'{item} updated successfully')
                pr = False
    elif cUpd == 'N' or cUpd == 'n':
        pass

def prUpdate(id):
    if len(pID) < 1:
        print('Product not found')
    else:
        pr = 0
        while pr < len(pID):
            if id == pID[pr]:
                confirmPrUpdate('product name', pName, pr)
                confirmPrUpdate('product category', pCategory, pr)
                confirmPrUpdate('product price', pPrice, pr)
            else:
                print('this product Id does not exist')
            pr += 1

def updPrdPrice(id):
    if len(pID) < 1:
        print('No product Id registered yet')
    else:
        pr = 0
        while pr < len(pID):
            if id == pID[pr]:
                confirmPrUpdate('product price', pPrice, pr)
            else:
                print('product Id does not exist boss')
            pr += 1

def removePrd(id):
    if len(pID) < 1:
        print("No product Id registered yet")
    else:
        pr = 0
        while pr < len(pID):
            if id == pID[pr]:
                pName.pop(pr)
                pCategory.pop(pr)
                pID.pop(pr)
                print("product removed successfully")
            else:
                print("product not found")
            pr += 1


while True:
    print("_____________ Ocmade Institute ___________")
    print("Hi, what would you like to do today?")
    print("1. Add Product \n2. View Product Details \n3. Update Product \n4. Update Price \n5. Remove Product \n6. Quit")
    userChoice = input("Please enter your choice\t")

    if userChoice == '1':
        getInfo('product name',pName)
        getInfo('product category',pCategory)
        getInfo('product price',pPrice)
        getID()
        getPrDetails()

    elif userChoice == '2':
        getPrDetails()

    elif userChoice == "3":
        pId = input("enter product Id to continue \t")
        chkID = prUpdate(pId)

    elif userChoice == "4":
        pId = input("enter product Id to continue \t")
        chkID = updPrdPrice(pId)

    elif userChoice == "5":
        pId = input("enter product  Id to continue \t")
        chkID = removePrd(pId)
        getPrDetails()

    elif userChoice == "6":
        print("See you later")
        exit()

    else:
        print("You entered a wrong input, Try again")
        restart = input("Please press enter key to restart")
