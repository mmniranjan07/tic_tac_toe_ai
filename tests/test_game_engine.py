
import numpy as np
from game_engine import GameEngine


def test_game_engine():
    game = GameEngine()

    assert len(game.get_legal_moves()) == 9
    assert game.check_winner() is None
    assert game.is_draw() is False
    assert game.game_over() is False

    assert game.make_move(0, 0) is True
    assert game.board[0][0] == "X"
    assert game.player == "O"

    assert game.make_move(0, 0) is False
    assert game.make_move(-1, 0) is False
    assert game.make_move(3, 3) is False

    game = GameEngine()
    assert len(game.get_legal_moves()) == 9
    assert game.player == "X"

    row_win = np.array([
        ["X", "X", "X"],
        ["O", "O", ""],
        ["", "", ""]
    ])
    game.board = row_win
    assert game.check_winner() == "X"
    assert game.game_over() is True
    assert game.make_move(2, 2) is False

    col_win = np.array([
        ["O", "X", ""],
        ["O", "X", ""],
        ["O", "", ""]
    ])
    game.board = col_win
    assert game.check_winner() == "O"

    diagonal_win = np.array([
        ["X", "O", ""],
        ["O", "X", ""],
        ["", "", "X"]
    ])
    game.board = diagonal_win
    assert game.check_winner() == "X"

    opposite_diagonal = np.array([
        ["", "O", "X"],
        ["O", "X", ""],
        ["X", "", ""]
    ])
    game.board = opposite_diagonal
    assert game.check_winner() == "X"

    draw = np.array([
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", "X"]
    ])
    game.board = draw
    assert game.is_draw() is True
    assert game.game_over() is True

    print("All game engine tests passed!")
