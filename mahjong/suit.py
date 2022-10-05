""" Suits of Mahjong """
from dataclasses import dataclass
from enum import Enum


class SuitEnum(Enum):
    CHARACTERS = 'w'
    DOTS = 'b'
    BAMBOO = 't'
    WINDS = 'f'
    DRAGONS = 'd'
    FLOWERS = 'h'
    SEASONS = 'j'


class FlowerSuitEnum(Enum):
    PLUM_BLOSSOM = 1
    ORCHID = 2
    CHRYSANTHEMUM = 3
    BAMBOO = 4


class SeasonSuitEnum(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4


class WindSuitEnum(Enum):
    EAST = 1
    SOUTH = 2
    WEST = 3
    NORTH = 4


class DragonSuitEnum(Enum):
    RED = 1
    Green = 2
    White = 3


@dataclass
class Suit:
    name: str
