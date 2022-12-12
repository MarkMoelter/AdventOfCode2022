import unittest

from Day2 import RPS, Outcome


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

        self.part1_win = RPS(self.wins)
        self.part1_draw = RPS(self.draws)
        self.part1_loss = RPS(self.losses)

    def test_returns_outcome_enum(self):
        for opponent, player in self.draws:
            self.assertEqual(
                type(self.part1_draw.game_logic(opponent, player)),
                Outcome
            )

    def test_win_logic(self):
        for opponent, player in self.wins:
            self.assertEqual(
                self.part1_win.game_logic(opponent, player),
                Outcome.WIN
            )

    def test_draw_logic(self):
        for opponent, player in self.draws:
            self.assertEqual(
                self.part1_draw.game_logic(opponent, player),
                Outcome.DRAW
            )

    def test_loss_logic(self):
        for opponent, player in self.losses:
            self.assertEqual(
                self.part1_loss.game_logic(opponent, player),
                Outcome.LOSS
            )


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

        self.sol_win = RPS(self.wins)
        self.sol_draw = RPS(self.draws)
        self.sol_loss = RPS(self.losses)

    def test_returns_int(self):
        self.assertEqual(type(self.sol_loss.input_score()), int)

    def test_returns_correct_score(self):
        self.assertEqual(RPS([('A', 'X')]).input_score(), 1)
        self.assertEqual(RPS([('A', 'Y')]).input_score(), 2)
        self.assertEqual(RPS([('A', 'Z')]).input_score(), 3)


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

        self.sol_win = RPS(self.wins)
        self.sol_draw = RPS(self.draws)
        self.sol_loss = RPS(self.losses)

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

        self.sol_win = RPS(self.wins)
        self.sol_draw = RPS(self.draws)
        self.sol_loss = RPS(self.losses)

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
