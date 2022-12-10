import unittest

from main import Opponent, Player, Solution, rps_logic


class TestOpponent(unittest.TestCase):
    def test_rock(self):
        self.assertEqual(Opponent.ROCK, 'A')

    def test_paper(self):
        self.assertEqual(Opponent.PAPER, 'B')

    def test_scissor(self):
        self.assertEqual(Opponent.SCISSORS, 'C')


class TestPlayer(unittest.TestCase):
    def test_rock(self):
        self.assertEqual(Player.ROCK, 'X')

    def test_paper(self):
        self.assertEqual(Player.PAPER, 'Y')

    def test_scissor(self):
        self.assertEqual(Player.SCISSORS, 'Z')


class TestSolutionLogic(unittest.TestCase):
    def setUp(self) -> None:
        self.draws = [
            ('A', 'X'), ('B', 'Y'), ('C', 'Z')
        ]

        self.losses = [
            ('A', 'Z'), ('B', 'X'), ('C', 'Y')
        ]

        self.wins = [
            ('A', 'Y'), ('B', 'Z'), ('C', 'X')
        ]

    def test_win_logic(self):
        for opponent, player in self.wins:
            self.assertEqual(rps_logic(opponent, player), 'W')

    def test_draw_logic(self):
        for opponent, player in self.draws:
            self.assertEqual(rps_logic(opponent, player), 'D')

    def test_loss_logic(self):
        for opponent, player in self.losses:
            self.assertEqual(rps_logic(opponent, player), 'L')


if __name__ == '__main__':
    unittest.main()
