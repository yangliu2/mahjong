""" Make a set of the available tiles, according to the given Rule """
from dataclasses import dataclass, field
from typing import List

from mahjong.tile import Tile
from mahjong.suit import SuitEnum, DragonSuitEnum
from mahjong.rules import Rules


@dataclass
class MahjongSet:
    rules: Rules
    tiles: List[Tile] = field(default_factory=lambda: [])

    def __post_init__(self):

        # Create tiles for each suit
        characters = [Tile(suit=str(SuitEnum.CHARACTERS.value), number=x)
                      for x in range(1, 10)] * 4
        dots = [Tile(suit=str(SuitEnum.DOTS.value), number=x)
                for x in range(1, 10)] * 4
        bamboos = [Tile(suit=str(SuitEnum.BAMBOO.value), number=x)
                   for x in range(1, 10)] * 4
        winds = [Tile(suit=str(SuitEnum.WINDS.value), number=x)
                 for x in range(1, 5)] * 4
        part_dragon = [Tile(suit=str(SuitEnum.DRAGONS.value),
                            number=DragonSuitEnum.RED)] * 4
        dragons = [Tile(suit=str(SuitEnum.DRAGONS.value), number=x)
                   for x in range(1, 4)] * 4
        flowers = [Tile(suit=str(SuitEnum.FLOWERS.value), number=x)
                   for x in range(1, 5)]
        seasons = [Tile(suit=str(SuitEnum.SEASONS.value), number=x)
                   for x in range(1, 5)]

        # Add tiles from each suit
        self.tiles.extend(characters)
        self.tiles.extend(dots)
        self.tiles.extend(bamboos)

        # Often, even if honors are not included, Red Dragon is included just
        #  to make sure there is enough tiles to divide by 4 equal stacks
        if self.rules.have_honors:
            self.tiles.extend(winds)
            self.tiles.extend(dragons)
        else:
            self.tiles.extend(part_dragon)

        # Only a few format include the bonus tiles
        if self.rules.have_bonus:
            self.tiles.extend(flowers)
            self.tiles.extend(seasons)
