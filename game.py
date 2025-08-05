import inquirer
from rich.console import Console
r = Console()

import dsStorage as dsS
from character import Character

class Game():
    def __init__(self):
        pass
    def createCharacter(self):
        charName = input("Your name: ")
        questions = [
            inquirer.List(
                "class",
                message="Choose your Class:",
                choices=dsS.ClassesIDs
            )
        ]
        choice = inquirer.prompt(questions)
        # for i in range(len(dsS.ClassesIDs)):
        #     print(f"[{i}] {dsS.ClassesIDs[i]}")
        # charClass = int(input("Choose your class:"))

        return Character(charName, dsS.ClassesStats[choice["class"]])
    def simulation(self, character):
        while True:
            r.clear()
            action = input(
                "[0] Leave\n[1] Get souls\n[2] Upgrade\n[3] Show Stats\nChoose: "
            )
            r.clear()
            if action == "0" or "":
                break
            elif action == "1":
                quantity = int(input("How much: "))
                character.getSouls(quantity)
            elif action == "2":
                print("Choose stat")
                print()
                statList = list(character.stats.keys())
                for i in range(1, len(statList)):
                    print(f"[{i}] {statList[i]}")
                stat = int(input("Choose: "))
                print()
                print(character.upgrade(statList[stat]))
                print()
            elif action == "3":
                character.showStats()
            else:
                pass
            