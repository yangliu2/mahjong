""" Group tiles into group to better analysis which tile to discard """
import logging
from mahjong.group import Group
from mahjong.tile import Tile
from mahjong.utils import find_friends, find_chow_tiles
from typing import Dict, List
from dataclasses import dataclass
from collections import Counter

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


@dataclass
class GroupMaker:
    group_dict: Dict[str, List[Tile]]

    def group_suit(self,
                   tiles: List[Tile]) -> List[Group]:
        """ Group the tiles in hand into Groups that can be used to find what
        are the possible tiles that will be good to draw. Maximizing the number
        of useful tiles will help the player win faster. Tile that 
        doesn't group with other tiles will be put in its own group.

        Args:
            tiles (List[Tile]): List of Tiles objects 

        Returns:
            List[Group]: List of Group object that can be fed into complete_set
            method in Group to find possible good tiles to draw
        """
        sorted_tiles = sorted(tiles)
        groups = []

        # loop through all tiles using while. It's easier to modify list on
        # the fly using while
        while sorted_tiles:
            first_tile = sorted_tiles[0]
            to_be_added = list()
            to_be_added.append(first_tile)

            # If the chow melds or pong melts exists, group them first
            # for chow melds
            chow_set = find_chow_tiles(tile=first_tile)
            if chow_set and all(x in sorted_tiles for x in chow_set):
                groups.append(Group(tiles=chow_set))
                [sorted_tiles.remove(x) for x in chow_set]
                continue

            # for pong melds
            counter = Counter(sorted_tiles)
            if first_tile in counter:
                if counter[first_tile] >= 3:
                    group = Group(tiles=[first_tile] * 3)
                    groups.append(group)
                    [sorted_tiles.pop(0) for _ in range(3)]
                    continue

            # If there are no melds, then group using friends of the first
            # tiles.
            sorted_tiles.pop(0)
            while sorted_tiles:
                first_tile_friends = find_friends(first_tile)
                current_tile = sorted_tiles[0]
                if current_tile in first_tile_friends:
                    to_be_added.append(current_tile)
                    sorted_tiles.pop(0)
                # if the next tile does not group, start a new group
                else:
                    break

            # put to_be_removed in the group list
            group = Group(tiles=to_be_added)
            groups.append(group)

        return groups

    def make_groups(self) -> List[Group]:
        """Generating groups of tiles that can be used to determine what tiles
        are needed in the future drawing

        Returns:
            List[Group]: List of Groups that are useful being put together
        """
        groups = [self.group_suit(tiles=v)
                  for _, v in self.group_dict.items()]
        flattened_groups = [x for sub in groups for x in sub]
        return flattened_groups
