from typing import List
from mahjong.tile import Tile
from mahjong.suit import SuitEnum


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
    if tile.suit in [SuitEnum.FLOWERS.value,
                     SuitEnum.SEASONS.value]:
        return []
    elif tile.suit in [SuitEnum.WINDS.value,
                       SuitEnum.DRAGONS.value]:
        return [Tile(suit=tile.suit, number=tile.number)]
    elif tile.suit in [SuitEnum.CHARACTERS.value,
                       SuitEnum.DOTS.value,
                       SuitEnum.BAMBOO.value]:
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
            return [Tile(suit=tile.suit, number=tile.number - 2),
                    Tile(suit=tile.suit, number=tile.number - 1),
                    Tile(suit=tile.suit, number=tile.number),
                    Tile(suit=tile.suit, number=tile.number + 1),
                    Tile(suit=tile.suit, number=tile.number + 2)]


def find_chow_tiles(tile: Tile) -> List[Tile]:
    """Find the tiles for the next chow set, starting from the current
    tile. If the tile is more than 7, then return 7, 8, 9

    Args:
        tile (Tile): given tile for the next chow set

    Returns:
        List[Tile]: set of tiles for chow
    """
    if tile.suit in [SuitEnum.FLOWERS.value,
                     SuitEnum.WINDS.value,
                     SuitEnum.DRAGONS.value,
                     SuitEnum.SEASONS.value]:
        return []
    elif tile.suit in [SuitEnum.CHARACTERS.value,
                       SuitEnum.DOTS.value,
                       SuitEnum.BAMBOO.value]:
        if tile.number < 8:
            return [Tile(suit=tile.suit, number=tile.number),
                    Tile(suit=tile.suit, number=tile.number + 1),
                    Tile(suit=tile.suit, number=tile.number + 2)]
        elif tile.number >= 8:
            return [Tile(suit=tile.suit, number=7),
                    Tile(suit=tile.suit, number=8),
                    Tile(suit=tile.suit, number=9)]
