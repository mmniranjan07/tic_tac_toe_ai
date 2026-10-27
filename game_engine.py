
import numpy as np
import random as rnd


class GameEngine:
    def __init__(self):
        self.board = np.full((3, 3), "", dtype="<U1")
        self.player = "X"

    def display_board(self):
        for i, row in enumerate(self.board):
            print(" | ".join(cell if cell else " " for cell in row))
            if i < 2:
                print("--+---+--")

    def get_legal_moves(self):
        legal_moves = []
        for row in range(self.board.shape[0]):
            for col in range(self.board.shape[1]):
                if self.board[row][col] == "":
                    legal_moves.append((row, col))
        return legal_moves

    def check_winner(self):
        for row in self.board:
            if np.all(row == "X") or np.all(row == "O"):
                return row[0]

        for col in self.board.T:
            if np.all(col == "X") or np.all(col == "O"):
                return col[0]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]

        return None

    def make_move(self, row, col):
        if not (0 <= row < 3 and 0 <= col < 3):
            return False

        if self.game_over():
            return False

        if self.board[row][col] != "":
            return False

        self.board[row][col] = self.player
        self.player = "O" if self.player == "X" else "X"
        return True

    def is_draw(self):
        return not self.get_legal_moves() and self.check_winner() is None

    def game_over(self):
        return self.check_winner() is not None or self.is_draw()
