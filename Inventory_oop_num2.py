
# Class product
class Product:
    def __init__(self, name, price, stock):
        self._name = name 
        self._price = price 
        self._stock = stock
    
    # Building getter to access to each attribute
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    @property
    def stock(self):
        return self._stock  
    
# Class invetory
class Inventory:
    def __init__(self, name_of_store):
        self.name_of_store = name_of_store
        self.products = []
    
    def add_products(self, product):
        self.products.append(product) 
    
    def list_products(self):
        for l in self.products:
            print(f"Name: {l._name} | Price: {l._price} | Stock Available: {l._stock}")
    
    def find_products(self):
        isFound = False
        if not self.products:
            print("Nothing to show")
        else:
            target = input("Insert the name of the product to look for: ")  
            for i in self.products:
                if target == i._name:
                    print("Name of the product exist!")
                    isFound = True
                    break
            if not isFound:
                print("Product do not exist") 
     
    def count_products(self):
        amount = len(self.products)
        print(f"There are {amount} in the inventory")                   
                    
product = Product("Monitor", 119, 10) 
product1 = Product("Pc Gamer", 750, 8)
product2 = Product("Laptop Asus", 700, 5)
product3 = Product("TV Samsung", 800, 4)
product4 = Product("iPhone 14 pro Max", 1200, 8)

my_inventory = Inventory("Supermarket")

my_inventory.add_products(product) 
my_inventory.add_products(product1) 
my_inventory.add_products(product2) 
my_inventory.add_products(product3)
my_inventory.add_products(product4)

my_inventory.count_products()                

            
my_inventory.find_products()                
                         
    
           