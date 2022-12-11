import utils
from Day2.opponent import Opponent
from Day2.player import Player


class Part1:
    def __init__(self, games: list[tuple[str, str]]):
        self.games = games

    @staticmethod
    def game_logic(opponent, player) -> str:
        """
        Logic for rock, paper, scissors game.

        :return: A string representation of the outcome of the game.
        """
        # win
        rock_paper = opponent == Opponent.ROCK and player == Player.PAPER
        scissor_rock = opponent == Opponent.SCISSORS and player == Player.ROCK
        paper_scissors = opponent == Opponent.PAPER and player == Player.SCISSORS

        # draw
        both_rock = opponent == Opponent.ROCK and player == Player.ROCK
        both_paper = opponent == Opponent.PAPER and player == Player.PAPER
        both_scissors = opponent == Opponent.SCISSORS and player == Player.SCISSORS

        # win
        if rock_paper or scissor_rock or paper_scissors:
            return 'W'

        # draw
        elif both_rock or both_paper or both_scissors:
            return 'D'

        # loss
        else:
            return 'L'

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
            if game_result == 'W':
                score += 6
            elif game_result == 'D':
                score += 3
            elif game_result == 'L':
                score += 0

        return score

    def total_score(self) -> int:
        return self.input_score() + self.outcome_score()


def separate_games() -> list[tuple[str, str]]:
    games = []

    for line in utils.read_input_file():
        opponent_input, player_input = line.split(' ')
        games.append((opponent_input, player_input))

    return games


def main():
    games = separate_games()
    print(Part1(games).total_score())


if __name__ == '__main__':
    main()
