import os
os.system("cls")

class Tech:
    def __init__(self, brand : str, model : str, type : str):
        self.brand = brand
        self.model = model
        self.type = type
        
    def get_info(self):
        return f"""
    
    brand :      {self.brand}
    model :      {self.model}
    type :       {self.type}
    """  
        
class Nootebooks(Tech):
    def __init__(self, video_card : int, ram : int, display : int):
        super().__init__("Mac", "Apple", "13 pro")
        self.video_card = video_card
        self.ram = ram
        self.display = display
        
    def more_info(self):
        tech_info = super().get_info()
        return f"""Nootes :
    
    {tech_info.strip()}
    video_card : {self.video_card}
    ram :        {self.ram}
    display :    {self.display}        
    """
    
class Televisions(Tech):
    def __init__(self, size : int, display : int):
        super().__init__("Mac", "Apple", "13 pro")
        self.size = size
        self.display = display


    def more_info(self):
        tech_info = super().get_info()
        return f"""Tels :
    
    {tech_info.strip()}
    size :       {self.size}
    display :    {self.display}
    """

class Smartphones(Tech):
    def __init__(self, size : int, sim_count : int):
        super().__init__("Mac", "Apple", "13 pro")
        self.size = size
        self.sim_count = sim_count


    def more_info(self):
        tech_info = super().get_info()
        return f"""Phones:
    
    {tech_info.strip()}
    size :       {self.size}
    sim_count :  {self.sim_count}
    """ 
            
tech = Tech("Mac", "Apple", "13 pro")
print(tech.get_info())
print("------------------------------")       
noote = Nootebooks(12, 16, 13)
print(noote.more_info())
print("------------------------------")
tel = Televisions(12, 14)
print(tel.more_info())
print("------------------------------")
phone = Smartphones(6, 2)
print(phone.more_info())
print("------------------------------")