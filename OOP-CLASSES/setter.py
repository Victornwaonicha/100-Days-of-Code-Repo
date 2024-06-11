class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("Retreiving the height")
        
        return self.__height

    @height.setter
    def height(self, value):
        
        if value.isdigit():
            self.__height = value
        else:
            print("Please only enter a valid number for height")

    @property
    def width(self):
        print("Retreiving the width")
        
        return self.__width

    @width.setter
    def width(self, value):
        
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter a valid number for width")

    def get_area(self):
        return int(self.__height) * int(self.__height)

def main():
    aSquare = Square()

    height = input("Enter the height of the square: ")
    width = input("Enter the width of the square: ")

    aSquare.height = height
    aSquare.width = width

    print("Height :", aSquare.height)
    print("Width :", aSquare.width)

    print("The Area of the square is: ", aSquare.get_area())

if __name__ == "__main__":
    main()
