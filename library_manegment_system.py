class Library:
    def __init__(self, bookList):
        self.books = bookList

    def showBooks(self):
        print('The available books are...')
        for i, item in enumerate(self.books):
            print(f'    {i+1}:{item}')

    def borrowBook(self, bookName):
        if bookName in self.books:
            self.books.remove(bookName)
        print(f'You have got the book {bookName}')
        for i in self.books:
            print(f'The available book is {i}')
        # print(self.books)
    def returnBook(self, bookName):
        if bookName not in self.books:
            self.books.append(bookName)
        # print(self.books)
        for i in self.books:
            print(f'The available book is {i}')

class Student:
    def requestBook(self):
        self.book = input("Enter a book: ")
        return self.book
    def returnBook(self):
        self.book = input("Enter a book: ")
        return self.book


if __name__ == "__main__":
    library1 = Library(['Book1', 'Python', 'Data Science','C', 'Java'])
    std = Student()
    # library1.showBooks()
    # library1.borrowBook('C')
    # library1.returnBook('C')
    while True:
        print('''Enter what you want to do
        Press 1 to see the available books.
        Press 2 to borrow a book.
        press 3 to return a book.
        Press 4 to exit.
        ''')
        userInp = int(input('Enter a number from the menu: '))
        if userInp == 1:
            library1.showBooks()
        elif userInp == 2:
            library1.borrowBook(std.requestBook())
        elif userInp == 3:
            library1.returnBook(std.returnBook())
        elif userInp == 4:
            exit()
        else:
            print('invalid input')


