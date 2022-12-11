import unittest

from Day2.part1 import Opponent
from Day2.part2 import NeededOutcome, Part2


class TestNeededSign(unittest.TestCase):
    def test_returns_string(self):
        self.assertEqual(type(Part2([('A', 'X')]).needed_sign('A', 'X')), str)

    def test_returns_rock(self):
        rock_needed = [(Opponent.ROCK, NeededOutcome.DRAW)]
        self.assertEqual(Part2(rock_needed).needed_sign(*rock_needed[0]), 'rock')

    def test_returns_paper(self):
        paper_needed = [(Opponent.ROCK, NeededOutcome.WIN)]
        self.assertEqual(Part2(paper_needed).needed_sign(*paper_needed[0]), 'paper')

    def test_returns_scissors(self):
        scissors_needed = [(Opponent.ROCK, NeededOutcome.LOSE)]
        self.assertEqual(Part2(scissors_needed).needed_sign(*scissors_needed[0]), 'scissors')


if __name__ == '__main__':
    unittest.main()
