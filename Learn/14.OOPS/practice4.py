class Bookstore:
    def __init__(self):
        self.inventory = {}
        self.sales_data = []

    def processOrders(self, isbn, customer, quantity):
        if isbn not in self.inventory:
            print("Book not found")
            return

        if quantity > self.inventory[isbn]["quantity"]:
            print("Insufficient quantity")
            return

        if quantity <= 0:
            print("Invalid entry")
            return

        total_price = self.inventory[isbn]["price"] * quantity
        data = {
            "isbn": isbn,
            "customer": customer,
            "quantity": quantity,
            "total_price": total_price,
        }

        self.sales_data.append(data)
        print("orders processed succesfully")

    def report(self):
        total_revenue = sum([txn["total_price"] for txn in self.sales_data])
        total_quantity = sum([txn["quantity"] for txn in self.sales_data])

        print("revenue data")
        print(f"total revenue = {total_revenue}")
        print(f"total quantity = {total_quantity}")

    def addBook(self, name, isbn, author, price, quantity):
        if isbn in self.inventory:
            print("Book with ISBN already exists")
            self.inventory[isbn][quantity] += 1
            return
        self.inventory[isbn] = {
            "name": name,
            "author": author,
            "price": price,
            "quantity": quantity,
        }

    def searchBook(self, query):
        foundbook_ids = []
        for isbn, details in self.inventory.items():
            if query.lower() in [
                str(isbn),
                details["name"].lower(),
                details["author"].lower(),
            ]:
                foundbook_ids.append(isbn)

        if len(foundbook_ids) == 0:
            print("No books found")
            return

        for ids in foundbook_ids:
            print(self.inventory[ids])

    def updateQuantity(self, isbn, new_quantity):
        if isbn not in self.inventory:
            print("Book not found")
            return
        if new_quantity < 0:
            print("invalid entry")
            return

        self.inventory[isbn]["quantity"] += new_quantity

    def displayInventory(self):
        if not self.inventory:
            print("No books are in inventory")
            return

        for isbn, details in self.inventory.items():
            print(
                f"isbn = {isbn}, Name = {details['name']}, Author = {details['author']}, Price = {details['price']}, Quantity = {details['quantity']}"
            )


obj = Bookstore()

while True:

    print(
        """
    \n1. add_book
    2. search_book
    3. update_quantity
    4. process_order
    5. get_sales_report
    6. display_inventory
    7. display_sales_data
    """
    )

    choice = int(input("Enter your choice = "))

    if choice == 1:
        name = input("Enter book name = ")
        isbn = int(input("Enter isbn = "))
        price = float(input("Enter book price = "))
        author = input("Enter book's author = ")
        quantity = input("Enter quantity of book = ")
        obj.addBook(name, isbn, author, price, quantity)

    elif choice == 2:
        q = input("Enter isbn/name/author")
        obj.searchBook(q)

    elif choice == 3:
        isbn = int(input("Enter isbn = "))
        new_quantity = int(input("enter new quantity = "))
        obj.updateQuantity(isbn, new_quantity)

    elif choice == 4:
        isbn = int(input("Enter isbn = "))
        quantity = input("Enter quantity of book = ")
        customer = input("Enter customer name = ")
        obj.processOrders(isbn, customer, quantity)

    elif choice == 5:
        obj.report()

    elif choice == 6:
        obj.displayInventory()

    elif choice == 8:
        break

    else:
        print("invalid entry")
