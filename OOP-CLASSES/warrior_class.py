import random
import math


# Warrior & Battle Class

class Warrior:
    def __init__(self, name="Warrior", health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax

    def attack(self):
        attkAmt = self.attkMax * (random.random() + 0.5)
        return attkAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() + 0.5)
        return blockAmt

class Battle:
    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAttkAmt = warriorA.attack()
        warriorBBlockAmt = warriorB.block()

        damage2WarriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)
        warriorB.health = warriorB.health - damage2WarriorB

        print("{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name, damage2WarriorB))
        print("{} is now at {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} has died and {} is the winner".format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Fight Again"

def main():

    # maximus = Warrior("Maximus", 50, 20, 10)
    # galaxon = Warrior("Galaxon", 50, 20, 10)

    # battle = Battle()
    # battle.startFight(maximus, galaxon)

    name1 = input("Enter the name for warrior 1: ")
    name2 = input("Enter the name for warrior 2: ")

    # Create warrior objects with the entered names
    warrior1 = Warrior(name1, 50, 20, 10)
    warrior2 = Warrior(name2, 50, 20, 10)

    # Start the battle
    battle = Battle()
    battle.startFight(warrior1, warrior2)

main()

