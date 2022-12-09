class Opponent:
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'


class Player:
    ROCK = 'X'
    PAPER = 'Y'
    SCISSORS = 'Z'


def rps_logic(win_score=6, draw_score=3, loss_score=0) -> int:
    """
    Logic for rock, paper, scissors game.

    :return: The score representing the outcome of the game.
    """
    # win
    rock_paper = Opponent.ROCK and Player.PAPER
    scissor_rock = Opponent.SCISSORS and Player.ROCK
    paper_scissors = Opponent.PAPER and Player.SCISSORS

    # draw
    both_rock = Opponent.ROCK and Player.ROCK
    both_paper = Opponent.PAPER and Player.PAPER
    both_scissors = Opponent.SCISSORS and Player.SCISSORS

    # win
    if rock_paper or scissor_rock or paper_scissors:
        return win_score

    # draw
    elif both_rock or both_paper or both_scissors:
        return draw_score

    # loss
    else:
        return loss_score


def input_score():
    pass


def outcome_score():
    pass


def total_score():
    pass


def main():
    # part 1
    pass


if __name__ == '__main__':
    main()
