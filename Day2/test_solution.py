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


class TestLogic(unittest.TestCase):
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


class TestSolution(unittest.TestCase):
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

        self.sol_win = Solution(self.wins)
        self.sol_draw = Solution(self.draws)
        self.sol_loss = Solution(self.losses)

    def test_input_score_returns_int(self):
        self.assertEqual(type(self.sol_loss.input_score()), int)

    def test_input_score_returns_correct_score(self):
        self.assertEqual(Solution([('A', 'X')]).input_score(), 1)
        self.assertEqual(Solution([('A', 'Y')]).input_score(), 2)
        self.assertEqual(Solution([('A', 'Z')]).input_score(), 3)

    def test_outcome_score_returns_int(self):
        self.assertEqual(type(self.sol_loss.outcome_score()), int)

    def test_outcome_score_returns_zero_for_losses(self):
        self.assertEqual(self.sol_loss.outcome_score()/len(self.losses), 0)

    def test_outcome_score_returns_three_for_draws(self):
        self.assertEqual(self.sol_draw.outcome_score()/len(self.draws), 3)

    def test_outcome_score_returns_six_for_wins(self):
        self.assertEqual(self.sol_win.outcome_score()/len(self.wins), 6)


if __name__ == '__main__':
    unittest.main()
