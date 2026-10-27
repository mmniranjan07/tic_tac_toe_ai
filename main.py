from agents.random_agent import random_ai
from simulation import evaluate_bots

from tests.test_game_engine import test_game_engine
from tests.test_random_agent import test_random_ai


def main():
    test_game_engine()
    test_random_ai()

    print("\nRandom AI vs Random AI")
    evaluate_bots(random_ai, random_ai, 1000)


if __name__ == "__main__":
    main()
