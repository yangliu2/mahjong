import unittest
from mahjong.tile_displayer import TileDisplayer


class TestTileDisplayer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def test_increment_hex(self):
        f1 = '🀀'
        actual = TileDisplayer.increment_hex(unicode_str=f1,
                                             increment=8)
        expected = '🀈'
        self.assertEqual(actual, expected)

    def test_increment_str(self):
        f1 = '🀀'
        actual = TileDisplayer.increment_str(unicode_str=f1,
                                             increment=8)
        expected = '🀈'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
