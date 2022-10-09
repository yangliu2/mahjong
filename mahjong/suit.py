""" Suits of Mahjong """
from dataclasses import dataclass
from enum import Enum, IntEnum


class SuitEnum(Enum):
    CHARACTERS = 'w'
    DOTS = 'b'
    BAMBOO = 't'
    WINDS = 'f'
    DRAGONS = 'd'
    FLOWERS = 'h'
    SEASONS = 'j'


class FlowerSuitEnum(IntEnum):
    PLUM_BLOSSOM = 1
    ORCHID = 2
    CHRYSANTHEMUM = 3
    BAMBOO = 4


class SeasonSuitEnum(IntEnum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4


class WindSuitEnum(IntEnum):
    EAST = 1
    SOUTH = 2
    WEST = 3
    NORTH = 4


class DragonSuitEnum(IntEnum):
    RED = 1
    Green = 2
    White = 3


@dataclass(unsafe_hash=True)
class Suit:
    name: str

    def __post_init__(self):
        self.name = SuitEnum(self.name).name
