import strategy

# toujours D : la stratégie « rationnelle » de la récurrence à rebours
class ALL_D(strategy.Strategy):
    name = "ALL-D"

    def play(self, h1, h2):
        return "D"