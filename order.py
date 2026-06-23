"""This file has the Order class."""


class Order:
    """An order made by one customer."""

    def __init__(self, customer):
        # The customer and an empty list of items.
        self.customer = customer
        self.items = []

    def add_item(self, item):
        """Add one item to the order."""
        self.items.append(item)

    def get_total(self):
        """Add up the price of all items and add 19% tax."""
        total = 0
        for item in self.items:
            total = total + item.price
        tax = total * 0.19
        return total + tax

    def show_receipt(self):
        """Print the receipt for this order."""
        print("Receipt for " + self.customer.get_name())
        for item in self.items:
            print(item.name + " - " + str(item.price) + " euro")
        print("Total with 19% tax: " + str(round(self.get_total(), 2))
              + " euro")

    def save_to_file(self, filename):
        """Save the order to a text file."""
        my_file = open(filename, "a")
        my_file.write("Order for " + self.customer.get_name() + "\n")
        for item in self.items:
            my_file.write(item.name + " - " + str(item.price) + " euro\n")
        my_file.write("Total: " + str(round(self.get_total(), 2))
                      + " euro\n")
        my_file.write("-----\n")
        my_file.close()
