class Person:
    """
    Defines a square
    Attributes:
        size: size of the square
    """

    def __init__(self, shoe_size=0, height=None, name=None):
        """
        method for class 'Square'
        Args:
            size
        """
        if not (isinstance(shoe_size, int)):
            raise TypeError("size must be an integer")
        else:
            if shoe_size < 20:
                raise ValueError("size must be >= 20")

        self.__size = shoe_size
        self.__height = height
        self._name = name

        

    # def use_s1(self):
    #     return f"My name is {self._name} and my shoe size is {self.__size}, I need to see other sizes you have in stock."
    

    # def use_s2(self):
    #     return f"My height is about {self.__height}"+ "ft" +", I think I am tall enough to play a basketball!"




sean = Person(42, 3, "Sean")
# print(sean.use_s1())


# victor = Person(42, 5.7, None)
# print(victor.use_s2())

print(sean.__size)