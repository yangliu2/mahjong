from tokenize import group
from typing import List, Dict
from mahjong.tile import Tile
from mahjong.rules import Rules
from mahjong.group import Group
from mahjong.group_maker import GroupMaker
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Hand:
    raw_tiles: str

    def __post_init__(self) -> None:
        self.tiles = [Tile(suit=x[1], number=int(x[0]))
                      for x in self.raw_tiles]

    def check_hand(self,
                   rules: Rules):
        # Check total tile count
        if len(self.tiles) != rules.hand_count:
            print("Hand count does not match the rules. Did you forget to "
                  "draw?")

    @staticmethod
    def group_by_suit(hand: List[Tile]) -> Dict[str, List[Tile]]:
        """Group each hand by suit so it can be used for Parts generation

        Args:
            hand (List[Tile]): List of Tile objects that represent the hand

        Returns:
            Dict[str, List[Tile]]: groups by hand in {'w': [<Tile>, <Tile>] ...} 
            format with key being the string representaiton of suit, and value 
            is a list of the tile numbers
        """
        group_dict = defaultdict(list)
        for x in hand:
            group_dict[x.suit].append(x)

        return group_dict

    def breakdown_groups(self) -> List[Group]:
        group_dict = self.group_by_suit(self.tiles)
        parts_maker = GroupMaker(group_dict=group_dict)
        parts = parts_maker.make_groups()
        print(parts)
