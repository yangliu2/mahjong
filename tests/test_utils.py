import unittest
from mahjong.tile import Tile
from mahjong.utils import find_chow_tiles, find_friends


class TestUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def test_find_friends_1w(self):
        tile = Tile('w', 1)
        actual = find_friends(tile=tile)

        expected = [Tile('w', 1),
                    Tile('w', 2),
                    Tile('w', 3)]
        self.assertEqual(actual, expected)

    def test_find_friends_9w(self):
        tile = Tile('w', 9)
        actual = find_friends(tile=tile)

        expected = [Tile('w', 7),
                    Tile('w', 8),
                    Tile('w', 9)]
        self.assertEqual(actual, expected)

    def test_find_friends_2w(self):
        tile = Tile('w', 2)
        actual = find_friends(tile=tile)

        expected = [Tile('w', 1),
                    Tile('w', 2),
                    Tile('w', 3),
                    Tile('w', 4)]
        self.assertEqual(actual, expected)

    def test_find_friends_2b(self):
        tile = Tile('b', 2)
        actual = find_friends(tile=tile)

        expected = [Tile('b', 1),
                    Tile('b', 2),
                    Tile('b', 3),
                    Tile('b', 4)]
        self.assertEqual(actual, expected)

    def test_find_friends_8w(self):
        tile = Tile('w', 8)
        actual = find_friends(tile=tile)

        expected = [Tile('w', 6),
                    Tile('w', 7),
                    Tile('w', 8),
                    Tile('w', 9)]
        self.assertEqual(actual, expected)

    def test_find_friends_4w(self):
        tile = Tile('w', 4)
        actual = find_friends(tile=tile)

        expected = [Tile('w', 2),
                    Tile('w', 3),
                    Tile('w', 4),
                    Tile('w', 5),
                    Tile('w', 6)]
        self.assertEqual(actual, expected)

    def test_find_chow_tile_1(self):
        tile = Tile(suit='w', number=1)
        actual = find_chow_tiles(tile=tile)
        expected = [Tile(suit='w', number=1),
                    Tile(suit='w', number=2),
                    Tile(suit='w', number=3)]
        self.assertEqual(actual, expected)

    def test_find_chow_tile_2(self):
        tile = Tile(suit='w', number=9)
        actual = find_chow_tiles(tile=tile)
        expected = [Tile(suit='w', number=7),
                    Tile(suit='w', number=8),
                    Tile(suit='w', number=9)]
        self.assertEqual(actual, expected)

    def test_find_chow_tile_3(self):
        tile = Tile(suit='w', number=8)
        actual = find_chow_tiles(tile=tile)
        expected = [Tile(suit='w', number=7),
                    Tile(suit='w', number=8),
                    Tile(suit='w', number=9)]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
