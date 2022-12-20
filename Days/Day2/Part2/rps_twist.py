from Days.Day2 import Opponent, RPS
from .needed_outcome import NeededOutcome


class RPSTwist(RPS):
    def __init__(self, games):
        super().__init__(games)
        self.games = games

    @staticmethod
    def needed_sign(opponent, outcome) -> str:
        """
        Determine which sign needs to be played
         using the opponent's sign and the desired outcome.

        :return: A string representation of rock, paper, or scissors.
        """
        outcome_dict = {
            NeededOutcome.WIN: {
                Opponent.ROCK: 'paper',
                Opponent.PAPER: 'scissors',
                Opponent.SCISSORS: 'rock',
            },

            NeededOutcome.DRAW: {
                Opponent.ROCK: 'rock',
                Opponent.PAPER: 'paper',
                Opponent.SCISSORS: 'scissors'
            },

            NeededOutcome.LOSE: {
                Opponent.ROCK: 'scissors',
                Opponent.PAPER: 'rock',
                Opponent.SCISSORS: 'paper'
            }
        }

        return outcome_dict[outcome][opponent]

    def outcome_score(self) -> int:
        """
        Calculate the outcome score
         using the second argument in each tuple of the input text.

        :return: The score of the outcomes as an integer.
        """
        score = 0

        outcome_score = {
            NeededOutcome.WIN: 6,
            NeededOutcome.DRAW: 3,
            NeededOutcome.LOSE: 0,
        }

        for opponent, outcome in self.games:
            score += outcome_score[outcome]

        return score

    def input_score(self) -> int:
        """
        Calculate the score given the opponents input
        and the desired outcome.

        :return: The score of the inputs.
        """

        input_score = {
            'rock': 1,
            'paper': 2,
            'scissors': 3
        }

        score = 0

        for opponent, outcome in self.games:
            player_sign = self.needed_sign(opponent, outcome)
            score += input_score[player_sign]

        return score
