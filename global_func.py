def hit(player, enemies, target, damage):
    enemies[target].health -= damage

def draw(battle):
    print(battle.players, 'vs', battle.enemies, battle.enemies[0].health)
