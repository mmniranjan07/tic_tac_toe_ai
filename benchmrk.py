
import time

from game_engine import GameEngine
import agents.minimax_agent as mm


def benchmark():
    game = GameEngine()

    mm.calls = 0

    start = time.perf_counter()

    move = mm.minimax_bot(game)

    elapsed = time.perf_counter() - start

    print("=== MINIMAX BENCHMARK ===")
    print(f"Chosen move: {move}")
    print(f"Recursive calls: {mm.calls:,}")
    print(f"Execution time: {elapsed:.4f} seconds")


if __name__ == "__main__":
    benchmark()
