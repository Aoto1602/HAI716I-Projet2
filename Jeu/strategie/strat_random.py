from strategy import Strategy

# C ou D au hasard, une chance sur deux : sert de témoin
class RANDOM(Strategy):
    name = "RANDOM"

    def play(self, h1, h2, rng):
        return "C" if rng.random() < 0.5 else "D"