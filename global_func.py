def hit(player, enemies, target, value):
    enemies[target].health -= value

def defence(player, value):
    player.armour += value

def draw(battle):
    print(battle.players[0].name, battle.players[0].armour, 'vs', battle.enemies[0].name, battle.enemies[0].health)
