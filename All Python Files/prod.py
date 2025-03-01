# def prod(lst):
#     # Write code here
#     for i in range(lst):
#         lst = lst * i
#     return lst
# 
# lst = [1, 3, 5, 7]
# result = prod(lst)
# print(result)




def prod(lst):
    
    result = 1

    for num in lst:
        result *= num

    return result

lst = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

result = prod(lst)
print(result)



