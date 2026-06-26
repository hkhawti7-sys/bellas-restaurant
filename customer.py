"""Customer - the person ordering."""
​
​
class Customer:
    """Someone who places an order."""
​
    def __init__(self, name, phone):
        # name and phone
        self.name = name
        self.phone = phone
​
    def get_name(self):
        """Give back the name."""
        return self.name
​
    def change_phone(self, new_phone):
        """Update the phone number."""
        self.phone = new_phone
​
    def to_text(self):
        """Customer as text."""
        return self.name + " (" + self.phone + ")"
​
