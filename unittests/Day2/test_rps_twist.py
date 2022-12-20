import unittest

from Days.Day2 import NeededOutcome, RPSTwist, Opponent


class TestNeededSign(unittest.TestCase):
    def test_returns_string(self):
        self.assertEqual(type(RPSTwist([('A', 'X')]).needed_sign('A', 'X')), str)

    def test_returns_rock(self):
        rock_needed = [(Opponent.ROCK, NeededOutcome.DRAW)]
        self.assertEqual(RPSTwist(rock_needed).needed_sign(*rock_needed[0]), 'rock')

    def test_returns_paper(self):
        paper_needed = [(Opponent.ROCK, NeededOutcome.WIN)]
        self.assertEqual(RPSTwist(paper_needed).needed_sign(*paper_needed[0]), 'paper')

    def test_returns_scissors(self):
        scissors_needed = [(Opponent.ROCK, NeededOutcome.LOSE)]
        self.assertEqual(RPSTwist(scissors_needed).needed_sign(*scissors_needed[0]), 'scissors')


class TestOutcomeScore(unittest.TestCase):
    def setUp(self) -> None:
        self.losses = [
            (Opponent.ROCK, NeededOutcome.LOSE),
            (Opponent.PAPER, NeededOutcome.LOSE),
            (Opponent.SCISSORS, NeededOutcome.LOSE),
        ]

        self.draws = [
            (Opponent.ROCK, NeededOutcome.DRAW),
            (Opponent.PAPER, NeededOutcome.DRAW),
            (Opponent.SCISSORS, NeededOutcome.DRAW),
        ]

        self.wins = [
            (Opponent.ROCK, NeededOutcome.WIN),
            (Opponent.PAPER, NeededOutcome.WIN),
            (Opponent.SCISSORS, NeededOutcome.WIN),
        ]

        self.part2_win = RPSTwist(self.wins)
        self.part2_draw = RPSTwist(self.draws)
        self.part2_loss = RPSTwist(self.losses)

    def test_returns_int(self):
        self.assertEqual(
            type(self.part2_win.outcome_score()),
            int
        )

    def test_returns_zero_for_losses(self):
        self.assertEqual(
            self.part2_loss.outcome_score() / len(self.losses),
            0
        )

    def test_returns_three_for_draws(self):
        self.assertEqual(
            self.part2_draw.outcome_score() / len(self.draws),
            3
        )

    def test_returns_six_for_wins(self):
        self.assertEqual(
            self.part2_win.outcome_score() / len(self.wins),
            6
        )


class TestInputScore(unittest.TestCase):
    def setUp(self) -> None:
        self.losses = [
            (Opponent.ROCK, NeededOutcome.LOSE),
            (Opponent.PAPER, NeededOutcome.LOSE),
            (Opponent.SCISSORS, NeededOutcome.LOSE),
        ]

        self.draws = [
            (Opponent.ROCK, NeededOutcome.DRAW),
            (Opponent.PAPER, NeededOutcome.DRAW),
            (Opponent.SCISSORS, NeededOutcome.DRAW),
        ]

        self.wins = [
            (Opponent.ROCK, NeededOutcome.WIN),
            (Opponent.PAPER, NeededOutcome.WIN),
            (Opponent.SCISSORS, NeededOutcome.WIN),
        ]

        self.part2_win = RPSTwist(self.wins)
        self.part2_draw = RPSTwist(self.draws)
        self.part2_loss = RPSTwist(self.losses)

    def test_returns_int(self):
        self.assertEqual(
            type(self.part2_win.input_score()),
            int
        )

    def test_returns_six_for_one_of_each(self):
        self.assertEqual(
            self.part2_draw.input_score(),
            6
        )

    def test_returns_one_for_rock(self):
        self.assertEqual(
            RPSTwist([(Opponent.ROCK, NeededOutcome.DRAW)]).input_score(),
            1
        )

    def test_returns_two_for_paper(self):
        self.assertEqual(
            RPSTwist([(Opponent.PAPER, NeededOutcome.DRAW)]).input_score(),
            2
        )

    def test_returns_three_for_scissors(self):
        self.assertEqual(
            RPSTwist([(Opponent.SCISSORS, NeededOutcome.DRAW)]).input_score(),
            3
        )


if __name__ == '__main__':
    unittest.main()
