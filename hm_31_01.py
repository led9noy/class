from os import system
system("cls")

class Animal:
    def __init__(self, animal_type : str, color : str, long_age : str):
        self.animal_type = animal_type
        self.color = color
        self.long_age = long_age
        
    def get_info(self):
        return f"""
    animal_type --> {self.animal_type}
    color -->       {self.color}
    long_age -->    {self.long_age}
    """
    
    def choose_one(self, other_animals):
        fastest_animal = max(other_animals, key=lambda animal: animal.high_speed)
        most_teeth_animal = max(other_animals, key=lambda animal: animal.sum_teeth)

        print(f"The animal that runs fastest is a {fastest_animal.animal_type} with a speed of {fastest_animal.high_speed}.")
        print(f"The animal with the most teeth is a {most_teeth_animal.animal_type} with {most_teeth_animal.sum_teeth} teeth.")
    
class Dog(Animal):
    def __init__(self, animal_type : str, color : str, long_age : str, high_speed : str, sum_teeth : str):
        super().__init__(animal_type, color, long_age)
        self.high_speed = high_speed
        self.sum_teeth = sum_teeth
        
    def get_more_info(self):
        animal_info = super().get_info()
        return f"""Info about dog:
    
    {animal_info.strip()}
    high_speed --> {self.high_speed}
    sum_teeth --> {self.sum_teeth}
    """    
class Horse(Animal):
    def __init__(self, animal_type : str, color : str, long_age : str,high_speed : str, sum_teeth : str):
        super().__init__(animal_type, color, long_age)
        self.high_speed = high_speed
        self.sum_teeth = sum_teeth
    
    def get_more_info(self):
        animal_info = super().get_info()
        return f"""Info about horse:
    
    {animal_info.strip()}
    high_speed --> {self.high_speed}
    sum_teeth -->  {self.sum_teeth}    
    """
    
class Cat(Animal):
    def __init__(self, animal_type : str, color : str, long_age : str,high_speed : str, sum_teeth : str):
        super().__init__(animal_type, color, long_age)
        self.high_speed = high_speed
        self.sum_teeth = sum_teeth
        
    def get_more_info(self):
        animal_info = super().get_info()
        return f"""Info about cat:
    
    {animal_info.strip()}
    high_speed --> {self.high_speed}
    sum_teeth -->  {self.sum_teeth}
    """

animal = Animal("mammal", "black", "50 years")
dog = Dog("dog","brown", "13 years", "20 km/h", "14 teeth")
horse = Horse("horse","black", "30 years","60 km/h", "32")
cat = Cat("cat","grey", "10 years","18 km/h", "24")

print(animal.get_info())
print("-------------------")
print(dog.get_more_info())
print("-------------------")
print(horse.get_more_info())    
print("-------------------")
print(cat.get_more_info())
animal.choose_one([dog, horse, cat])