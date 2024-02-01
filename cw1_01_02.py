from os import system 
system("cls")
import cw_01_02

class Avtosalon:
    def __init__(self, salon_nomi : str, salon_manzili : str) :
        self.salon_nomi = salon_nomi
        self.salon_manzili = salon_manzili
        
    def add_avto(self,newCar):
        self.added_cars = []
        self.added_cars.append(newCar)
        
    def get_info(self):
        return [car.get_info() for car in self.added_cars]

avtosalon = Avtosalon("Salon Name", "Salon Address")

avtosalon.add_avto(cw_01_02.car)

print(avtosalon.get_info(), end=" ")
