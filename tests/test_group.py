import unittest
from mahjong.group import Group
from mahjong.tile import Tile


class TestGroup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 2w, 3w
        cls.tiles_1 = [Tile('w', 2),
                       Tile('w', 3),
                       Tile('w', 7)]

        # 1w, 3w
        cls.tiles_2 = [Tile('w', 1),
                       Tile('w', 3)]

        # 2w, 4w
        cls.tiles_3 = [Tile('w', 2),
                       Tile('w', 4)]

        # 2w, 2w
        cls.tiles_4 = [Tile('w', 2),
                       Tile('w', 2)]

        # 2w, 2w, 3w
        tiles_5 = [Tile('w', 2),
                   Tile('w', 2),
                   Tile('w', 3)]
        cls.group_1 = Group(tiles_5)

        # 1w, 3w, 5w
        tiles_6 = [Tile('w', 1),
                   Tile('w', 3),
                   Tile('w', 5)]
        cls.group_2 = Group(tiles_6)

    def test_complete_2_parts_1(self):
        actual = self.group_1.complete_2_parts(self.tiles_1)
        expected = [Tile('w', 1),
                    Tile('w', 4)]
        self.assertEqual(actual, expected)

    def test_complete_2_parts_2(self):
        actual = self.group_1.complete_2_parts(self.tiles_2)
        expected = [Tile('w', 2)]
        self.assertEqual(actual, expected)

    def test_complete_2_parts_3(self):
        actual = self.group_1.complete_2_parts(self.tiles_3)
        expected = [Tile('w', 3)]
        self.assertEqual(actual, expected)

    def test_complete_2_parts_4(self):
        actual = self.group_1.complete_2_parts(self.tiles_4)
        expected = [Tile('w', 2)]
        self.assertEqual(actual, expected)
        
    def test_complete_3_parts_1(self):
        tiles = self.group_2.tiles
        actual = self.group_2.complete_3_parts(tiles=tiles)
        expected = [Tile('w', 2),
                    Tile('w', 4)]
        self.assertEqual(actual, expected)
        
    def test_complete_3_parts_2(self):
        tiles = self.group_1.tiles
        actual = self.group_1.complete_3_parts(tiles=tiles)
        expected = [Tile('w', 1),
                    Tile('w', 2),
                    Tile('w', 4)]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
