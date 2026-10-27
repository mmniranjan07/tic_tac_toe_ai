import numpy as np
import random as rnd

def display_board(board):
    for i, row in enumerate(board):
        print(" | ".join(cell if cell else " " for cell in row))
        if i < 2:
            print("--+---+--")

def get_legal_moves(board):
    legal_moves = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "":
                legal_moves.append((row,col))
    return legal_moves

def make_move(board, row, col, player):
    if player not in ("X", "O"):
        return False
    if not (0 <= row < 3 and 0 <= col < 3):
        return False
    if game_over(board):
        return False
    if board[row][col] != "":
        return False

    board[row][col] = player
    return True

def check_winner(board):
    for row in board:
        if np.all(row == "X") or np.all(row == "O"):
                return row[0]
    for col in board.T:
        if np.all(col == "X") or np.all(col == "O"):
                return col[0]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    return None

def is_draw(board):
    return not get_legal_moves(board) and check_winner(board) is None

def game_over(board):
    return check_winner(board) is not None or is_draw(board)

def play_game():
    board = np.full((3, 3), "", dtype="<U1")
    player = "X"

    while not game_over(board):
        display_board(board)

        if player == "X":
            while True:
                try:
                    x = int(input("Enter your row: "))
                    y = int(input("Enter your column: "))
                except ValueError:
                    print("Please enter a valid integer")
                    continue

                if make_move(board, x, y, player):
                    break

                print("Invalid move")
                print(f"Available moves: {get_legal_moves(board)}")

        else:
            x, y  = random_ai(board)
            if not make_move(board, x, y, player):
                raise RuntimeError(f"Invalid move: ({x}, {y})")
            print(f"AI played at ({x}, {y})")

        player = "O" if player == "X" else "X"
    display_board(board)

    winner = check_winner(board)
    print(f"Winner: {winner}" if winner else "Draw")

def test_game_engine():
    empty = np.full((3, 3), "", dtype="<U1")

    assert len(get_legal_moves(empty)) == 9
    assert check_winner(empty) is None
    assert is_draw(empty) is False
    assert game_over(empty) is False

    row_win = np.array([
        ["X", "X", "X"],
        ["O", "O", ""],
        ["", "", ""]
    ])
    assert check_winner(row_win) == "X"
    assert game_over(row_win) is True
    assert make_move(row_win, 2, 2, "O") is False

    col_win = np.array([
        ["O", "X", ""],
        ["O", "X", ""],
        ["O", "", ""]
    ])
    assert check_winner(col_win) == "O"

    diagonal_win = np.array([
        ["X", "O", ""],
        ["O", "X", ""],
        ["", "", "X"]
    ])
    assert check_winner(diagonal_win) == "X"

    draw = np.array([
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", "X"]
    ])
    assert is_draw(draw) is True
    assert game_over(draw) is True

    print("All game engine tests passed!")

def random_ai(board):
    return rnd.choice(get_legal_moves(board))

def test_random_ai():
    board = np.array([
        ["X", "O", "X"],
        ["O", "", ""],
        ["", "X", "O"]
    ])

    legal_moves = get_legal_moves(board)

    for i in range(100):
        move = random_ai(board)
        assert move in legal_moves

    print("Random AI tests passed!")

def play_rnd_ais():
    winner_X = 0
    winner_O = 0
    draw = 0
    for i in range(100):
        player = 'X'
        board = np.full((3, 3), "", dtype="<U1")

        while not game_over(board):
            x, y = random_ai(board)

            if not make_move(board, x, y, player):
                raise RuntimeError(f"Invalid move: ({x}, {y})")

            print(f"AI {player} played at ({x}, {y})")
            player = "O" if player == "X" else "X"

        display_board(board)
        winner = check_winner(board)
        print(f"Winner: {winner}" if winner else "Draw")
        winner_X += 1 if winner == "X" else 0
        winner_O += 1 if winner == "0" else 0
        draw += 1 if winner is None else 0

    

if __name__ == "__main__":
    test_game_engine()
    test_random_ai()
    play_rnd_ais()
    play_game()