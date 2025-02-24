# Initialize the sum to zero
even_sum = 0

for number in range(1, 101):
    if number % 2 == 0: # Check if the number is even
        even_sum = even_sum + number
        
print(even_sum)
       