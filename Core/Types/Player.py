from typing import Any

class Player(object):
    def __init__(self, player_id: Any, card: str):
        self.id = player_id
        self.card = card
        