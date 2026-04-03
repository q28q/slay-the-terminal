from typing import List
import card

class Character:
    name: str
    max_health: int
    health: int
    card_suite: List[card.CardBase]

    def __init__(
        self,
        name: str,
        max_health: int = 80,
        init_health: int = None,
        card_suite: List[card.CardBase] = [],
    ):
        self.name = name
        self.armor = 0
        self.max_health = 80
        self.health = init_health if init_health is not None else max_health
        self.card_suite = card_suite
        self.potions = []

class BrokenRobot(Character):
    def __init__(self):
        card_suite = [
            card.Hit(),
            card.Defence(),
        ]

        super().__init__(
            name='故障机器人',
            card_suite=card_suite,
        )

