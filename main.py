"""This is the main program. Run this file to start.

It shows a simple menu and lets the user make an order for
Bella's Restaurent.
"""

from menu import Menu
from customer import Customer
from order import Order


def make_order(menu):
    """Ask for a customer and items, then make an order."""
    name = input("Customer name: ")
    phone = input("Phone number: ")
    customer = Customer(name, phone)
    order = Order(customer)

    # Keep asking for items until the user presses Enter.
    while True:
        item_id = input("Item id to add (or press Enter to finish): ")
        if item_id == "":
            break
        item = menu.find_item(item_id)
        if item is None:
            print("Sorry, there is no item with that id.")
        elif item.available is False:
            print("Sorry, that item is sold out.")
        else:
            order.add_item(item)
            print(item.name + " was added.")

    # Show the receipt and save the order to a file.
    order.show_receipt()
    order.save_to_file("data/orders.txt")
    print("The order was saved to data/orders.txt")


def main():
    """Run the program."""
    # Load the menu from the file.
    menu = Menu()
    menu.load_from_file("data/menu.csv")

    print("Welcome to Bella's Restaurent!")

    # This loop keeps going until the user chooses to quit.
    while True:
        print("")
        print("1. Show the menu")
        print("2. Make an order")
        print("3. Quit")
        choice = input("Choose a number: ")

        if choice == "1":
            menu.show_all()
        elif choice == "2":
            make_order(menu)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please type 1, 2 or 3.")


main()
