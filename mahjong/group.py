""" Group tiles together to make sense of it """
from mahjong.tile import Tile
from typing import List
from mahjong.suit import SuitEnum
from dataclasses import dataclass


@dataclass
class Group:
    tiles: List[Tile]

    def complete_2_parts(self) -> List[Tile]:
        """ Find the tiles that would complete sets with 2 members """

        # Determine the smaller number
        numbers = [x.number for x in self.tiles]
        smaller_number = sorted(numbers)[0]

        # for 'hua' suit
        if SuitEnum.FLOWERS in [x.suit for x in self.tiles]:
            return []

        # for 'feng' suit
        if SuitEnum.WINDS in [x.suit for x in self.tiles]:
            return [Tile(suit=self.tiles[0].suit,
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
                complement_tiles = [Tile(suit=self.tiles[0].suit,
                                         number=smaller_number + 2)]
            elif smaller_number == 7:
                complement_tiles = [Tile(suit=self.tiles[0].suit,
                                         number=smaller_number - 1)]
            else:
                complement_tiles = [Tile(suit=self.tiles[0].suit,
                                         number=smaller_number - 1),
                                    Tile(suit=self.tiles[0].suit,
                                         number=smaller_number + 2)]
        # for 2w, 4w format
        elif abs(difference[0]) == 2:
            complement_tiles = [Tile(suit=self.tiles[0].suit,
                                     number=smaller_number + 1)]
        # for 2w, 2w, format
        elif abs(difference[0]) == 0:
            complement_tiles = [Tile(suit=self.tiles[0].suit,
                                     number=smaller_number)]
        else:
            tiles = [str(x) for x in self.tiles]
            print(f"Error encountered when trying complete {tiles}")

        return complement_tiles

    def complete_set(self) -> List[Tile]:
        """ Find the tile that would complete the set for the parts """

        complement_tiles = []

        if len(self.tiles) == 2:
            complement_tiles = self.complete_2_parts()
        # For parts that doesn't work with anything else, return empty
        elif len(self.tiles) == 1:
            return []
        # Return more possibilities with 3 member parts
        elif len(self.tiles) > 2:
            # TODO: What find the complements for longer than 2 groups 
            pass

        return complement_tiles
