import strategy

# D au premier tour. Si l'adversaire riposte, joue TIT-FOR-TAT ; sinon répète C, C, D
class TESTER(strategy.Strategy):
    name = "TESTER"

    def __init__(self, seed=None):
        super().__init__(seed)
        # si l'adversaire a riposté à la dernière action. False par défaut
        self.opponent_reacted = False

    def reset(self):
        super().reset()
        self.opponent_reacted = False

    def play(self, h1, h2):
        if len(h1) >= 2 and h1[-2] == "D" and h2[-1] == "D":
            self.opponent_reacted = True
        if self.opponent_reacted:
            return h2[-1]
        return "D" if len(h1) %3 == 0 else "C"