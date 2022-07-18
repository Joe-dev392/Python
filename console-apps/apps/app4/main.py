class Library:
    def __init__(self, booklist):
        self.books = booklist

    def displayAvailableBooks(self):
        print(f"There are many {len(self.books)} books available")
        for book in self.books:
            print(f"==> {book}")

    def checkOutBooks(self, name, bookName):
        pass

    def checkInBooks(self, bookName):
        pass

    def populateBookList(self, bookName):
        pass




class Person():
    def issueBook(self):
        pass

    def returnBook(self):
        pass

    def addBook(self):
        pass

if __name__ == '__main__':
    wuseLibrary = Library(['General Maths', 'Programming Fundemantals', 'Ikemefuna'])
    individual = Person()

    print("<======== Wuse Digital Libraary ========>")
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    print("\nWelcome user, what would you like to accomplish today?")
    print("\n1. View Book List \n2. Check out a book \n3. Add a new book \4. Check in a book \n5. Track book(s) \n6. Quit")

    while True:
        try:
            action = int(input("Kindly enter an option\t"))
            if action == 1:
                wuseLibrary.displayAvailableBooks()
            elif action == 2:
                pass
            elif action == 3:
                pass
            elif action == 4:
                pass
            elif action == 5:
                pass
            elif action == 6:
                print("Thanks for showing me love")
                exit()

        except Exception as anomaly:
            print(anomaly)
    