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

    def test_find_friends_1w(self):
        tile = Tile('w', 1)
        actual = GroupMaker.find_friends(tile=tile)

        expected = [Tile('w', 1),
                    Tile('w', 2),
                    Tile('w', 3)]
        self.assertEqual(actual, expected)

    def test_find_friends_9w(self):
        tile = Tile('w', 9)
        actual = GroupMaker.find_friends(tile=tile)

        expected = [Tile('w', 7),
                    Tile('w', 8),
                    Tile('w', 9)]
        self.assertEqual(actual, expected)

    def test_find_friends_2w(self):
        tile = Tile('w', 2)
        actual = GroupMaker.find_friends(tile=tile)

        expected = [Tile('w', 1),
                    Tile('w', 2),
                    Tile('w', 3),
                    Tile('w', 4)]
        self.assertEqual(actual, expected)

    def test_find_friends_2b(self):
        tile = Tile('b', 2)
        actual = GroupMaker.find_friends(tile=tile)

        expected = [Tile('b', 1),
                    Tile('b', 2),
                    Tile('b', 3),
                    Tile('b', 4)]
        self.assertEqual(actual, expected)

    def test_find_friends_8w(self):
        tile = Tile('w', 8)
        actual = GroupMaker.find_friends(tile=tile)

        expected = [Tile('w', 6),
                    Tile('w', 7),
                    Tile('w', 8),
                    Tile('w', 9)]
        self.assertEqual(actual, expected)

    def test_find_friends_4w(self):
        tile = Tile('w', 4)
        actual = GroupMaker.find_friends(tile=tile)

        expected = [Tile('w', 2),
                    Tile('w', 3),
                    Tile('w', 4),
                    Tile('w', 5),
                    Tile('w', 6)]
        self.assertEqual(actual, expected)

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

    def test_make_groups(self):
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
        
    def test_find_chow_tile_1(self):
        tile = Tile(suit='w', number=1)
        actual = GroupMaker.find_chow_tiles(tile=tile)
        expected = [Tile(suit='w', number=1),
                    Tile(suit='w', number=2),
                    Tile(suit='w', number=3)]
        self.assertEqual(actual, expected)
        
    def test_find_chow_tile_2(self):
        tile = Tile(suit='w', number=9)
        actual = GroupMaker.find_chow_tiles(tile=tile)
        expected = [Tile(suit='w', number=7),
                    Tile(suit='w', number=8),
                    Tile(suit='w', number=9)]
        self.assertEqual(actual, expected)
        
    def test_find_chow_tile_3(self):
        tile = Tile(suit='w', number=8)
        actual = GroupMaker.find_chow_tiles(tile=tile)
        expected = [Tile(suit='w', number=7),
                    Tile(suit='w', number=8),
                    Tile(suit='w', number=9)]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
