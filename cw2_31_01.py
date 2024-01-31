import os
os.system("cls")

class Transport:
    def __init__(self, brand : str, type : str, model : str):
        self.brand = brand 
        self.model = model
        self.type = type
        
    def get_info(self):
        return f"""
    brand -->           {self.brand}
    model -->           {self.model}
    type  -->           {self.type}
    """
        
class Electro_cars(Transport):
    def __init__(self, battery_life : str, charging_time : str):
        super().__init__("Porsche", "Coupe", "GT3 911rs")
        self.battery_life = battery_life
        self.charging_time = charging_time
            
    def get_more_info(self):
        trans_info = super().get_info()
        return f"""Electro cars:
    
    {trans_info.strip()}
    battery_life  -->  {self.battery_life}
    charging_time -->  {self.charging_time}
    """
    
class Sport_cars(Transport):
    def __init__(self, motor : str, color : str):
        super().__init__("Porsche", "Coupe", "GT3 911rs")
        self.motor = motor
        self.color = color
        
    def get_more_info(self):
        trans_info = super().get_info()
        return f"""Sport cars:
    
    {trans_info.strip()}
    motor -->           {self.motor}
    color -->           {self.color}
    """            
        
class Truck(Transport):
    def __init__(self, motor : str, height : int, long : int, weight : int):
        super().__init__("Porsche", "Coupe", "GT3 911rs")
        self.motor = motor
        self.height = height
        self.long = long
        self.weight = weight
        
    def get_more_info(self):
        trans_info = super().get_info()
        return f"""Trucks:
    
    {trans_info.strip()}
    motor  -->          {self.motor}
    height -->          {self.height}
    long   -->          {self.long}
    weight -->          {self.weight}
    """            
    
                        
car = Transport("Porsche", "Coupe", "GT3 911rs")
print(car.get_info())
print("--------------------------------------")

car1 = Electro_cars("for 5 years","12 h for full charge")
print(car1.get_more_info())
print("--------------------------------------")

car2 = Sport_cars("v12 twinTurbo", "black xoxo")
print(car2.get_more_info())
print("--------------------------------------")

car3 = Truck("v8 biTurbo", "1.7 metres high", "4 metres long", "1.2 tons")
print(car3.get_more_info())
print("--------------------------------------")