###### INHERITANCE #######

# Parent Class
class Vehicle:
    def __init__(self, color, model):
        self.color = color
        self.model = model
    
    def start(self):
        return f"The {self.color} {self.model} is starting now"
    

#Child Class
class Car(Vehicle): # Inheriting from the Vehicle class.
    def __init__(self, color, model, year): 
        super().__init__(color, model) # Calling the constructor of the Vehicle class.
        self.year = year
        
    def drive(self):
        return f"The {self.color} {self.model} is driving."
    

my_car = Car('white', 'Honda', 2023)
sister_car = Car('red', 'BMW', 2025)

print(my_car.start())
print(sister_car.drive())
    
    
    
    


