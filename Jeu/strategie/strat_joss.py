from Jeu.strategie.strategy import Strategy



# TIT-FOR-TAT, mais remplace C par D une fois sur dix
class JOSS(Strategy):
    name = "JOSS"

    def __init__(self, probability_defection=0.1):
        super().__init__()
        self.probability_defection = probability_defection

    def play(self, h1, h2, rng):
        choice = "C" if not h2 else h2[-1]
        if choice == "C" and rng.random() < self.probability_defection:
            choice = "D"
        return choice