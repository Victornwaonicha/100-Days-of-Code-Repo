# def is_valid(username, password):
#     if username == "admin":
#         return True
#     elif username == "user" and password == "qweasd":
#         return True
#     else:
#         return False 
# 
# username = "user"
# password = "qweasd"
# 
# is_valid_result = is_valid(username, password)
# 
# print(is_valid_result)



def is_valid(username, password):
    if username == "admin":
        return True
    elif username == "user" and password == "qweasd":
        print("You got it", True, "this time.")
        return True
    else:
        return False
    
username = input("Enter a valid username: ")
password = input("Enter a valid password: ")

is_valid_result = is_valid(username, password)

print(is_valid_result)