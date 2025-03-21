class ShopCart:
    def __init__(self):
        self.items = []
    
    def addItem(self, name, price):
        self.items.append({'name': name, 'price': price})
    
    def removeItem(self, name):
        self.items = [item for item in self.items if item['name'] != name]
    
    def printContent(self):

        if not self.items:
            print("The cart is empty.")
            return
        total_value = 0
        print("Items in the cart:")
        for item in self.items:
            print(f"{item['name']}: ${item['price']:.2f}")
            total_value += item['price']
        print(f"Total value: ${total_value:.2f}")


cart = ShopCart()
cart.addItem("Laptop", 1200.00)
cart.addItem("Mouse", 25.50)
cart.printContent()
cart.removeItem("Mouse")
cart.printContent()
