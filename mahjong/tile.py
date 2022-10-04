""" Basic unit in Mahjong """
from mahjong.suit import Suit, SuitEnum
from dataclasses import dataclass, field


@dataclass(order=True, unsafe_hash=True)
class Tile:
    suit: str = field(compare=False)
    number: int = field(compare=True)

    @staticmethod
    def increment_hex(unicode_str: str,
                      increment: int = 1,
                      encoding: str = 'utf8') -> str:
        """Increase the hex str by 1 to get the next unicode displaying tile

        Args:
            unicode_str (str): the tile unicode 
            increment (int, optional): how many increment to the hex str. 
            Defaults to 1.
            encoding (str, optional): displaying encoding. Defaults to 'utf8'.

        Returns:
            str: the unicode string that can be displayed in cli
        """
        hex_str = unicode_str.encode(encoding)
        hex_str_int = int.from_bytes(hex_str, 'big')
        incresed_hex_str_int = hex_str_int + increment
        hex_length = len(hex_str)
        increased_hex_str = incresed_hex_str_int.to_bytes(hex_length, 'big')
        increased_str = increased_hex_str.decode(encoding)

        return increased_str

    @staticmethod
    def increment_str(unicode_str: str,
                      increment: int = 1) -> str:
        """Increase the str by increment number to get the next displaying tile

        Args:
            unicode_str (str): tile unicode
            increment (int, optional): how many increment to increase. 
            Defaults to 1.

        Returns:
            str: the unicode string that can be displayed in cli
        """
        return chr(ord(unicode_str) + increment)
