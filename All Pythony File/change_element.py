def change_element(lst, index, new_element):
    lst[index] = new_element
    return lst

my_list = input("Enter the list elements separated by spaces: ").split().sort()

modified_list = change_element(my_list, 2, 10)
print(modified_list)