from Jeu.strategie.strategy import Strategy



# C au premier tour, puis rejouer le coup de l'adversaire au tour précédent
class TIT_FOR_TAT(Strategy):
    name = "TIT-FOR-TAT"

    def play(self, h1, h2, rng):
        if not h2: # premier tour
            return "C"
        else:
            return h2[-1] # rejouer le coup de l'adversaire au tour précédent