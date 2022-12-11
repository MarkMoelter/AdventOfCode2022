import unittest

from Day2.part1 import Part1


class TestGameLogic(unittest.TestCase):
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

        self.sol_win = Part1(self.wins)
        self.sol_draw = Part1(self.draws)
        self.sol_loss = Part1(self.losses)

    def test_win_logic(self):
        for opponent, player in self.wins:
            self.assertEqual(self.sol_win.game_logic(opponent, player), 'W')

    def test_draw_logic(self):
        for opponent, player in self.draws:
            self.assertEqual(self.sol_draw.game_logic(opponent, player), 'D')

    def test_loss_logic(self):
        for opponent, player in self.losses:
            self.assertEqual(self.sol_loss.game_logic(opponent, player), 'L')


class TestInputScore(unittest.TestCase):
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

        self.sol_win = Part1(self.wins)
        self.sol_draw = Part1(self.draws)
        self.sol_loss = Part1(self.losses)

    def test_returns_int(self):
        self.assertEqual(type(self.sol_loss.input_score()), int)

    def test_returns_correct_score(self):
        self.assertEqual(Part1([('A', 'X')]).input_score(), 1)
        self.assertEqual(Part1([('A', 'Y')]).input_score(), 2)
        self.assertEqual(Part1([('A', 'Z')]).input_score(), 3)


class TestOutcomeScore(unittest.TestCase):
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

        self.sol_win = Part1(self.wins)
        self.sol_draw = Part1(self.draws)
        self.sol_loss = Part1(self.losses)

    def test_returns_int(self):
        self.assertEqual(type(self.sol_loss.outcome_score()), int)

    def test_returns_zero_for_losses(self):
        self.assertEqual(self.sol_loss.outcome_score() / len(self.losses), 0)

    def test_returns_three_for_draws(self):
        self.assertEqual(self.sol_draw.outcome_score() / len(self.draws), 3)

    def test_returns_six_for_wins(self):
        self.assertEqual(self.sol_win.outcome_score() / len(self.wins), 6)


class TestTotalScore(unittest.TestCase):
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

        self.sol_win = Part1(self.wins)
        self.sol_draw = Part1(self.draws)
        self.sol_loss = Part1(self.losses)

    def test_returns_int(self):
        self.assertEqual(type(self.sol_loss.total_score()), int)

    def test_returns_six_for_losses(self):
        self.assertEqual(self.sol_loss.total_score(), 6)

    def test_returns_fifteen_for_draws(self):
        self.assertEqual(self.sol_draw.total_score(), 15)

    def test_returns_twenty_four_for_wins(self):
        self.assertEqual(self.sol_win.total_score(), 24)


if __name__ == '__main__':
    unittest.main()
