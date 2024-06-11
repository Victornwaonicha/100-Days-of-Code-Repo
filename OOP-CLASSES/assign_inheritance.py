#### INHERITANCE 2 ####

class Animal:
    def __init__(self, species):
        self.species = species
     
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
class Bird(Animal):
    def make_sound(self):
        return "Tweet!"
    
    
# Creating instances of Dog and Cat classes
dog = Dog("Canine")
cat = Cat("Feline")
bird = Bird("Egyptian goose")

# Using the make_sound method on each instance
print(dog.species)
print(dog.make_sound())
print(cat.species)
print(cat.make_sound())
print(bird.species)
print(bird.make_sound())
