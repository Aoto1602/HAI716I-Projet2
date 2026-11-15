from Jeu.strategie.strategy import Strategy



# D au premier tour. Si l'adversaire riposte, joue TIT-FOR-TAT ; sinon répète C, C, D
class TESTER(Strategy):
    name = "TESTER"

    def __init__(self):
        super().__init__()
        # si l'adversaire a riposté à la dernière action. False par défaut
        self.opponent_reacted = False

    def reset(self):
        super().reset()
        self.opponent_reacted = False

    def play(self, h1, h2, rng):
        if len(h1) >= 2 and h1[-2] == "D" and h2[-1] == "D": # j'ai joué D à l'avant-dernier tour et l'adversaire a riposté avec D
            self.opponent_reacted = True
        if self.opponent_reacted:
            return h2[-1] # joue TIT-FOR-TAT
        return "D" if len(h1) %3 == 0 else "C" # séquence C, C, D