from Jeu.strategie.strategy import Strategy

# toujours D : la stratégie « rationnelle » de la récurrence à rebours
class ALL_C(Strategy):
    name = "ALL-C"

    def play(self, h1, h2, rng):
        return "C"