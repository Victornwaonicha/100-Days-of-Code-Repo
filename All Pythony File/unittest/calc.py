def add(a, b):
    """ADD FUNCTION"""
    return a + b


def substract(a, b):
    """SUBSTRACT FUNCTION"""
    return a - b


def multiply(a, b):
    """MULTIPLY FUNCTION"""
    return a * b


def divide(a, b):
    """DIVIDE FUNCTION"""
    if b == 0:
        raise ValueError("Can not divide by zero")
    return a / b




