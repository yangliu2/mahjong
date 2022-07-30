from mahjong.group import Group
from mahjong.tile import Tile
from mahjong.suit import SuitEnum
from typing import Dict, List
from dataclasses import dataclass


@dataclass
class GroupMaker:
    group_dict: Dict[str, List[Tile]]

    @staticmethod
    def find_friends(tile: Tile) -> List[Tile]:
        """Find the friends of a tile considering whether it's on the edge. 
        Friends are defined as tiles that can be useful when combined with the
        current tile. e.g. for 1w, 2w and 3w are friends. For 4w, all of 
        [2w, 3w, 4w, 5w, 6w] are friends.

        Args:
            tile (Tile): the tile that we will find friends for

        Returns:
            List[Tile]: List of friendly tiles
        """
        if tile.suit == SuitEnum.HUA or tile.suit == SuitEnum.FENG:
            return []
        elif tile.suit in [SuitEnum.WAN, SuitEnum.BING, SuitEnum.TIAO]:
            if tile.number == 1:
                return [Tile(suit=tile.suit, number=1),
                        Tile(suit=tile.suit, number=2),
                        Tile(suit=tile.suit, number=3)]
            elif tile.number == 9:
                return [Tile(suit=tile.suit, number=7),
                        Tile(suit=tile.suit, number=8),
                        Tile(suit=tile.suit, number=9)]
            elif tile.number == 2:
                return [Tile(suit=tile.suit, number=1),
                        Tile(suit=tile.suit, number=2),
                        Tile(suit=tile.suit, number=3),
                        Tile(suit=tile.suit, number=4)]
            elif tile.number == 8:
                return [Tile(suit=tile.suit, number=6),
                        Tile(suit=tile.suit, number=7),
                        Tile(suit=tile.suit, number=8),
                        Tile(suit=tile.suit, number=9)]
            else:
                return [Tile(suit=tile.suit, number=tile.number-2),
                        Tile(suit=tile.suit, number=tile.number-1),
                        Tile(suit=tile.suit, number=tile.number),
                        Tile(suit=tile.suit, number=tile.number+1),
                        Tile(suit=tile.suit, number=tile.number+2)]

    def group_suit(self,
                   tiles: List[Tile]) -> List[Group]:
        """ Group the tiles in hand into Groups that can be used to find what
        are the possible tiles that will be good to draw. Maximizing the number
        of useful tiles will help the player win faster. Tile that 
        doesn't group with other tiles will be put on it's own group. 

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
            to_be_added = []
            to_be_added.append(first_tile)
            sorted_tiles.pop(0)

            while sorted_tiles:
                first_tile_friends = self.find_friends(first_tile)

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