# Arthematic and Comparision
class InventoryItems:
    # A class is a demonstrate operator overloading for inventory management.
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __repr(self):
        return f"InventoryItems(name='{self.name}', quantity={self.quantity})"

    # Arthematic Operators
    def __add__(self, other):
        if isinstance(other, InventoryItems) and self.name == other.name:
            return InventoryItems(self.name, self.quantity + other.quantity)
        raise ValueError("Cannot add items of different types")

    def __sub__(self, other):
        if isinstance(other, InventoryItems) and self.name == other.name:
            if self.quantity >= other.quantity:
                return InventoryItems(self.name, self.quantity - other.quantity)
            raise ValueError(
                "Cannot subtract more than the available quantity")
        raise ValueError("Cannot subtract items of different types.")

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return InventoryItems(self.name, int(self.quantity * factor))
        raise ValueError("Multplication factor must be a number.")

    def __truediv__(self, factor):
        if isinstance(factor, (int, float)) and factor != 0:
            return InventoryItems(self.name, int(self.quantity / factor))
        raise ValueError("Divivsion factor must be a non-zero number")

    # Comparision Operators

    def __eq__(self, other):
        if isinstance(other, InventoryItems):
            return self.name == other.name and self.quantity == other.quantity
        return False

    def __lt__(self, other):
        if isinstance(other, InventoryItems) and self.name == other.name:
            return self.quantity < other.quantity
        raise ValueError("Cannot compare items of different types.")

    def __gt__(self, other):
        if isinstance(other, InventoryItems) and self.name == other.name:
            return self.quantity > other.quantity
        raise ValueError("Cannot compare items of different types.")


# Creating some inventory items
item1 = InventoryItems("Apple", 50)
item2 = InventoryItems("Apple", 30)
item3 = InventoryItems("Orange", 80)

# Adding quantities of the same item
result_add = item1 + item2
print(result_add)
# Output is Inventoryitems(name='Apple', quantity:10)


# Subracting quantities of the same item
result_sub = item1 - item2
print(result_sub)
# Output is Inventoryitems(name='Apple', quantity:-10)


# Multiplying item quantities by a factor
result_mul = item1 * 2
print(result_mul)
# Output is Inventoryitems(name='Apple', quantity:0)

# Comparing item quantities
print(item1 > item2)  # output is True
print(item1 == InventoryItems("Apple", 0))  # output is True


# Trying to add items of differrent types
try:
    result_invalid = item1 + item3
except ValueError as e:
    print(e)  # output Cannot add items of different types

# Trying to subtract more than avaiable quantity
try:
    result_invalid = item2 - item1
except ValueError as e:
    print(e)  # output Cannot subract more than the available quantity
