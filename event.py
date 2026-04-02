from global_func import *

class Battle:
    def __init__(self, players, enemies):
        self.players = players
        self.enemies = enemies

    def start(self):
        while self.enemies[0].health > 0:
            action = input('>>')
            if action == 'hit':
                self.players[0].cards[0].use(self, 0)
            elif action == 'defence':
                self.players[0].cards[1].use(self)
            else:
                print('指令错误')
            draw(self)
