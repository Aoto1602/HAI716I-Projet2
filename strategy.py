import random

#classe de base pour toutes les stratégies qu'on va implémenter pour le dilemme du prisonnier itéré
class Strategy:
    name = " "

    def __init__(self, seed=None):
        self.seed = seed
        self.rng = random.Random(seed)

    def reset(self):
        self.rng = random.Random(self.seed)

    # h1 : historique de mes coups
    # h2 : historique des coups de l'adversaire
    def play(self, h1, h2):
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes")