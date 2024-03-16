def values(lst):
    for i in range(len(lst)):
        print(lst[i])

# Get user input for the list
my_list = input("Enter the list elements separated by spaces: ").split()

# Call the function with the provided list
values(my_list)
