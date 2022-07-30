from dataclasses import dataclass

class SuitEnum():
    WAN = 'w'
    BING = 'b'
    TIAO = 't'
    FENG = 'f'
    HUA = 'h'

class FengSuitEnum():
    DONG = 1
    XI = 2
    NAN = 3
    BEI = 4
    ZHONG = 5
    FA = 6
    CAI = 7
    BAN = 8

@dataclass
class Suit:
    name: str