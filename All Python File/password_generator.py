#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Step 1: Welcome Message
print("Welcome to the PyPassword Generator!")

# Step 2: User Input
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Step 3: Generating the Password
password = ""

# Generate random letters
for _ in range(nr_letters):
    password = password + random.choice(letters)
    # Add a random letter to the password
    # You can use random.choice() to select a random character from the 'letters' list
    # Append the selected character to the 'password' variable
    # Hint: password += random.choice(letters)
    
# Generate random symbols
for _ in range(nr_symbols):
    password = password + random.choice(symbols)
    # Add a random symbol to the password
    # You can use random.choice() to select a random character from the 'symbols' list
    # Append the selected character to the 'password' variable
    # Hint: password += random.choice(symbols)

# Generate random numbers
for _ in range(nr_numbers):
    password += random.choice(numbers)
    # Add a random number to the password
    # You can use random.choice() to select a random character from the 'numbers' list
    # Append the selected character to the 'password' variable
    # Hint: password += random.choice(numbers)

# Step 4: Combine the Password Components (Combine them by shuffling)
password_list = list(password)  # Convert the password string to a list
# random.shuffle(password_list)   # Shuffle the characters randomly
# password = ''.join(password_list)  # Join the shuffled characters back into a string

# Step 5: Display the Password
print(f"Your generated password is: {password}")