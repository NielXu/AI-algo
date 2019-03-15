"""
Minimax is an algorithm that tries to maximize computer's
move while minimize player's move. It usually make a few
simulation moves and then evaluate score for each move
and pick the best move.

Wiki:
Minimax (sometimes MinMax or MM[1]) is a decision rule used
in artificial intelligence, decision theory, game theory,
statistics and philosophy for minimizing the possible loss for
a worst case (maximum loss) scenario. When dealing with gains,
it is referred to as "maximin"—to maximize the minimum gain.
"""
import game


MAX_DEPTH = 9
MIN = -999
MAX = 999


def gen(b):
    "Generate move and give (x,y)"
    return gen_move(b, False, 0)[1]


def gen_move(b, p, d):
    "Generation based on player(minimize) and computer(maximize)"
    best = MIN if not p else MAX
    move = (-1, -1)
    if d == MAX_DEPTH or game.is_full(b):
        best = evaluate(b)
    else:
        for i in range(3):
            for j in range(3):
                if game.is_placed(b, i, j):
                    continue
                cp = game.cp_board(b)
                game.make_move(cp, i, j, p)
                score = gen_move(cp, not p, d+1)[0]
                if p:
                    if score < best:
                        best = score
                        move = (i,j)
                else:
                    if score > best:
                        best = score
                        move = (i,j)
    return best, move


def evaluate(b):
    "Evaluate the score on board"
    score = 0
    score += evaluate_line(b, 0, 0, 0, 1, 0, 2)
    score += evaluate_line(b, 1, 0, 1, 1, 1, 2)
    score += evaluate_line(b, 2, 0, 2, 1, 2, 2)
    score += evaluate_line(b, 0, 0, 1, 0, 2, 0)
    score += evaluate_line(b, 0, 1, 1, 1, 2, 1)
    score += evaluate_line(b, 0, 2, 1, 2, 2, 2)
    score += evaluate_line(b, 0, 0, 1, 1, 2, 2)
    score += evaluate_line(b, 0, 2, 1, 1, 2, 0)
    return score


def evaluate_line(b, r1, c1, r2, c2, r3, c3):
    "Evaluate each line's score"
    score = 0
    if b[r1][c1] == "X":
        score = 1
    elif b[r1][c1] == "O":
        score = -1
    
    if b[r2][c2] == "X":
        if score == 1:
            score = 10
        elif score == -1:
            score = 0
        else:
            score = 1
    elif b[r2][c2] == "O":
        if score == -1:
            score = -10
        elif score == 1:
            score = 0
        else:
            score = -1
    
    if b[r3][c3] == "X":
        if score > 0:
            score *= 10
        elif score < 0:
            return 0
        else:
            return 1
    elif b[r3][c3] == "O":
        if score < 0:
            score *= 10
        elif score > 0:
            return 0
        else:
            score = -1
    return score


if __name__ == "__main__":
    b = [
        ["O", "O", "X"],
        ["O", "O", "X"],
        ["X", "-", "-"]
    ]
    # (2,0) to win
    print(gen_move(b, False, 0))

    b = [
        ["O", "-", "X"],
        ["X", "-", "O"],
        ["X", "X", "O"]
    ]
    # (1,1) to win
    print(gen_move(b, False, 0))
