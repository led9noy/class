from os import system
system("cls")

class Uy:
    def __init__(self, type : str, sum_room : str, price : str):
        self.type = type
        self.sum_room = sum_room
        self.price = price
        
    def get_info(self):
        return f"""
    type = {self.type}
    sum_room = {self.sum_room}
    price = {self.price}
    """    
    
    def choose_one(self, other_houses):
        most_expensive_house = max(other_houses, key=lambda dom: dom.price)
    
        print(f"The most expensive house is {most_expensive_house.price}")
    
class Flat(Uy):
    def __init__(self, type, sum_room, price, hudud : str, holat : str):
        super().__init__(type, sum_room, price)
        self.hudud = hudud
        self.holat = holat
        
    def get_info_flat(self):
        uy_info = super().get_info()
        return f"""Flat:
    {uy_info}
    hudud = {self.hudud}
    holat = {self.holat}
    """
    
    def set_price(self, newPrice : str):
        self.price = newPrice
        
        print(f"New price for '{self.type}' is {self.price}")
    
class House(Uy):
    def __init__(self, type: str, sum_room: str, price: str, hudud : str, holat : str):
        super().__init__(type, sum_room, price)
        self.hudud = hudud
        self.holat = holat
        
    def get_info_house(self):
        uy_info = super().get_info()
        return f"""House:
    {uy_info}
    hudud = {self.hudud}
    holat = {self.holat}
    """

    def set_price(self, newPrice : str):
        self.price = newPrice
        
        print(f"New price for '{self.type}' is {self.price}")
                
        
dom = Uy("Houses and Flats", "12 rooms", "125 000 $")
dom1 = Flat("Flat on 4 floor", "4 rooms", "60 000 $", "Sergeli region", "Euro remont")        
dom2 = House("Hi-tech House", "6 rooms", "80 000 $", "Mirzo Ulugbek region", "Good")

print(dom.get_info())
print("----------------------")
print(dom1.get_info_flat())
print("----------------------")
dom1.set_price("90 000 $")
print("-----------------------")
print(dom2.get_info_house())
print("------------------------")
dom2.set_price("85 000 $ ")
print("------------------------")
print()
print("------------------------")
dom.choose_one([dom1, dom2])
print("-------------------------")