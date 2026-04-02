from global_func import *

class Hit:
    def __init__(self):
        self.name = '打击'
        self.value = 6

    def use(self, battle, target):
        hit(battle.players[0], battle.enemies, target, self.value)

class Defence:
    def __init__(self):
        self.name = '防御'
        self.value = 6

    def use(self, battle):
        defence(battle.players[0], self.value)
