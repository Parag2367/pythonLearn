from random import randint


class LibSystem:

    def __init__(self):
        self.name = input("Enter book name = ")
        self.isbn = randint(1000, 10000)
        self.price = float(input("Enter price of book = "))
        self.quantity = int(input("Enter quantity of book = "))
        self.status: bool = False

    def info(self):
        print(f"Name of book is {self.name}")
        print(f"isbn of book is {self.isbn}")
        print(f"price of book is {self.price}")
        print(f"quantity of book is {self.quantity}")
        print(f"status of book is {self.status}")

    def rent(self):
        self.status = True


library = []

while True:

    print(
        """
    1.add_book: Add a book to the library
    2.search_book: Search for a book by ISBN
    3.check_quantity: Check the quantity of a book
    4.rent_book: Rent a book
    5.display_books: Display all books in the library
    6.exit_program: Exit the program
    """
    )

    choice = int(input("Enter your choice = "))
    try:
        if choice in range(1, 7):
            if choice == 1:
                obj = LibSystem()
                library.append(obj)
                print("ADDED")
                obj.info()

            elif choice == 2:
                if len(library) != 0:
                    number = int(input("Enter book's isbn = "))
                    for a in library:
                        if a.isbn == number:
                            print("DETAILS")
                            a.info()
                            break
                    else:
                        print("Book not found !!")
                else:
                    print("Library is empty")

            elif choice == 3:
                if len(library) != 0:
                    number = int(input("Enter book's isbn = "))
                    for a in library:
                        if a.isbn == number:
                            print("Quantity")
                            print(a.quantity)
                            break
                    else:
                        print("Book not found !!")
                else:
                    print("Library is empty")

            elif choice == 4:
                if len(library) != 0:
                    number = int(input("Enter book's isbn = "))
                    for a in library:
                        if a.isbn == number:
                            a.rent()
                            print("DETAILS")
                            a.info()
                            break
                    else:
                        print("Book not found !!")
                else:
                    print("Library is empty")

            elif choice == 5:
                if len(library) != 0:
                    for a in library:
                        a.info()
                else:
                    print("No books found !")

            elif choice == 6:
                break
        else:
            raise ModuleNotFoundError

    except ModuleNotFoundError:
        print("Not a valid entry")
