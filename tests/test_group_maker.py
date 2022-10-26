import unittest
from mahjong.tile import Tile
from mahjong.group import Group
from mahjong.group_maker import GroupMaker


class TestGroupMaker(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        group_dict = {'w': [Tile('w', 9),
                            Tile('w', 9),
                            Tile('w', 3),
                            Tile('w', 5),
                            Tile('w', 7)],
                      't': [Tile('t', 2),
                            Tile('t', 2),
                            Tile('t', 3),
                            Tile('t', 7),
                            Tile('t', 9)],
                      'b': [Tile('b', 4)]}
        cls.group_maker = GroupMaker(group_dict=group_dict)

        # For winds
        group_dict_2 = {'f': [Tile('f', 1),
                              Tile('f', 2)]}
        cls.group_maker_2 = GroupMaker(group_dict=group_dict_2)

    def test_group_suit_1(self):
        tiles = [Tile('w', 9),
                 Tile('w', 9),
                 Tile('w', 3),
                 Tile('w', 5),
                 Tile('w', 7)]
        actual = self.group_maker.group_suit(tiles=tiles)
        expected = [Group([Tile('w', 3),
                           Tile('w', 5)]),
                    Group([Tile('w', 7),
                           Tile('w', 9),
                           Tile('w', 9)])]

        self.assertEqual(actual, expected)

    def test_group_suit_2(self):
        tiles = [Tile('t', 4)]
        actual = self.group_maker.group_suit(tiles=tiles)
        expected = [Group([Tile('t', 4)])]

        self.assertEqual(actual, expected)

    def test_group_suit_3(self):
        tiles = [Tile('b', 2),
                 Tile('b', 2),
                 Tile('b', 3),
                 Tile('b', 7),
                 Tile('b', 9)]
        actual = self.group_maker.group_suit(tiles=tiles)
        expected = [Group([Tile('b', 2),
                           Tile('b', 2),
                           Tile('b', 3)]),
                    Group([Tile('b', 7),
                           Tile('b', 9)])]

        self.assertEqual(actual, expected)

    def test_group_suit_4(self):
        tiles = [Tile('b', 1),
                 Tile('b', 2),
                 Tile('b', 3),
                 Tile('b', 7),
                 Tile('b', 9)]
        actual = self.group_maker.group_suit(tiles=tiles)
        expected = [Group([Tile('b', 1),
                           Tile('b', 2),
                           Tile('b', 3)]),
                    Group([Tile('b', 7),
                           Tile('b', 9)])]

        self.assertEqual(actual, expected)

    def test_group_suit_5(self):
        tiles = [Tile('b', 1),
                 Tile('b', 2),
                 Tile('b', 3),
                 Tile('b', 3)]
        actual = self.group_maker.group_suit(tiles=tiles)
        expected = [Group([Tile('b', 1),
                           Tile('b', 2),
                           Tile('b', 3)]),
                    Group([Tile('b', 3)])]

        self.assertEqual(actual, expected)

    def test_group_suit_6(self):
        tiles = [Tile('b', 2),
                 Tile('b', 2),
                 Tile('b', 2),
                 Tile('b', 3)]
        actual = self.group_maker.group_suit(tiles=tiles)
        expected = [Group([Tile('b', 2),
                           Tile('b', 2),
                           Tile('b', 2)]),
                    Group([Tile('b', 3)])]

        self.assertEqual(actual, expected)

    def test_group_suit_7(self):
        tiles = [Tile('f', 1)]
        actual = self.group_maker.group_suit(tiles=tiles)
        expected = [Group([Tile('f', 1)])]

        self.assertEqual(actual, expected)

    def test_make_groups_1(self):
        actual = self.group_maker.make_groups()
        expected = [Group([Tile('w', 3),
                           Tile('w', 5)]),
                    Group([Tile('w', 7),
                           Tile('w', 9),
                           Tile('w', 9)]),
                    Group([Tile('b', 2),
                           Tile('b', 2),
                           Tile('b', 3)]),
                    Group([Tile('b', 7),
                           Tile('b', 9)]),
                    Group([Tile('t', 4)])]
        self.assertEqual(actual, expected)

    def test_make_groups_2(self):
        actual = self.group_maker_2.make_groups()

        expected = [Group([Tile('f', 1)]),
                    Group([Tile('f', 2)])]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
