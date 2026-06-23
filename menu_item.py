"""This file has the MenuItem class."""


class MenuItem:
    """One item on the menu, like a burger or a drink."""

    def __init__(self, item_id, name, category, price):
        # Save the details of the item.
        self.item_id = item_id
        self.name = name
        self.category = category
        self.price = price
        self.available = True

    def make_unavailable(self):
        """Set the item to sold out."""
        self.available = False

    def make_available(self):
        """Set the item back to available."""
        self.available = True

    def to_text(self):
        """Return one line of text to show the item."""
        if self.available:
            status = ""
        else:
            status = " (sold out)"
        return self.item_id + " - " + self.name + " - " + str(self.price) \
            + " euro" + status
