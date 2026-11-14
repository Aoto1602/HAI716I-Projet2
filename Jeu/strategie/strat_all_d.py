from strategy import Strategy

# toujours D : la stratégie « rationnelle » de la récurrence à rebours
class ALL_D(Strategy):
    name = "ALL-D"

    def play(self, h1, h2, rng):
        return "D"