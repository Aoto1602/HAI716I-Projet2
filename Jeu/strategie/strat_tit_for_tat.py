import strategy

# C au premier tour, puis rejouer le coup de l'adversaire au tour précédent
class TIT_FOR_TAT(strategy.Strategy):
    name = "TIT-FOR-TAT"

    def play(self, h1, h2):
        if len(h2) == 0:
            return "C"
        else:
            return h2[-1]