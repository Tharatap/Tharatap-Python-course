""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def get_info(self):
        print(f"brand: {self.brand}")
        print(f"model: {self.model}")
        print(f"year: {self.year}")

class car(Vehicle):
    def __init__(self,brand,model,year,number_of_doors):
        super().__init__(brand,model,year)
        self.number_of_doors = number_of_doors
    
    def get_info(self):
        super().get_info()
        print(f"number of doors: {self.number_of_doors}")

myCar = car("Tesla","x",2006,4)
myCar.get_info()