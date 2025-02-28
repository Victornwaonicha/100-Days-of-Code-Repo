############DEBUGGING#####################

# Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# Play computer
# year = int(input("What is your year of birth? "))
# if year >= 1980 and year < 1995:
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z!")

# Fix the Error
# age = int(input("What is your age?"))
# if age > 18:
#     print(f"You can drive at age {age}")
# elif age < 18:
#     print("You can only start driving when you are 18!")

# Print is your friend
# pages = 0
# word_paper_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13 ])