from rich.console import Console
from rich.live import Live
r = Console()

import dsStorage as dsS
from style import createStatMenu

class Character:
    def __init__(self, name, initialStatList):
        self.name = name
        self.initialStatList = initialStatList
        self.stats = {
            "Level": 0,
            "Vigor": 0,
            "Attunement": 0,
            "Endurance": 0,
            "Vitality": 0,
            "Strength": 0,
            "Dexterity": 0,
            "Intelligence": 0,
            "Faith": 0,
            "Luck": 0
        }
        self.setStats()
        self.soulQuantity = 0

    def setStats(self):
        keys = list(self.stats.keys())
        for i in range(len(self.initialStatList)):
            self.stats[keys[i]] = self.initialStatList[i]
        return

    def showStats(self):
        r.clear()  
        with Live(createStatMenu(list(self.stats.values()), self.soulQuantity, dsS.getSoulsRequired(self.stats["Level"]))):
            wait = input()
        return
    
    def upgrade(self, stat):
        level = self.stats["Level"]
        soulsRequired = dsS.getSoulsRequired(level)
        if self.soulQuantity < soulsRequired:
            return f"Insufficient souls, you need {soulsRequired} souls"
        if stat in self.stats:
            self.stats["Level"] += 1
            self.stats[stat] += 1
            self.soulQuantity -= soulsRequired
            return f"Successfullly upgraded {stat}"
        else:
            return f"Error: Invalid stat"

    def getSouls(self, quantity):
        self.soulQuantity += quantity
        