import card

class Player:
    def __init__(self):
        self.max_health = 80
        self.health = 80
        self.cards = []
        self.potions = []
        self.buffs = []

class BrokenRobot(Player):
    def __init__(self):
        super().__init__()
        hit_card = card.Hit()
        self.cards.append(hit_card)
