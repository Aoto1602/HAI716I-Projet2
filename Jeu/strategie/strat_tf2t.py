from Jeu.strategie.strategy import Strategy


class TF2T(Strategy):
    """TIT-FOR-TWO-TATS(trouvé sur internet)

    Règle : coopère, et ne trahit que si l'adversaire a trahi aux DEUX
    derniers tours.

    Origine : Axelrod note qu'elle aurait gagné le premier tournoi (1980)
    si quelqu'un l'avait soumise ; proposée au second tournoi par
    John Maynard Smith.

    Attendu : plus indulgente que TFT, elle évite les échos de représailles
    après une trahison isolée (JOSS, bruit). En revanche, une stratégie qui
    trahit un tour sur deux l'exploite sans jamais être punie.
    """

    name = "TF2T"

    def play(self, h1, h2, rng):
        if len(h2) >= 2 and h2[-1] == "D" and h2[-2] == "D":
            return "D"
        return "C"