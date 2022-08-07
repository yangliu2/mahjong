import unittest
from mahjong.group import Group
from mahjong.tile import Tile


class TestGroup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        
        # 2w, 3w
        tiles_1 = [Tile('w', 2),
                   Tile('w', 3),
                   Tile('w', 7)]
        cls.group_1 = Group(tiles_1)

        # 1w, 3w
        tiles_2 = [Tile('w', 1),
                   Tile('w', 3)]
        cls.group_2 = Group(tiles_2)
        
        # 2w, 4w
        tiles_3 = [Tile('w', 2),
                   Tile('w', 4)]
        cls.group_3 = Group(tiles_3)
        # 2w, 2w
        tiles_4 = [Tile('w', 2),
                   Tile('w', 2)]
        cls.group_4 = Group(tiles_4)

    def test_complete_2_parts_1(self):
        actual = self.group_1.complete_2_parts()
        expected = [Tile('w', 1),
                    Tile('w', 4)]
        self.assertEqual(actual, expected)

    def test_complete_2_parts_2(self):
        actual = self.group_2.complete_2_parts()
        expected = [Tile('w', 2)]
        self.assertEqual(actual, expected)
        
    def test_complete_2_parts_3(self):
        actual = self.group_3.complete_2_parts()
        expected = [Tile('w', 3)]
        self.assertEqual(actual, expected)
        
    def test_complete_2_parts_4(self):
        actual = self.group_4.complete_2_parts()
        expected = [Tile('w', 2)]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
