import random

#classe de base pour toutes les stratégies qu'on va implémenter pour le dilemme du prisonnier itéré
class Strategy:
    name = " - "

    def reset(self):
        pass

    # h1 : historique de mes coups
    # h2 : historique des coups de l'adversaire
    # rng : objet random.Random fourni par le moteur
    def play(self, h1, h2, rng):
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes")