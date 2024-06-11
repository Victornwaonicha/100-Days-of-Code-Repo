class Fraction(object):
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        top = self.num * other.den + self.den * other.num
        bottom = self.den * other.den
        return Fraction(top, bottom)

    def __sub__(self, other):
        top = self.num * other.den - self.den * other.num
        bottom = self.den * other.den
        return Fraction(top, bottom)

    def __float__(self):
        return self.num / self.den

    def inverse(self):
        return Fraction(self.den, self.num)
