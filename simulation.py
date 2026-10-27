from game_engine import GameEngine

def simulate_game(bot_x, bot_o):
    game = GameEngine()

    while not game.game_over():
        if game.player == "X":
            x, y = bot_x(game)
        else:
            x, y = bot_o(game)
        if not game.make_move(x, y):
            raise RuntimeError("AI made an invalid move")

    return game.check_winner()


def evaluate_bots(bot_x, bot_o, n_games=1000):
    winner_x = 0
    winner_o = 0
    draw = 0

    for i in range(n_games):
        winner = simulate_game(bot_x, bot_o)
        winner_x += 1 if winner == "X" else 0
        winner_o += 1 if winner == "O" else 0
        draw += 1 if winner is None else 0

    assert winner_x + winner_o + draw == n_games
    print(f"X wins: {winner_x}")
    print(f"O wins: {winner_o}")
    print(f"Draws: {draw}")
    return winner_x, winner_o, draw