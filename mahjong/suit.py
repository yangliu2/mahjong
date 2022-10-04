""" Suits of Mahjong """
from dataclasses import dataclass


class SuitEnum():
    CHARACTERS = 'w'
    DOTS = 'b'
    BAMBOO = 't'
    WINDS = 'f'
    FLOWERS = 'h'
    SEASONS = 'j'


class FlowerSuitEnum():
    PLUM_BLOSSOM = 1
    ORCHID = 2
    CHRYSANTHEMUM = 3
    BAMBOO = 4


class DragonSuitEnum():
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4


class WindSuitEnum():
    EAST = 1
    SOUTH = 2
    WEST = 3
    NORTH = 4


class DragonSuitEnum():
    RED = 1
    Green = 2
    White = 3


@dataclass
class Suit:
    name: str
