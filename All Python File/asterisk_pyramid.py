n = int(input("Enter the value of n (an odd whole number): "))

# Determine the number of rows by using a floor division.
num_rows = (n + 1) // 2

# Iterate through each row
for i in range(1, num_rows + 1):
    num_spaces = num_rows - i
    num_asterisks = 2 * i - 1
    
# Print the spaces
    print(" " * num_spaces, end="")

    # Print the asterisks
    print("*" * num_asterisks)