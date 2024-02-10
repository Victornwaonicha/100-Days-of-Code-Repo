# #Functions with Outputs and using DocStrings

def format_name(f_name, l_name):
  """Take a first and last name and format it 
     to return the title case version of the name."""
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()

  return f"{formated_f_name} {formated_l_name}"


print(format_name("victor", "nwaonicha"))
output = len("Nwaonicha")








# ------------------------------------------------


# def format_name(f_name, l_name):
#   if f_name == "" or l_name == "":
#     return "You didn't provide valid inputs."
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()
#   f"Result: {formated_f_name} {formated_l_name}"

# #Storing output in a variable
# formatted_name = format_name(input("Your first name: "), input("Your last name: "))
# print(formatted_name)
# #or printing output directly
# print(format_name(input("What is your first name? "), input("What is your last name? ")))

# #Already used functions with outputs.
# length = len(formatted_name)

# #Return as an early exit
# def format_name(f_name, l_name):
#   if f_name == "" or l_name == "":
#     return "You didn't provide valid inputs."
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()
#   return f"Result: {formated_f_name} {formated_l_name}"

#Calculator

# def add(n1, n2):
#   """Add n1 to n2"""
#   return n1 + n2

# def subtract(n1, n2):
#   """Subtracts n2 from n1"""
#   return n1 - n2

# def multiply(n1, n2):
#   return n1 * n2

# def divide(n1, n2):
#   return n1 / n2

# def square(n):
#   return n * n

# operations = {
#   "+": add,
#   "-": subtract,
#   "*": multiply,
#   "/": divide
# }

# num1 = int(input("What's the first number?: "))
# for symbol in operations:
#   print(symbol)
# operation_symbol = input("Pick an operation from the line above: ")
# num2 = int(input("What's the second number?: "))
# calculation_function = operations[operation_symbol]
# answer = calculation_function(num1, num2)
# answer = square(answer)

# print(f"{num1} {operation_symbol} {num2} = {answer}")