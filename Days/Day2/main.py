import utils
from Days.Day2 import RPS, RPSTwist


def separate_games() -> list[tuple[str, str]]:
    games = []

    for line in utils.read_input_file():
        line = line.strip()
        opponent_input, player_input = line.split(' ')
        games.append((opponent_input, player_input))

    return games


def main():
    games = separate_games()

    # part 1
    print(RPS(games).total_score())

    # part 2
    print(RPSTwist(games).total_score())


if __name__ == '__main__':
    main()
