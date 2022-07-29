from typing import List
from mahjong.tile import Tile
from mahjong.rules import Rules

class Hand:
    def __init__(self, raw_tiles: List[str]) -> None:
        self.hand = [Tile(suit=x[1], number=x[0]) for x in raw_tiles]

    def check_hand(self, 
                   rules: Rules):
        # Check total tile count
        if len(self.hand) != rules.hand_count:
            print("Hand count does not match the rules. Did you forget to "
                  "draw?")
