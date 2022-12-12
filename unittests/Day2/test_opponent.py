import unittest

from Day2 import Opponent


class TestOpponent(unittest.TestCase):
    def test_rock(self):
        self.assertEqual(Opponent.ROCK, 'A')

    def test_paper(self):
        self.assertEqual(Opponent.PAPER, 'B')

    def test_scissor(self):
        self.assertEqual(Opponent.SCISSORS, 'C')


if __name__ == '__main__':
    unittest.main()
