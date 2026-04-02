from global_func import *

# 卡牌基类
class Card:
    def __init__(self):
        self.name = ''

    def use(self, battle, target):
        pass

class Hit(Card):
    def __init__(self):
        self.name = '打击'
        self.damage = 6

    def use(self, battle, target):
        hit(battle.players[0], battle.enemies, target, self.damage)
