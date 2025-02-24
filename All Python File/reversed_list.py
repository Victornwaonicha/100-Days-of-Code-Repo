def reverse(lst):
    reversed_list = []

    # Iterate through the list in reverse order
    for i in range(len(numbers) - 1, -1, -1):
        reversed_list.append(numbers[i])

    return reversed_list

numbers = [1, 2, 3]
reversed_numbers = reverse(numbers)
print(reversed_numbers)