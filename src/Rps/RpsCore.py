from .Types.Card import (
    Card,
    Rock, Paper, Scissors,
    Gun, Lighting, Devil, Dragon,
    Water, Air, Sponge, Wolf, Tree,
    Human, Snake, Fire
)
from .Types.Player import Player
from typing import List, Dict
from random import choice
from .Match import Match
import uuid


class RpsCore:
    def __init__(self):
        self.__valid_tags: List[Card] = [
            Rock(),  Paper(),    Scissors(),
            Gun(),   Lighting(), Dragon(),
            Devil(), Wolf(),     Water(),
            Air(),   Human(),    Snake(),
            Fire(),  Tree(),     Sponge(),
        ]
        self.__matches: Dict[str, Match] = {}

    def GetMatch(self, match_id: str, out=None) -> Match:
        return self.__matches.get(match_id, out)

    @property
    def NewMatch(self) -> str:
        match_id = str(uuid.uuid4())
        while(match_id in self.__matches):
            match_id = str(uuid.uuid4())

        match = Match(self)
        self.__matches[match_id] = match
        return match_id

    def Random(self, to_skip: List[str] = []):
        return choice([x for x in self.__valid_tags if x.Tag not in to_skip])

    @property
    def AllCards(self):
        return self.__valid_tags

    def IsValid(self, card: str):
        return any([x for x in self.__valid_tags if x.Tag])

    def GetCard(self, tag):
        for x in self.__valid_tags:
            if x.Tag == tag:
                return x

    def Fight(self, card1: str, card2: str) -> str:
        if not self.IsValid(card1) or not self.IsValid(card2):
            return None

        card1 = self.GetCard(card1)
        card2 = self.GetCard(card2)

        if card1 == card2:
            return "draw"

        if card1.CanWin(card2):
            return card1.Tag
        else:
            return card2.Tag

    def PlayerFight(self, player1: Player, player2: Player) -> Player:
        res = self.Fight(player1.card, player2.card)
        if res:
            if player2.card == res:
                return player2
            else:
                return player1
