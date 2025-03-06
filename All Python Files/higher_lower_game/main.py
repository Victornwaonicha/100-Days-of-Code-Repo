# Higher Lower Game To-Do List:
# 1. Import necessary modules
import os
import random
from random import choice


# 2. Set up data & art
from game_data import data
from art import logo, vs

# 3. Display game intro and rules
name = input("What is your name?: ")

print(logo)

print(f"Welcome to the Higher Lower Game {name}!")
print("Guess which has more followers: A or B?")


# 4. Pick two random options (A and B) from data
option_a = choice(data)
option_b = choice(data)
while option_a == option_b:
    option_b = choice(data)



# # 5. Show A and B to player with details (hide follower counts)
select_1 = f"Compare A: {option_a['name']}, a {option_a['description']} from {option_a['country']}"
select_2 = f"Compare B: {option_b['name']}, a {option_b['description']} from {option_b['country']}"


print(select_1)
print(vs)
print(select_2)


# 6. Get player’s guess (A or B)
answer = input("Which has more followers, A or B:").upper()




# 7. Compare follower counts to check if guess is correct
is_correct = False
count_a = option_a['follower_count']
count_b = option_b['follower_count']
if count_a > count_b and answer == "A":
    is_correct = True
elif count_b > count_a and answer == "B":
    is_correct = True
else:
    is_correct = False




score = 0
# 8. Give feedback (right/wrong) and update score
if is_correct:
    score = score +1
    print(f"You are right! Current score: {score}")
else:
    print(f"Sorry, that's wrong.")
os.system('clear')






# 9. Repeat with new B (A becomes old B if correct) until wrong guess
while is_correct:
    option_a = option_b
    while option_a == option_b:
        option_b = choice(data)
    select_1 = f"Compare A: {option_a['name']}, a {option_a['description']} from {option_a['country']}"
    select_2 = f"Compare B: {option_b['name']}, a {option_b['description']} from {option_b['country']}"

    print(logo)
    print(f"You are right! Current score is now: {score}")
    print(select_1)
    print(vs)
    print(select_2) 

    answer = input("Which has more followers, A or B:").upper()

    is_correct = False
    count_a = option_a['follower_count']
    count_b = option_b['follower_count']
    if count_a > count_b and answer == "A":
        is_correct = True
    elif count_b > count_a and answer == "B":
        is_correct = True
    else:
        is_correct = False



    if is_correct:
        score = score +1
        print(f"You are right! Current score is now: {score}")
    else:
        print(f"Sorry, you got it wrong.")
    os.system('clear')

    
        



# 10. End game with final score
print(logo)
print(f"Game over, final score: {score}")







