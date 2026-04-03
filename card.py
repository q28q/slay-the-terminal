import abc
from scene import Battle
from global_func import *

class CardBase(abc.ABC):
    @abc.abstractmethod
    def use(self, battle: Battle, target):
        pass

    @abc.abstractproperty
    def name(self) -> str:
        pass

class Hit(CardBase):
    def __init__(self):
        self.value = 6

    @property
    def name(self) -> str:
        return '打击'

    def use(self, battle, target):
        hit(battle.players[0], battle.enemies, target, self.value)

class Defence(CardBase):
    def __init__(self):
        self.value = 6

    @property
    def name(self) -> str:
        return '防御'

    def use(self, battle):
        defence(battle.players[0], self.value)
