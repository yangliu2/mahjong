""" Group tiles together to make sense of it """
from mahjong.tile import Tile
from typing import List, Set
from itertools import combinations
from mahjong.suit import SuitEnum
from dataclasses import dataclass


@dataclass
class Group:
    tiles: List[Tile]

    @staticmethod
    def complete_2_parts(tiles: List[Tile]) -> List[Tile]:
        """ Find the tiles that would complete sets with 2 members """

        # Determine the smaller number
        numbers = [x.number for x in tiles]
        smaller_number = sorted(numbers)[0]

        # for 'bonus' suit
        if (SuitEnum.FLOWERS.value in {x.suit for x in tiles} or
                SuitEnum.SEASONS.value in {x.suit for x in tiles}):
            return []

        # for 'honor' suit
        if (SuitEnum.WINDS.value in [x.suit for x in tiles] or
                SuitEnum.DRAGONS.value in [x.suit for x in tiles]):
            return [Tile(suit=tiles[0].suit,
                         number=smaller_number)]

        # for all other suits
        # Find the difference between all items in the numbers list
        difference = [j - i for i, j in zip(numbers[:-1], numbers[1:])]

        # return empty list if the set were not related at all
        complement_tiles = []
        smaller_number = sorted(numbers)[0]

        # for 2w, 3w format
        if abs(difference[0]) == 1:
            if smaller_number == 1:
                complement_tiles = [Tile(suit=tiles[0].suit,
                                         number=smaller_number + 2)]
            elif smaller_number == 7:
                complement_tiles = [Tile(suit=tiles[0].suit,
                                         number=smaller_number - 1)]
            else:
                complement_tiles = [Tile(suit=tiles[0].suit,
                                         number=smaller_number - 1),
                                    Tile(suit=tiles[0].suit,
                                         number=smaller_number + 2)]
        # for 2w, 4w format
        elif abs(difference[0]) == 2:
            complement_tiles = [Tile(suit=tiles[0].suit,
                                     number=smaller_number + 1)]
        # for 2w, 2w, format
        elif abs(difference[0]) == 0:
            complement_tiles = [Tile(suit=tiles[0].suit,
                                     number=smaller_number)]
        else:
            tiles = [str(x) for x in tiles]
            print(f"Error encountered when trying complete {tiles}")

        return complement_tiles

    def complete_multiple_parts(self,
                                tiles: List[Tile]) -> List[Tile]:
        """Break down the tiles into 2 tile groups, determine the tiles
        need to complete each 2 tile groups, then combine all the tiles for
        the complete set of useful tiles.

        Args:
            tiles (List[Tile]): these tiles will be used to generate complements

        Returns:
            List[Tile]: the complemented tiles
        """

        # Breakdown the tiles into 2 member groups
        two_groups = list(combinations(tiles, 2))

        # For each of the 2 member group, find the complementary tile for each
        complement_tiles = [self.complete_2_parts(list(x))
                            for x in two_groups]

        # Flatten the 2d structure into a single set
        flattened_comp_tiles = {x
                                for groups in complement_tiles
                                for x in groups}

        # Added the original tiles because they are still consider useful pieces
        added_own = flattened_comp_tiles | set(tiles)

        return sorted(added_own)

    def complete_set(self) -> List[Tile]:
        """ Find the tile that would complete the set for the parts """

        complement_tiles = []

        if len(self.tiles) == 2:
            complement_tiles = self.complete_2_parts(tiles=self.tiles)
        # For parts that doesn't work with anything else, return empty
        elif len(self.tiles) == 1:
            return []
        # Return more possibilities with 3 member parts
        elif len(self.tiles) > 2:
            self.complete_multiple_parts(tiles=self.tiles)

        return complement_tiles
