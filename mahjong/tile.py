from mahjong.suit import Suit, SuitEnum
from typing import List
from dataclasses import dataclass, field

@dataclass(order=True)
class Tile:
    suit: Suit = field(compare=False)
    number: int = field(compare=True)
    
    # def __str__(self):
    #     return f"{self.number}{self.suit}"