from enum import Enum

class SuitEnum:
    WAN = 'w'
    BING = 'b'
    TIAO = 't'
    FENG = 'f'
    HUA = 'h'

class Suit:
    def __init__(self, 
                 name: str) -> None:
        self.name = name