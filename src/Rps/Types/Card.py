from abc import ABC


class Card(ABC):
    """
    Reprecent a card whitch can be used in a Rps Battle.
    """
    def __init__(self, tag: str, can_win_tags: list):
        self.__tag = tag
        self.__can_win_tags = can_win_tags

    @property
    def Tag(self):
        """Card tag
        """
        return self.__tag

    def CanWin(self, card: "[Card|str]"):
        if isinstance(card, Card):
            card = card.Tag

        return card in self.__can_win_tags

    def __eq__(self, obj: "Card"):
        return obj.Tag == self.Tag


class Rock(Card):
    def __init__(self):
        super().__init__(
            "rock",
            ["sponge", "wolf", "tree", "human", "snake", "scissors", "fire"])


class Scissors(Card):
    def __init__(self):
        super().__init__(
            "scissors",
            ["snake", "human", "tree", "wolf", "sponge", "paper", "air"])


class Paper(Card):
    def __init__(self):
        super().__init__(
            "paper",
            ["air", "water", "dragon", "devil", "lighting", "gun", "rock"])


class Gun(Card):
    def __init__(self):
        super().__init__(
            "gun",
            ["wolf", "tree", "human", "snake", "scissors", "fire", "rock"])


class Lighting(Card):
    def __init__(self):
        super().__init__(
            "lighting",
            ["tree", "human", "snake", "scissors", "fire", "rock", "gun"])


class Devil(Card):
    def __init__(self):
        super().__init__(
            "devil",
            ["human", "snake", "scissors", "fire", "rock", "gun", "lighting"])


class Dragon(Card):
    def __init__(self):
        super().__init__(
            "dragon",
            ["snake", "scissors", "fire", "rock", "gun", "lighting", "devil"])


class Water(Card):
    def __init__(self):
        super().__init__(
            "water",
            ["scissors", "fire", "rock", "gun", "lighting", "devil", "dragon"])


class Air(Card):
    def __init__(self):
        super().__init__(
            "air",
            ["fire", "rock", "gun", "lighting", "devil", "dragon", "water"])


class Sponge(Card):
    def __init__(self):
        super().__init__(
            "sponge",
            ["dragon", "water", "air", "devil", "lighting", "gun", "paper"])


class Wolf(Card):
    def __init__(self):
        super().__init__(
            "wolf",
            ["dragon", "water", "air", "devil", "lighting", "sponge", "paper"])


class Tree(Card):
    def __init__(self):
        super().__init__(
            "tree",
            ["dragon", "water", "air", "devil", "wolf", "sponge", "paper"])


class Human(Card):
    def __init__(self):
        super().__init__(
            "human",
            ["dragon", "water", "air", "tree", "wolf", "sponge", "paper"])


class Snake(Card):
    def __init__(self):
        super().__init__(
            "snake",
            ["air", "water", "human", "tree", "wolf", "sponge", "paper"])


class Fire(Card):
    def __init__(self):
        super().__init__(
            "fire",
            ["scissors", "snake", "human", "tree", "wolf", "sponge", "paper"])
