""" Basic unit in Mahjong """
from mahjong.suit import SuitEnum
from dataclasses import dataclass, field


@dataclass(order=True, unsafe_hash=True)
class Tile:
    """This is a the most basic unit in Mahjong

    :param suit: str representation of the suit type
    :type suit: str
    :param number: number of the tile
    :type number: int
    """
    suit: str = field(compare=False)
    number: int = field(compare=True)

    def __post_init__(self):
        """ Use SuitEnum values as a shorthand to indicate tile type"""
        self.suit = str(SuitEnum(self.suit).value)

    @staticmethod
    def increment_hex(unicode_str: str,
                      increment: int = 1,
                      encoding: str = 'utf8') -> str:
        """Increase the hex str by 1 to get the next unicode displaying tile

        :param unicode_str: the tile unicode
        :type unicode_str: str
        :param increment: how many increment to the hex str, defaults to 1
        :type increment: int, optional
        :param encoding: displaying encoding, defaults to 'utf8'
        :type encoding: str, optional
        :return: the unicode string that can be displayed in cli
        :rtype: str
        """

        hex_str = unicode_str.encode(encoding)
        hex_str_int = int.from_bytes(hex_str, 'big')
        increased_hex_str_int = hex_str_int + increment
        hex_length = len(hex_str)
        increased_hex_str = increased_hex_str_int.to_bytes(hex_length, 'big')
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
