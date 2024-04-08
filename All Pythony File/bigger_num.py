iterations = int(input())
num1 = int(input())
num2 = int(input())

def bigger(arg1, arg2):
    if arg1 >= arg2:
        return arg1
    else:
        return arg2

for i in range(iterations):
    result = bigger(num1, num2)
    larger = result / 2
    print(larger)
    
    if larger < 2:
        break
    
    if num1 >= num2:
        num1 = larger
    else:
        num2 = larger