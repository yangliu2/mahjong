import unittest
from mahjong.mahjong_set import MahjongSet
from mahjong.rules import Rules


class TestHand(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        full_set_rule = Rules(have_bonus=True, have_honors=True)
        cls.full_set = MahjongSet(rules=full_set_rule)

        suit_only_rule = Rules(have_bonus=False, have_honors=False)
        cls.suit_only_set = MahjongSet(rules=suit_only_rule)

    def test_post_init_1(self):
        actual = len(self.full_set.tiles)
        expected = 144
        self.assertEqual(actual, expected)

    def test_post_init_2(self):
        actual = len(self.suit_only_set.tiles)
        expected = 112
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
