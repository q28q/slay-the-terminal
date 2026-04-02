from global_func import *

class Hit:
    def __init__(self):
        self.name = '打击'
        self.damage = 6

    def use(self, battle, target):
        hit(battle.players[0], battle.enemies, target, self.damage)
