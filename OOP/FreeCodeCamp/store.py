class Item:
    def __init__(self, name: str, price: float, quantity= 0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        
        self.name = name
        self.price = price
        self.quantity = quantity
        
    
    def calculate_total_price(self):
        return self.quantity*self.price

item1 = Item('Phone', 100, 5)

print(item1.calculate_total_price())

item2 = Item("Laptop", 1000, -3)
print(item2.calculate_total_price())
