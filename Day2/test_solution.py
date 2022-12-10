import unittest

from main import Opponent, NeededOutcome, Player, Part1, Part2, rps_logic


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


class TestPart1(unittest.TestCase):
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

    def test_input_score_returns_int(self):
        self.assertEqual(type(self.sol_loss.input_score()), int)

    def test_input_score_returns_correct_score(self):
        self.assertEqual(Part1([('A', 'X')]).input_score(), 1)
        self.assertEqual(Part1([('A', 'Y')]).input_score(), 2)
        self.assertEqual(Part1([('A', 'Z')]).input_score(), 3)

    def test_outcome_score_returns_int(self):
        self.assertEqual(type(self.sol_loss.outcome_score()), int)

    def test_outcome_score_returns_zero_for_losses(self):
        self.assertEqual(self.sol_loss.outcome_score() / len(self.losses), 0)

    def test_outcome_score_returns_three_for_draws(self):
        self.assertEqual(self.sol_draw.outcome_score() / len(self.draws), 3)

    def test_outcome_score_returns_six_for_wins(self):
        self.assertEqual(self.sol_win.outcome_score() / len(self.wins), 6)


class TestNeededOutcome(unittest.TestCase):
    def test_returns_string(self):
        self.assertEqual(type(Part2([('A', 'X')]).needed_sign()), str)

    def test_returns_rock(self):
        rock_needed = [(Opponent.ROCK, NeededOutcome.DRAW)]
        self.assertEqual(Part2(rock_needed).needed_sign(), 'rock')

    def test_returns_paper(self):
        paper_needed = [(Opponent.ROCK, NeededOutcome.WIN)]
        self.assertEqual(Part2(paper_needed).needed_sign(), 'paper')

    def test_returns_scissors(self):
        scissors_needed = [(Opponent.ROCK, NeededOutcome.LOSE)]
        self.assertEqual(Part2(scissors_needed).needed_sign(), 'scissors')


if __name__ == '__main__':
    unittest.main()
