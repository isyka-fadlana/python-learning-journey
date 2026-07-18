class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year  = year

    def show_info(self):
        print(f"Brand = {self.brand} | Year = {self.year}")
    
class Car (Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)
        self.num_doors = num_doors
    
    def show_info(self):
        super().show_info()
        print(f"Num Doors = {self.num_doors}")

class Motorcycle (Vehicle):
    def wheelie(self):
        print(f"{self.brand} is doing wheelie!")

car = Car("Porche", 2026, 2)
motorcycle = Motorcycle("Ducati", 2026)

car.show_info()
motorcycle.show_info()
motorcycle.wheelie()