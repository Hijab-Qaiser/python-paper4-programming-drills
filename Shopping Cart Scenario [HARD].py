class ShoppinCart:
    def __init__(self, coustomer_name):
        self.__coustomer_name = coustomer_name  # Private String variable
        self.__items = 0  # Private integer variable
        self.__total_price = 0.0  # Private float variable

    @property
    def GetCustomerName(self):
        return self.__coustomer_name

    @property
    def GetItems(self):
        return self.__items

    @property
    def GetTotalPrice(self):
        return self.__total_price

    def AddItem(self, price):
        self.__items += 1
        self.__total_price += price

    def RemoveItem(self, price):
        if self.__items > 0:
            self.__items -= 1
            self.__total_price -= price
            return True
        return False

    def ApplyDiscount(self, percentage):
        discount = self.__total_price * (percentage / 100)
        self.__total_price -= discount

    def Checkout(self):
        print(f"Customer: {self.__coustomer_name} ")
        print(f"Total Items: {self.__items} ")
        print(f"Total Price: {self.__total_price} ")
        return self.__total_price


Cart1 = ShoppinCart(input(f"Enter customer name: "))
print(f"\n")
while True:
    print(f"--- Shopping Cart Menu ---")
    print(f"--- 1. Add item ---")
    print(f"--- 2. Remove item ---")
    print(f"--- 3. Apply discount ---")
    print(f"--- 4. Checkout ---")
    print(f"\n")
    user_choice = input(f"What do u want to continue with? ").lower()
    if user_choice == "add item" or user_choice == "1":
        price = float(input(f"Enter item price: "))
        Cart1.AddItem(price)
        print(f"Item added ")
    elif user_choice == "remove item" or user_choice == "2":
        price = float(input(f"Enter item price to remove: "))
        if Cart1.RemoveItem(price):
            print(f"Item removed ")
        else:
            print(f"Cart is empty ")
    elif user_choice == "apply discount" or user_choice == "3":
        percentage = float(input(f"Enter discount percentage: "))
        Cart1.ApplyDiscount(percentage)
        print(f"Discount applied ")
    elif user_choice == "checkout" or user_choice == "4":
        Cart1.Checkout()
        break
