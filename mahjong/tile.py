from mahjong.suit import Suit

class Tile:
    def __init__(self,
                 suit: Suit,
                 number: int) -> None:
        self.suit = suit
        self.number = number

    def __str__(self):
        return f"{self.number}{self.suit}"
