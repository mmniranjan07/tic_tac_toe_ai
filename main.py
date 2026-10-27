from agents.random_agent import random_ai
from simulation import evaluate_bots
from agents.minimax_agent import minimax_bot
import time
from tests.test_game_engine import test_game_engine
from tests.test_random_agent import test_random_ai


def main():
    test_game_engine()
    test_random_ai()

    print("\nMiniMax AI vs Random AI")
    start = time.perf_counter()

    evaluate_bots(minimax_bot, random_ai, 1)

    end = time.perf_counter()

    print(f"Execution time: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
