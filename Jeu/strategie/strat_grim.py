from Jeu.strategie.strategy import Strategy


class Grim(Strategy):
    """GRIM TRIGGER (rancunière)

    Règle : coopère tant que l'adversaire n'a jamais trahi ; dès sa première
    trahison, trahit pour toujours.

    Origine : Friedman (1971) ; une stratégie de ce type (FRIEDMAN) était
    présente au tournoi d'Axelrod de 1980.

    Attendu : gentille (ne trahit jamais la première) mais sans pardon.
    Très bonne contre les coopératives pures, mais une seule trahison
    (JOSS, TESTER, RANDOM, bruit) la bloque définitivement en D,D.
    Sert de contre-exemple aux règles d'Axelrod sur le pardon.
    """

    name = "GRIM"

    def play(self, h1, h2, rng):
        return "D" if "D" in h2 else "C"