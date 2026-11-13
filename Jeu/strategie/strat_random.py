import strategy

# C ou D au hasard, une chance sur deux : sert de témoin
class RANDOM(strategy.Strategy):
    name = "RANDOM"

    def play(self, h1, h2):
        return "C" if self.rng.random() < 0.5 else "D"