def add(x, y) -> int:
    if x < y:
        if x == 0:
            return y
        else:
            return x + y
    elif x > y:
        return x - y
    elif x == y:
        return f"x and y are equal and the answer is {x + y}"
    else:
        return x * y


x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

w = add(x, y)
# w = x + y
print(w)
