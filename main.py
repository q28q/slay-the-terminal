print('hello spire')

import player
import event
import enemy
from global_func import *

jibao = player.BrokenRobot()
small_red = enemy.SmallRed()
battle = event.Battle([jibao], [small_red])

draw(battle)
battle.start()
