from abc import ABC, abstractmethod
from datetime import datetime

class Product(ABC):

    def __init__(self, product_id, name, price, quantity_in_stock):
        self._product_id = product_id #protected
        self._name = name
        self._price = price
        self._quantity_in_stock = quantity_in_stock

    def restock(self, amount):
        self._quantity_in_stock += amount
        print(f"{self._name} restocked. New quantity is {self._quantity_in_stock}.")

    def sell(self, quantity):
        if quantity > self._quantity_in_stock: 
            print("not enough stock")

        else:
            self._quantity_in_stock -= quantity
            print(f"{self._name} sold. New quantity is {self._quantity_in_stock}.")

    def total_value(self):
        return self._price * self._quantity_in_stock

    @abstractmethod
    def __str__(self):
        pass

#subclasses

#Electronics
class Electronics(Product):

    def __init__(self, product_id, name, price, quantity_in_stock, warranty_years, brand):
        super().__init__(product_id, name, price, quantity_in_stock)
        self._warranty_years = warranty_years
        self._brand = brand

    def __str__(self):
        return f"Electronic - {self._name} | Brand - {self._brand} | Warranty - {self._warranty_years} | stock - {self._quantity_in_stock}"

 #Grocery

class Grocery(Product):

    def __init__(self, product_id, name, price, quantity_in_stock, expiry_date):
        super().__init__(product_id, name, price, quantity_in_stock)
        self._expiry_date = expiry_date  #YYYY-MM-DD fomat

    def is_expired(self):
        today = datetime.now().date()  
        return today > datetime.strptime(self._expiry_date, "%Y-%m-%d").date()



    def __str__(self):
        status = "Expired" if self.is_expired() else "Fresh"
        return f"Grocery - {self._name} | Expiry - {self._expiry_date} | Status - {status} | stock - {self._quantity_in_stock}"

#Clothing

class Clothing(Product):

     def __init__(self, product_id, name, price, quantity_in_stock, size, material):
        super().__init__(product_id, name, price, quantity_in_stock)
        self._size = size
        self._material = material

     def __str__(self):
        return f"Clothing - {self._name} | Size - {self._size} | Material - {self._material} | stock - {self._quantity_in_stock}"

#Inventory

class Inventory:

    def __init__(self):
        self._products = {}

    def add_product(self, product):
        if product._product_id in self._products:
            print("Product ID already exists")
        else:
            self._products[product._product_id] = product
            print("Product added successfully")

    def sell_product(self, product_id, quantity):
        if product_id in self._products:
            self._products[product_id].sell(quantity)
        else:
                print("Product not found")

    def restock_product(self, product_id, amount):
        if product_id in self._products:
            self._products[product_id].restock(amount)
        else:
            print("Product not found")

    def list_products(self):
        for product in self._products.values():
            print(product)

    def remove_expired_products(self):
        for product_id, product in list(self._products.items()):
            if isinstance(product, Grocery) and product.is_expired():
                del self._products[product_id]
                print(f"Removed expired product: {product._name}")

    def total_inventory_value(self):
        total = 0
        for product in self._products.values():
            total += product.total_value()
        return total

# create Inventory System

inv = Inventory()

e1 = Electronics('E01', 'Laptop', 12000, 10, 2, 'Dell')
g1 = Grocery('G01', 'Yogurt', 2.5, 50, '2025-06-30')
c1 = Clothing('C01', 'shirt', 20, 30, 'M', 'cotton')

inv.add_product(e1)
inv.add_product(g1)
inv.add_product(c1)

inv.list_products()

inv.sell_product('E01', 2)
inv.sell_product('G01', 10)

#restock
inv.restock_product('C01', 10)

#removed expired Grocery

inv.remove_expired_products()

#show total inventory

print(f"Total Inventory Value: {inv.total_inventory_value()}")
