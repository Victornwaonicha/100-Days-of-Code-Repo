# Sample list of numbers
numbers = [10, 5, 8, 20, 3, 15]

# Initialize a variable to store the maximum value
max_number = numbers[0]  # Assume the first number is the maximum

# Iterate through the list
for number in numbers:
    if number > max_number:
        max_number = number

# After the loop, max_number will contain the highest number in the list
print("The highest number is:", max_number)