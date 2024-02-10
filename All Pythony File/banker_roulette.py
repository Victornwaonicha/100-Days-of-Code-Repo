# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

random_index = random.randint(0, len(names) -1)
selected_person = names[random_index]

print(f"{selected_person} has been selected and he will pay for the food bills")