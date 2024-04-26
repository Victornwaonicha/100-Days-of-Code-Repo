class Car:
    def __init__(self, color, model, repair):
        self.color = color
        self.model = model
        self.repair = repair
    
    def drive(self):
        return f"The {self.color} {self.model} is driving now"
    def service(self):
        return f"The {self.color} {self.model} is in for {self.repair}"
    
my_car = Car("blue", "BMW", "repair")
sister_car = Car("yellow", "Toyota", "repair")

print(my_car.drive())
print(sister_car.service())

