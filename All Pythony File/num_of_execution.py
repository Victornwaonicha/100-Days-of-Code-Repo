# def sum_numbers():
#     local_sum = 0  
#     for i in range(1, 10000 + 1): 
#         local_sum = local_sum + i
#     return local_sum  # Return the calculated sum

# n = int(input("Enter the number of times for execution: "))
# for i in range(1, n + 1):
#     result = sum_numbers()  # Call the sum_numbers function
#     print(f"Sum for iteration {i}: {result}")
    



global_sum = 0

def sum_numbers():
    local_sum = 0
    for i in range(1, 10000 + 1):
        local_sum = local_sum + i
    return local_sum

n = int(input())
for i in range(n):
    result = sum_numbers()
    global_sum += result  # Add the local sum to the global sum
    print(f"Sum for iteration {i + 1}: {result}")

print(f"Total sum across all iterations: {global_sum}")