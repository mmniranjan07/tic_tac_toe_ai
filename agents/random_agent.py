import random as rnd

def random_ai(game):
    return rnd.choice(game.get_legal_moves())
