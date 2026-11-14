from Jeu.strategie.strategy import Strategy


class Pavlov(Strategy):
    """PAVLOV / WIN-STAY LOSE-SHIFT (WSLS)

    Règle : coopère au premier tour. Ensuite, si le tour précédent a bien
    rapporté (3 ou 5), rejoue le même coup ; sinon (0 ou 2), change de coup.
    Équivalent : joue C si les deux joueurs ont joué le même coup au tour
    précédent, D sinon.

    Origine : Kraines & Kraines (1989) ; Nowak & Sigmund (1993, Nature).

    Attendu : se réconcilie toute seule après une erreur entre deux PAVLOV
    (utile avec du bruit) et exploite ALL-C. Faible contre ALL-D : elle
    recoopère un tour sur deux (D,D -> C), donc se fait avoir plus que TFT.
    """

    name = "PAVLOV"

    def play(self, h1, h2, rng):
        if not h1:
            return "C"
        return "C" if h1[-1] == h2[-1] else "D"