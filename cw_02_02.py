from os import system
system("cls")

class Transport:
    def __init__(self, brand, color, model) -> None:
        self.brand = brand
        self.color = color
        self.model = model
        
    def get_info_trans(self):
        return f"""

    brand -->             {self.brand}
    color -->             {self.color}
    model -->             {self.model}
    """
    
    def set_brand(self, newBrand):
        self.brand = newBrand
        print(f"New brand car is {self.brand}")
        
    def set_color(self, newColor, newModel):
        self.color = newColor
        self.model = newModel
        print(f"New color for {self.model} is {self.color}")
    
    def set_model(self, newModel):
        self.model = newModel  
        print(f"New car brand is {self.model}")
        
    def get_new_info(self):
        return f"""
          *** NEW TRNASPORT ***
          
    new brand -->        {self.brand}
    new color -->        {self.color}
    new model -->        {self.model}
    """
    
class Car(Transport):
    def __init__(self, brand, color, model, speed, seat_count, manifacture_date) -> None:
        super().__init__(brand, color, model)
        self.speed = speed
        self.seat_count = seat_count
        self.manifacture_date = manifacture_date
        
    def get_info_trans(self):
        avtomobil_info = super().get_info_trans
        return f""""
              *** CAR ***
              
    {avtomobil_info().strip()}
    speed -->             {self.speed}
    seat count -->        {self.seat_count}
    manifacture date -->  {self.manifacture_date}
    """

class Truck(Transport):
    def __init__(self, brand, color, model, speed, weight_capacity, manifacture_date) -> None:
        super().__init__(brand, color, model)
        self.speed = speed
        self.weight_capacity = weight_capacity
        self.manifacture_date = manifacture_date
        
    def get_info_trans(self):
        avtomobil_info = super().get_info_trans
        return f"""
              *** TRUCK ***
              
    {avtomobil_info().strip()}
    speed -->             {self.speed}
    weight capacity -->   {self.weight_capacity}
    manifacture date -->  {self.manifacture_date}
    """        
        
    def set_weight_capacity(self, newCapacity):
        self.weight_capacity = newCapacity
        print(f"New weight capacity is {self.weight_capacity}")
        
    def get_info(self):
        avtomobil_info = super().get_info_trans
        return f"""
            *** TRUCK ***
       with new weight capacity
              
    {avtomobil_info().strip()}
    speed -->             {self.speed}
    weight capacity -->   {self.weight_capacity}
    manifacture date -->  {self.manifacture_date}    
    """
    
    
avto = Transport("Sedan", "Black", "Porsche GT3 911rs")
print(avto.get_info_trans())
print("----------------")
avto.set_brand("Truck")
avto.set_color("Yellow", "Lamborghini Urus")
avto.set_model("Lamborghini Urus")    
print("----------------")
print(avto.get_new_info())
print()    
car = Car("Hybrid", "Grey & Black", "Porsche GT4 991rs", "440 km/h", "4 seats", "2024")
print(car.get_info_trans())
print()
truck = Truck("Truck", "Yellow & Red", "Lexus 570", "220 km/h", "3 tons", "2020")
print(truck.get_info_trans())
print("-----------------")
truck.set_weight_capacity("4 tons")
print("-----------------")
print(truck.get_info())