class Dog:
    # Self just allow an object to refer to itself just like a human can use "Myself" such as my food my shoe.
    def __init__(self, name="", height=0, weight=0):

        # Self. is the attribute of the class Dog
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print("{} the dog runs".format(self.name))

    def eat(self):
        print("{} the dog eats".format(self.name))

    def bark(self):
        print("{} the dog barks".format(self.name))


def main():
    spot = Dog("Spot", 66, 26)

    spot.bark()

    bowser = Dog()
    bowser.name = "Bowser"
    bowser.bark()



main()



