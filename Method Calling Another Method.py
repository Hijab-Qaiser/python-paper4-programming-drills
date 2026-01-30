class product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name  # string variable
        self.price = price  # real variable
        self.quantity = quantity  # integer variable

    @property
    def GetProductName(self):
        return self.product_name

    @property
    def GetPrice(self):
        return self.price

    @property
    def GetQuantity(self):
        return self.quantity

    def CalculateTotalValue(self):
        total = self.price * self.quantity
        return total

    def CalculateDiscountedValue(self, discount_percent):
        discount = self.CalculateTotalValue() * (1 - discount_percent / 100)
        return discount


Prod_1 = product("Laptop", 85000.00, 3)
print(f"Total value: {Prod_1.CalculateTotalValue()}")
print(f"Discounted value: {Prod_1.CalculateDiscountedValue(15)}")
