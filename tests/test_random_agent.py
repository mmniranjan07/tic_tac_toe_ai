import numpy as np

from game_engine import GameEngine
from agents.random_agent import random_ai


def test_random_ai():
    game = GameEngine()

    game.board = np.array([
        ["X", "O", "X"],
        ["O", "", ""],
        ["", "X", "O"]
    ])

    legal_moves = game.get_legal_moves()
    original_board = game.board.copy()

    for i in range(100):
        move = random_ai(game)
        assert move in legal_moves

    assert np.array_equal(game.board, original_board)

    print("Random AI tests passed!")
