import os
bTitle = []
bAuthor = []
bCategory = []
dCreated = []
tComms = []

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def getInfo(msg,provar):
    bl = True
    while bl == True:
        val = input(f'Enter {msg} \t')
        if val != '':
            print(f'{msg} added succesfully')
            provar.append(val)
            bl = False
        else:
            print(f'{msg} cannot be empty')

def getTit():
    bl = True
    while bl == True:
        val = input(f"Enter blog title\t")
        if val != "":
            if val not in bTitle:
                bTitle.append(val)
                print(f"blog title added successfully")
                bl = False
            else:
                print("blog title already exists alaye. Try again")
        else:
            print(f"Blog Title cannot be empty")

def getBlDetails():
    print('Find the blog details below')
    if len(bTitle) < 1:
        print('There has been no registered blog title')
    else:
        bl = 0
        while bl < len(bTitle):
            print(f'Blog Title: {bTitle[bl]} | Blog Author: {bAuthor[bl]} | Blog Category: {bCategory[bl]} | Date Created: {dCreated[bl]} | Total Comments: {tComms[bl]}')
            bl += 1
    restart = input('Please press the enter key to restart')

def confirmBlUpdate(item, list, index):
    cUpd =input(f'would you like to update {item}? y/n\t')
    if cUpd == 'Y' or cUpd == 'y':
        val = input('Enter your value boss\t')
        bl = True
        while bl == True:
            if val == '':
                print('dondore you must enter a value. Try again')
            else:
                list[index] = val
                print(f'{item} updated successfully')
                bl = False
    elif cUpd == 'N' or cUpd == 'n':
        pass

def blUpdate(title):
    if len(bTitle) < 1:
        print('Blog Title not found')
    else:
        bl = 0
        while bl < len(bTitle):
            if title == bTitle[bl]:
                confirmBlUpdate('blog author', bAuthor, bl)
                confirmBlUpdate('blog category', bCategory, bl)
                confirmBlUpdate('yours comments', tComms, bl)
                confirmBlUpdate('date changes were made', dCreated, bl)
            else:
                print('this blog title does not exist')
            bl += 1



def removeBl(title):
    if len(bTitle) < 1:
        print("No blog title registered yet")
    else:
        bl = 0
        while bl < len(bTitle):
            if title == bTitle[bl]:
                bAuthor.pop(bl)
                bCategory.pop(bl)
                dCreated.pop(bl)
                tComms.pop(bl)
                print("blog title removed successfully")
            else:
                print("blog title not found")
            bl += 1


while True:
    print("_____________ Ocmade Institute ___________")
    print("Hi, what would you like to do today?")
    print("1. Add Blog \n2. View Blog Details \n3. Update Blog Details \n4. Remove Blog \n5. Quit")
    userChoice = input("Please enter your choice\t")

    if userChoice == '1':
        getTit()
        getInfo('blog author',bAuthor)
        getInfo('blog category',bCategory)
        getInfo('date created',dCreated)
        getInfo('total comments',tComms)
        getBlDetails()

    elif userChoice == '2':
        getBlDetails()

    elif userChoice == "3":
        bTit = input("enter blog title to continue \t")
        chkTitle = blUpdate(bTit)

    elif userChoice == "4":
        bTit = input("enter blog title to continue \t")
        chkTitle = removeBl(bTit)
        getBlDetails()

    elif userChoice == "5":
        print("See you later")
        exit()

    else:
        print("You entered a wrong input, Try again")
        restart = input("Please press enter key to restart")
