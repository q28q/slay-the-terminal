print('hello spire')

import player
import scene
import enemy
from global_func import *

jibao = player.BrokenRobot()
small_red = enemy.SmallRed()
battle = scene.Battle([jibao], [small_red])

draw(battle)
battle.start()
