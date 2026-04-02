class Enemy:
    def __init__(self):
        self.max_health = 80
        self.health = 80
        self.buffs = []

    def action(self):
        pass

class SmallRed(Enemy):
    def __init__(self):
        super().__init__()
