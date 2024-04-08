def calculate_product(num1, num2):
    product = num1 * num2
    return product

# Get user input with prompts
get_num1 = int(input("Enter the first number: "))
get_num2 = int(input("Enter the second number: "))

# Call the function
result = calculate_product(get_num1, get_num2)

# Print the result
print(f"The product is {result}")