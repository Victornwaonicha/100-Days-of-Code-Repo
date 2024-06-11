matrix_4by4 = [["a", "b", "c", "d"], 
               ["e", "f", "g", "h"], 
               ["i", "j", "k", "l"], 
               ["m", "n", "o", "p"]]
matrix_3by3 =  [
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]
]

ord_list = [1, 2, 3,4, 5]


# def matrix_f(x):
#     for row in x:
#         for i in row:
#             print(i)
        

# def matrix_g(x):
#     selected_index = f"{matrix_4by4[0][0]}\n{matrix_4by4[1][1]}\n{matrix_4by4[2][2]}\n{matrix_4by4[3][3]}"

# store = "row"    

def matrix_f(x):
    if (type(x) != list):
        print("this is not a list")
        return
    for i in range(len(x)):
        if (type(x[i]) != list):
            return
        print(x[i][i])     
            # print(matrix_4by4[1]) 
            # print(matrix_4by4[2])  
            # print(matrix_4by4[3])


# def matrix_f(x):
#     for row in x:
#         print(" ".join(row))



# print(matrix_4by4[0][3])

# matrix_4by4[0][0] = "z"

# print(matrix_4by4)


matrix_f(matrix_3by3)
print("______")
matrix_f(matrix_4by4)
print("----"*4)
matrix_f(ord_list)







