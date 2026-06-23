"""This file has the Menu class."""

from menu_item import MenuItem


class Menu:
    """A list of all the menu items."""

    def __init__(self):
        # Start with an empty list of items.
        self.items = []

    def add_item(self, item):
        """Add one item to the menu."""
        self.items.append(item)

    def find_item(self, item_id):
        """Find an item by its id. Return None if it is not found."""
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None

    def show_all(self):
        """Print every item on the menu."""
        for item in self.items:
            print(item.to_text())

    def load_from_file(self, filename):
        """Read the menu items from a CSV file."""
        # Try to open the file. Show a message if it is missing.
        try:
            my_file = open(filename, "r")
        except FileNotFoundError:
            print("Sorry, the menu file was not found.")
            return

        lines = my_file.readlines()
        my_file.close()

        # The first line is the header, so we start from the second line.
        for line in lines[1:]:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            item_id = parts[0]
            name = parts[1]
            category = parts[2]
            price = float(parts[3])
            item = MenuItem(item_id, name, category, price)
            if parts[4] == "0":
                item.make_unavailable()
            self.add_item(item)
