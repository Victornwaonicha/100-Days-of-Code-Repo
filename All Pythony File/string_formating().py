# name = "victor"
# age = 30
# 
# formated_St = "My name is {} and I am {} years old.".format("Victor", 30)
# print(formated_St)

# item = "apple"
# cost = 0.99
# formated_string = "The cost of one {1} is {0:.2f}".format(0.99, "apple")
# print(formated_string)


# formating with dictionaries
# data = {"item": "banana", "cost": 0.49}
# formated_string = "The cost of one {item} is {cost:.2f}".format(**data)
# print(formated_string)


# formating with class
# class Fruit:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         
#         
# fruit = Fruit("orange", 0.79)
# formated_string = "The cost of one {0.name} is  {0.price:.2f}".format(fruit)
# print(formated_string)



# formating with list
# fruit = ["apple", "banana", "cherry"]
# formated_string = "The first fruit is {0[2]}".format(fruit)
# print(formated_string)



# formating with  Enum
# from enum import Enum 
# class Animal(Enum):
#     CAT =1
#     DOG = 2
#     BIRD = 3
#     
# formated_string = "The selected animal is {0.name}".format(Animal.CAT)
# print(formated_string)




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __format__(self, format_spec):
        if format_spec == "age":
            return str(self.age)
        return self.name
    
person = Person("Herbert", 30)   
formated_string = "Name: {:}, Age: {:age}".format(person, person)
print(formated_string)
    
    
    
    
# YOUTUBE VIDEO: https://youtu.be/vTX3IwquFkc?si=LEdmaYtCA2_24ifX