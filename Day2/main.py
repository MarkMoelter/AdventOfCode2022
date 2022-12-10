import utils


class Opponent:
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'


class Player:
    ROCK = 'X'
    PAPER = 'Y'
    SCISSORS = 'Z'


class Solution:
    def __init__(self, games: list[tuple[str, str]]):
        self.games = games

    @staticmethod
    def rps_logic(opponent, player) -> int:
        """
        Logic for rock, paper, scissors game.

        :return: The score representing the outcome of the game.
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
            return 6

        # draw
        elif both_rock or both_paper or both_scissors:
            return 3

        # loss
        else:
            return 0

    def input_score(self) -> int:
        rock = 1
        paper = 2
        scissors = 3

        result = 0

        for game in self.games:
            if game[1] == Player.ROCK:
                result += rock
            elif game[1] == Player.PAPER:
                result += paper
            elif game[1] == Player.SCISSORS:
                result += scissors

        return result

    def outcome_score(self) -> int:
        result = 0

        for opponent, player in self.games:
            result += self.rps_logic(opponent, player)

        return result

    def total_score(self) -> int:
        return self.input_score() + self.outcome_score()


def separate_games() -> list[tuple[str, str]]:
    games = []

    for line in utils.read_input_file():
        opponent_input, player_input = line.split(' ')
        games.append((opponent_input, player_input))

    return games


def main():
    # part 1
    print(Solution(separate_games()).total_score())

    # part 2


if __name__ == '__main__':
    main()
