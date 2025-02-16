class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0  # To track last transaction price

    def add_item(self, title, price, quantity=1):
        """
        Adds an item to the register.
        - `title` (str): Name of the item.
        - `price` (float): Price of one unit.
        - `quantity` (int, optional): Number of items. Defaults to 1.
        """
        self.total += price * quantity
        self.last_transaction = price * quantity
        self.items.extend([title] * quantity)  # Store item names

    def apply_discount(self):
        """
        Applies the discount and updates the total.
        """
        if self.discount:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """
        Removes the last transaction amount from total.
        """
        self.total -= self.last_transaction
        self.last_transaction = 0  # Reset last transaction
        if self.items:
            self.items.pop()  # Remove last added item


# Example usage:
register = CashRegister(20)  # 20% discount
register.add_item("Laptop", 1000)  # Add an item
register.add_item("Mouse", 50, 2)  # Add two items of $50 each
print(register.items)  # Expected: ['Laptop', 'Mouse', 'Mouse']
register.apply_discount()  # Apply discount
register.void_last_transaction()  # Remove last item
print(f"Final total: ${register.total:.2f}")  # Print final total
