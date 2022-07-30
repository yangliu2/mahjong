from dataclasses import dataclass

class SuitEnum():
    WAN = 'w'
    BING = 'b'
    TIAO = 't'
    FENG = 'f'
    HUA = 'h'

class FengSuitEnum():
    DONG = 1
    NAN = 2
    XI = 3
    BEI = 4
    ZHONG = 5
    FA = 6
    BAI = 7

@dataclass
class Suit:
    name: str