import numpy as np
import copy

calls = 0

def evaluate_state(game):
    winner = game.check_winner()

    if winner == "X":
        return 1
    elif winner == "O":
        return -1
    else:
        return 0

def minimax(game):
    global calls
    calls += 1
    best_score = -np.inf if game.player == "X" else np.inf

    if game.game_over():
        return float(evaluate_state(game))

    moves = game.get_legal_moves()
    for move in moves:
        game_cpy = game.clone()
        game_cpy.make_move(move[0], move[1])
        score = minimax(game_cpy)
        if game.player == "X":
            best_score = max(best_score, score)
        else:
            best_score = min(best_score, score)

    return best_score


def minimax_bot(game):
    best_score = -np.inf if game.player == "X" else np.inf
    best_move = None
    for move in game.get_legal_moves():
        game_cpy = game.clone()
        game_cpy.make_move(move[0], move[1])
        score = minimax(game_cpy)
        if game.player == "X":
            if score > best_score:
                best_score = score
                best_move = move
        else:
            if score < best_score:
                best_score = score
                best_move = move
    return best_move
