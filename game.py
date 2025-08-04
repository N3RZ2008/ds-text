import dsStorage
import utility as ut
from character import Character

class Game():
    def __init__(self):
        pass
    def createCharacter(self):
        charName = input("Your name: ")
        for i in range(len(dsStorage.ClassesIDs)):
            print(f"[{i}] {dsStorage.ClassesIDs[i]}")
        charClass = int(input("Choose your class:"))

        return Character(charName, dsStorage.ClassesStats[dsStorage.ClassesIDs[charClass]])
    def simulation(self, character):
        while True:
            ut.clear()
            action = int(input(
                "[0] Leave\n[1] Get souls\n[2] Upgrade\n[3] Show Stats\nChoose: "
            ))
            ut.clear()
            if action == 0:
                break
            elif action == 1:
                quantity = int(input("How much: "))
                character.getSouls(quantity)
            elif action == 2:
                print("Choose stat")
                print()
                statList = list(character.stats.keys())
                for i in range(1, len(statList)):
                    print(f"[{i}] {statList[i]}")
                stat = int(input("Choose: "))
                print()
                print(character.upgrade(statList[stat]))
                print()
            elif action == 3:
                character.showStats()
            else:
                pass
            

