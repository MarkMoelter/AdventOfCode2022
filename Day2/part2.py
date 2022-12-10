from Day2.needed_outcome import NeededOutcome
from Day2.opponent import Opponent
from Day2.part1 import Part1, separate_games


class Part2(Part1):
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

        draw_dict = {
            Opponent.ROCK: 'rock',
            Opponent.PAPER: 'paper',
            Opponent.SCISSORS: 'scissors',
        }

        win_dict = {
            Opponent.ROCK: 'paper',
            Opponent.PAPER: 'scissors',
            Opponent.SCISSORS: 'rock',
        }

        lose_dict = {
            Opponent.ROCK: 'scissors',
            Opponent.PAPER: 'rock',
            Opponent.SCISSORS: 'paper',
        }

        # draws
        if NeededOutcome.DRAW == outcome:
            return draw_dict[opponent]

        elif NeededOutcome.WIN == outcome:
            return win_dict[opponent]

        elif NeededOutcome.LOSE == outcome:
            return lose_dict[opponent]
        else:
            raise ValueError(f'Game outcome: {outcome} or opponent input: {opponent} not valid')

    def outcome_score(self) -> int:
        pass


def main():
    games = separate_games()
    print(Part2(games).total_score())


if __name__ == '__main__':
    main()
