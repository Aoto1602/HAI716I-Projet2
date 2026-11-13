import strategy

# TIT-FOR-TAT, mais remplace C par D une fois sur dix
class JOSS(strategy.Strategy):
    name = "JOSS"

    def __init__(self, seed=None, probability_defection=0.1):
        super().__init__(seed)
        self.probability_defection = probability_defection

    def play(self, h1, h2):
        choice = "C" if len(h2) == 0 else h2[-1]
        if choice == "C" and self.rng.random() < self.probability_defection:
            choice = "D"
        return choice