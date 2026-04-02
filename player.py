import card

class Player:
    def __init__(self):
        self.name = ''
        self.max_health = 80
        self.health = 80
        self.armour = 0
        self.cards = []
        self.potions = []
        self.buffs = []

class BrokenRobot(Player):
    def __init__(self):
        super().__init__()
        self.name = '故障机器人'

        hit_card = card.Hit()
        self.cards.append(hit_card)
        defence_card = card.Defence()
        self.cards.append(defence_card)
