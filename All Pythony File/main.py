import random
import my_module

value = 500
ran_num = random.randint(30, 90)
print(ran_num)

ran_float = random.randint(0, 5)
float_now= float(ran_float)
print(float_now)

print(value - my_module.sum)