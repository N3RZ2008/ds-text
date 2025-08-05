# Armazenamento de informações relativas ao jogo
import math

def getSoulsRequired(level):
    earlyLevelsRequirement = [0, 0, 673, 690, 707, 724, 741, 758, 775, 793, 811, 829]
    if level < 12:
        return earlyLevelsRequirement[level]
    else:
        return math.floor(0.02*level**3 + 3.06*level**2 + 105.6*level - 895)

ClassesStats = {
    "Knight": [9,12,10,11,15,13,12,9,9,7],
    "Mercenary": [8,11,12,11,10,10,16,10,8,9],
    "Warrior": [7,14,6,12,11,16,9,8,9,11],
    "Herald": [9,12,10,9,12,12,11,8,13,11],
    "Thief": [5,10,11,10,9,9,1,10,8,14],
    "Assassin": [10,10,14,11,10,10,144,11,9,10],
    "Sorcerer": [9,16,9,7,7,12,16,7,12],
    "Pyromancer": [8,11,12,10,8,12,9,14,14,7],
    "Cleric": [7,10,14,9,7,12,8,7,16,13],
    "Deprived": [1,10,10,10,10,10,10,10,10,10]
}
ClassesIDs = list(ClassesStats.keys())
