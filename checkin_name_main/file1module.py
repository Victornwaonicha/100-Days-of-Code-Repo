print("This is statement will be executed always")

def main():
    print("First file name is {}".format(__name__))

    a = 4
    b = 2

    c = a - b

    print(c)

if __name__== "__main__":
    main()