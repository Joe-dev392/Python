class Library:
    def __init__(self, booklist):
        self.books = booklist

    def displayAvailableBooks(self):
        print(f"There are many {len(self.books)} books available")
        for book in self.books:
            print(f"==> {book}")

    def checkOutBooks(self, name, bookName):
        if bookName not in self.books:
            print(f"{bookName} is unavailable in our library")
        else:
            self.books.remove(bookName)
            trackList.append({name:bookName})
            print(f"{bookName} checked out successfully")

    def checkInBooks(self, bookName):
        self.books.append(bookName)
        print(f"Book {bookName} checked in successfully")

    def populateBookList(self, bookName):
        self.books.append(bookName)
        print(f"Book \"{bookName}\" added successfully")




class Person():
    def issueBook(self):
        print("You wanna issue out a book")
        self.books = input("Please enter the book name ")
        return self.books

    def returnBook(self):
        print("You wanna return a book?")
        self.books = input("Enter book name ")
        borrower = input("Enter the borrower name ")
        if {borrower: self.books} in trackList:
            trackList.remove({borrower: self.books})
        return self.books

    def addBook(self):
        print("A donated new book")
        self.books = input("Please enter book name ")
        return self.books

if __name__ == '__main__':
    wuseLibrary = Library(['General Maths', 'Programming Fundemantals', 'Ikemefuna'])
    individual = Person()
    trackList = []

    print("<======== Wuse Digital Libraary ========>")
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    print("\nWelcome user, what would you like to accomplish today?")
    print("\n1. View Book List \n2. Check out a book \n3. Add a new book \n4. Check in a book \n5. Track book(s) \n6. Quit")

    while True:
        try:
            action = int(input("Kindly enter an option\t"))
            if action == 1:
                wuseLibrary.displayAvailableBooks()
            elif action == 2:
                wuseLibrary.checkOutBooks(input("Please provide the borrower's name\t "), individual.issueBook())
            elif action == 3:
                wuseLibrary.populateBookList(individual.addBook())
            elif action == 4:
                wuseLibrary.checkInBooks(individual.returnBook())
            elif action == 5:
                for item in trackList:
                    for key, value in item.items():
                        borrower = key
                        book = value
                        print(f"==> Book: {book} | Borrower: {borrower}")
                if len(trackList) == 0:
                    print("No book has been borrowed")
            elif action == 6:
                print("Thanks for showing me love")
                exit()

        except Exception as anomaly:
            print(anomaly)