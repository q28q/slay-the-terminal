class Enemy:
    def __init__(self):
        self.name = ''
        self.max_health = 80
        self.health = 80
        self.buffs = []

    def action(self):
        pass

class SmallRed(Enemy):
    def __init__(self):
        super().__init__()
        self.name = '地精大块头'
