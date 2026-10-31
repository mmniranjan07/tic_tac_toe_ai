import time
from game_engine import GameEngine
import agents.minimax_agent as mm


def benchmark(model):
    game = GameEngine()

    mm.calls = 0
    mm.cache.clear()

    start = time.perf_counter()

    move = mm.minimax_bot(game, model)

    elapsed = time.perf_counter() - start

    print(f"\n=== {model.__name__} ===")
    print(f"Chosen move: {move}")
    print(f"Recursive calls: {mm.calls:,}")
    print(f"Cache entries: {len(mm.cache):,}")
    print(f"Execution time: {elapsed:.4f} seconds")


benchmark(mm.minimax_cache)
benchmark(mm.minimax_prune)
