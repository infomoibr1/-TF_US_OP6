class Product:

    def __init__(self, price) -> None:
        self.__price = price 

    def __repr__(self) -> str:
        return f"Price: {self.price}"

    # 1. Classical Way -> Methode
    def set_price(self, price):
        if price > 0:
            self.price = price


    # 2. Way --> Property
    
    @property  #--> Getter --> method has the same name like the attribute
    def price(self):
        return f"Price: {self.__price} €"
    
    
    @price.setter # Setter
    def price(self, value):
        if value > 0:
            self.__price = value 
        # else:
        #     raise ValueError("Price cannot be negative")
        
    @price.deleter # Deleter
    def price(self):
        self.__price = 0  # instead of delete from memory --> make the value = 0



car = Product(10)
print(car) # 10

car.set_price(500)
print(car) # 500


car.set_price(-60)
print(car) # 500


car.price = 400   # setter
print(car.price)  # getter

print(car) # Getter also was called


car.price = -300
print(car) # 400



del car.price
print(car) # Price = 0