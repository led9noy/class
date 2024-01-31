import os
os.system("cls")

class Employee:
    def __init__(self, name : str, surname : str, position : str, salary : int):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.position = position
    
    def get_info(self):
        return f"""
    name :     {self.name}
    surname :  {self.surname}
    position : {self.position}
    salary :   {self.salary}
    """

class Enterprice_employee(Employee):
    def __init__(self,rating : int):
        super().__init__("Abdulla", "ABdullayev", "Boss", 45000.0)
        self.rating = rating
        
    def get_info(self):
        main_info = super().get_info()
        return f"""
    {main_info.strip()}
    rating :   {self.rating}
    """
    
    def update(self):
        if self.rating > '60' or self.rating < '75':
            self.salary += self.salary * 0.2 
        elif self.rating > '75' or self.rating < '90':
            self.salary += self.salary * 0.4
        elif self.rating > '90' or self.rating < '100':
            self.salary += self.salary * 0.6
        return self.salary
            
def_employ = Employee("Abdulla", "ABdullayev","Boss",45000.0)
employer1 = Enterprice_employee(input("Enter yout rating: "))
print(employer1.get_info())
print("After changing your salary equal to:")
print(employer1.update())
    
    
    
    