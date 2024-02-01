from os import system
system("cls")

class Avto:
    def __init__(self, model : str, color : str, price : int, probeg : int, korobka : str):
        self.model = model
        self.color = color
        self.price = price
        self.probeg = probeg
        self.korobka = korobka
        
    def get_info(self):
        return f"""
        Avtomobilimiz nomi {self.model} va rangi {self.color} rangda bolib, uning narxi 
        {self.price} hisbolanadi.Bosib otgan masofasi {self.probeg} km va korobkasi 
        {self.korobka} peredachali hisoblanadi."""
       
     # agar probeg 1000, 3000 va 5000 dan katta bolsa uning narxi 20 yoki 40 yoki 60 % ga tushsin 
    def update(self, newprobeg : int):
        self.probeg = newprobeg and newprobeg > 0
        if newprobeg > 1000:
            self.price = self.price // 0.2
        elif newprobeg > 3000:
            self.price = self.price // 0.4
        elif newprobeg > 5000:
            self.price = self.price // 0.6
        return f"""
        Avtomobilimiz nomi {self.model} va rangi {self.color} rangda bolib, uning narxi {self.price} hisbolanadi.Bosib otgan masofasi {newprobeg} km va korobkasi {self.korobka} peredachali hisoblanadi."""
        

car = Avto("Matiz", "Sariq", 12000, 0, "5")
print(car.get_info())
print("-----------------------------------------------------------------------------")
print(car.update(int(input("enter new probeg for your car --> "))))