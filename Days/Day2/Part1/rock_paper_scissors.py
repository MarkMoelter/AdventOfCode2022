from .opponent import Opponent
from .outcome import Outcome
from .player import Player


class RPS:
    def __init__(self, games: list[tuple[str, str]]):
        self.games = games

    @staticmethod
    def game_logic(opponent, player) -> Outcome:
        """
        Logic for rock, paper, scissors game.

        :return: An Outcome enum of the outcome of the game.
        """
        outcome_dict = {
            Opponent.ROCK: {
                Player.ROCK: Outcome.DRAW,
                Player.PAPER: Outcome.WIN,
                Player.SCISSORS: Outcome.LOSS
            },

            Opponent.PAPER: {
                Player.ROCK: Outcome.LOSS,
                Player.PAPER: Outcome.DRAW,
                Player.SCISSORS: Outcome.WIN
            },

            Opponent.SCISSORS: {
                Player.ROCK: Outcome.WIN,
                Player.PAPER: Outcome.LOSS,
                Player.SCISSORS: Outcome.DRAW
            }
        }

        return outcome_dict[opponent][player]

    def input_score(self) -> int:
        score = 0

        for opponent, player in self.games:
            if player == Player.ROCK:
                score += 1
            elif player == Player.PAPER:
                score += 2
            elif player == Player.SCISSORS:
                score += 3

        return score

    def outcome_score(self) -> int:
        score = 0

        for opponent, player in self.games:
            game_result = self.game_logic(opponent, player)
            if game_result == Outcome.WIN:
                score += 6
            elif game_result == Outcome.DRAW:
                score += 3
            elif game_result == Outcome.LOSS:
                score += 0

        return score

    def total_score(self) -> int:
        return self.input_score() + self.outcome_score()
