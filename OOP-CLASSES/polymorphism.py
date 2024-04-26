#### POLYMORPHISM ####

class Animal:
    def make_sound(self):
        pass      # Placeholder method, to be overridden by subclasses.
    

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
    
# Creating instances of Dog and Cat classes
dog = Dog()
cat = Cat()

# Using the make_sound method on each instance
print(dog.make_sound())
print(cat.make_sound())