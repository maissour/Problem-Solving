'''
Write a Python class Restaurant with attributes like :
menu_items, book_table,and customer_orders.
methods like : add_item_to_menu, book_tables, and customer_order.
Perform the following tasks now:

    Now add items to the menu.
    Make table reservations.
    Take customer orders.
    Print the menu.
    Print table reservations.
    Print customer orders.

Note: Use dictionaries and lists to store the data.
'''
# Solution one
class Restaurant1:

    def __init__(self, menu_items=[], book_tables=[], customer_orders=[]):
        self.menu_items = menu_items
        self.book_tables = book_tables
        self.customer_orders = customer_orders

    def add_item_to_menu(self, item):
        if item not in self.menu_items :
            self.menu_items.append(item)
        else :
            print("The item already exists")

    def book_table(self, reservations):
        if reservations not in self.book_tables :
            self.book_tables.append(reservations)
        else :
            print("The table is already reserved")

    def customer_order(self, order):
        if (order not in self.customer_orders) and (order in self.menu_items) :
            self.customer_orders.append(order)
        else :
            print("this order is out of our service")

    def Menu(self):
        if self.menu_items:
            print(self.menu_items)
        else :
            print("the menu is empty")

    def table_reserved(self):
        if self.book_tables:
            print(self.book_tables)
        else :
            print("the tables is empty")

    def orders(self):
        if self.customer_orders:
            print(self.customer_orders)
        else :
            print("there is no order")
        

rest1 = Restaurant1(["PIZZA","SANDWITCH","TACCOS"],[1,2,3],["PIZZA"])

print("#"*10)
rest1.add_item_to_menu("EGGS")
rest1.Menu()
print("#"*10)
rest1.book_table(4)
rest1.table_reserved()
print("#"*10)
rest1.customer_order("SANDWITCH")
rest1.orders()

# Solution two
class Restaurant2:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []

    def add_item_to_menu(self, item, price):
        self.menu_items[item] = price

    def book_tables(self, table_number):
        self.book_table.append(table_number)

    def customer_order(self, table_number, order):
        order_details = {'table_number': table_number, 'order': order}
        self.customer_orders.append(order_details)

    def print_menu_items(self):
        for item, price in self.menu_items.items():
            print("{}: {}".format(item, price))

    def print_table_reservations(self):
        for table in self.book_table:
            print("Table {}".format(table))

    def print_customer_orders(self):
        for order in self.customer_orders:
            print("Table {}: {}".format(order['table_number'], order['order']))

restaurant = Restaurant2()

# Add items
restaurant.add_item_to_menu("Cheeseburger", 9.99)
restaurant.add_item_to_menu("Caesar Salad", 8)
restaurant.add_item_to_menu("Grilled Salmon", 19.99)
restaurant.add_item_to_menu("French Fries", 3.99)
restaurant.add_item_to_menu("Fish & Chips:", 15)
# Book table
restaurant.book_tables(1)
restaurant.book_tables(2)
restaurant.book_tables(3)
# Order items
restaurant.customer_order(1, "Cheeseburger")
restaurant.customer_order(1, "Grilled Salmon")
restaurant.customer_order(2, "Fish & Chips")
restaurant.customer_order(2, "Grilled Salmon")

print("\nPopular dishes in the restaurant along with their prices:")
restaurant.print_menu_items()
print("\nTable reserved in the Restaurant:")
restaurant.print_table_reservations()
print("\nPrint customer orders:")
restaurant.print_customer_orders()
