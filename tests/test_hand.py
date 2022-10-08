import unittest
from mahjong.hand import Hand
from mahjong.tile import Tile
from mahjong.rules import Rules
from mahjong.group import Group
from mahjong.suit import SuitEnum


class TestHand(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw_tiles = '1w2w3w4b'
        cls.invalid_hand = Hand(raw_tiles=raw_tiles)

        raw_tiles = '1w1w1w4w5w2t3t3t6f6f5f5f4b'
        cls.valid_hand = Hand(raw_tiles=raw_tiles)

        cls.rules = Rules()

    def test_is_valid_hand_true(self):
        actual = self.invalid_hand.is_valid_hand(rules=self.rules)
        expected = False
        self.assertEqual(actual, expected)

    def test_is_valid_hand_false(self):
        actual = self.valid_hand.is_valid_hand(rules=self.rules)
        expected = True
        self.assertEqual(actual, expected)

    def test_group_by_suit(self):
        actual = Hand.group_by_suit(self.invalid_hand.tiles)
        expected = {'w': [Tile('w', 1),
                          Tile('w', 2),
                          Tile('w', 3)],
                    'b': [Tile('b', 4)]}
        self.assertEqual(actual, expected)

    def test_is_breakdown_groups(self):
        actual = self.invalid_hand.breakdown_groups()
        first_group = [Tile('w', 1),
                       Tile('w', 2),
                       Tile('w', 3)]
        second_group = [Tile('b', 4)]
        expected = [Group(first_group),
                    Group(second_group)]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
