import utils


class Opponent:
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'


class Player:
    ROCK = 'X'
    PAPER = 'Y'
    SCISSORS = 'Z'


class Part1:
    def __init__(self, games: list[tuple[str, str]]):
        self.games = games

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
            game_result = rps_logic(opponent, player)
            if game_result == 'W':
                score += 6
            elif game_result == 'D':
                score += 3
            elif game_result == 'L':
                score += 0

        return score

    def total_score(self) -> int:
        return self.input_score() + self.outcome_score()


class NeededOutcome:
    WIN = 'Z'
    DRAW = 'Y'
    LOSE = 'X'


class Part2(Part1):
    def __init__(self, games):
        super().__init__(games)
        self.games = games

    def needed_sign(self) -> str:
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

        for opponent, outcome in self.games:
            # draws
            if NeededOutcome.DRAW == outcome:
                return draw_dict[opponent]

            elif NeededOutcome.WIN == outcome:
                return win_dict[opponent]

            elif NeededOutcome.LOSE == outcome:
                return lose_dict[opponent]

            raise ValueError(f'Game outcome: {outcome} or opponent input: {opponent} not valid')

    def outcome_score(self) -> int:
        pass


def separate_games() -> list[tuple[str, str]]:
    games = []

    for line in utils.read_input_file():
        opponent_input, player_input = line.split(' ')
        games.append((opponent_input, player_input))

    return games


def rps_logic(opponent, player) -> str:
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


def main():
    games = separate_games()
    # part 1
    print(Part1(games).total_score())

    # part 2
    print(Part2(games).total_score())


if __name__ == '__main__':
    main()
