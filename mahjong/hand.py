""" The tiles each player has """
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
    split_interval: int = 2

    def __post_init__(self) -> None:
        """Parse the raw tiles input from string to Tile object
        """
        # split the raw input every split interval length for the shortest input
        # e.g. 1w2b -> [1w, 2b]
        raw_tiles = [self.raw_tiles[i:i + self.split_interval]
                     for i in range(0, 
                                    len(self.raw_tiles), 
                                    self.split_interval)]
        
        self.tiles = [Tile(suit=x[1], number=int(x[0]))
                      for x in raw_tiles]

    def is_valid_hand(self,
                      rules: Rules) -> bool:
        """Check if the hand is valid according to the given rule

        Args:
            rules (Rules): Rules object with predetermined rules

        Returns:
            bool: return whether the hand is valid
        """
        # Check total tile count
        if len(self.tiles) != rules.hand_count:
            print("Hand count does not match the rules. Did you forget to "
                  "draw?")
            return False
        else:
            return True

    @staticmethod
    def group_by_suit(hand: List[Tile]) -> Dict[str, List[Tile]]:
        """Group each hand by suit so it can be used for Parts generation

        Args:
            hand (List[Tile]): List of Tile objects that represent the hand

        Returns:
            Dict[str, List[Tile]]: groups by hand in {'w': [<Tile>, <Tile>] ...} 
            format with key being the string representation of suit, and value
            is a list of the tile numbers
        """
        group_dict = defaultdict(list)
        for x in hand:
            group_dict[x.suit].append(x)

        return group_dict

    def breakdown_groups(self) -> List[Group]:
        """Generate groups from the hand
        
        Args (self):
            self.tiles: List of Tiles objects

        Returns:
            List[Group]: a list of groups than can be used to find best tiles
            to draw
        """
        group_dict = self.group_by_suit(self.tiles)
        group_maker = GroupMaker(group_dict=group_dict)
        groups = group_maker.make_groups()
        
        return groups
