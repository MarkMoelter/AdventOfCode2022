import unittest

from Day2.part1 import Player


class TestPlayer(unittest.TestCase):
    def test_rock(self):
        self.assertEqual(Player.ROCK, 'X')

    def test_paper(self):
        self.assertEqual(Player.PAPER, 'Y')

    def test_scissor(self):
        self.assertEqual(Player.SCISSORS, 'Z')


if __name__ == '__main__':
    unittest.main()
