import argparse

from Jeu.jeu import C,D,Config, compare, print_matrix, print_ranking, tournament      
from Jeu.strategie.strat_all_d import ALL_D
from Jeu.strategie.strat_joss import JOSS
from Jeu.strategie.strat_random import RANDOM
from Jeu.strategie.strat_tester import TESTER
from Jeu.strategie.strat_tit_for_tat import TIT_FOR_TAT
#from Jeu.strategie.strat_all_c import ALL_C
from Jeu.strategie.strat_grim import GRIM
from Jeu.strategie.strat_pavlov import PAVLOV
from Jeu.strategie.strat_tf2t import TF2T


etape1 = [ALL_D, RANDOM, TIT_FOR_TAT, TESTER, JOSS]
etape2 = etape1 + [GRIM, PAVLOV, TF2T]

# étape 1
def tournoi_etape1():
    M, ranking = tournament(etape1, Config(noise=0.0))
    print_ranking("Étape 1 : stratégies du cours", ranking)
    print_matrix("Matrice étape 1 (score de la LIGNE contre la COLONNE)", M)

# étape 2
def tournoi_etape2():
    M, ranking = tournament(etape2, Config(noise=0.0))
    _, ranking1 = tournament(etape1, Config(noise=0.0))
    print_ranking("Étape 1 : stratégies du cours", ranking1)
    print_ranking("Étape 2 : population élargie", ranking, ref_ranking=ranking1, score_diff=False)
    print_matrix("Matrice étape 2 (score de la LIGNE contre la COLONNE)", M)

# étape 3 - modification 1 : bruit
def tournoi_bruit():
    compare(etape2, Config(noise=0.0), Config(noise=0.1), "Sans bruit (étape 2)", "Bruit 10 %")


# Matrices des jeux 2x2 (section 07 du cours)
JEUX = {
    # Chasse au cerf, valeurs de la diapositive 76 : C,C > D,C > D,D > C,D
    "cerf": ("Chasse au cerf", {(C, C): (4, 4), (C, D): (0, 3), (D, C): (3, 0), (D, D): (1, 1)}),
    # Poule mouillée, ordre de la diapositive 74 : D,C > C,C > C,D > D,D
    "chicken": ("Poule mouillée", {(C, C): (3, 3), (C, D): (1, 4), (D, C): (4, 1), (D, D): (0, 0)}),
}



# étape 3 - modification 2 : autres gains
def tournoi_gains(jeu):
    nom, gains = JEUX[jeu]
    compare(etape2, Config(), Config(payoff=gains), "Dilemme du cours", nom)
TOURNOIS = {
    "etape1": tournoi_etape1,
    "etape2": tournoi_etape2,
    "bruit": tournoi_bruit,
    "gains": tournoi_gains,
}
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tournoi de dilemme du prisonnier itéré (format Axelrod)")
    parser.add_argument("tournoi", choices=TOURNOIS, help="tournoi à lancer : etape1, etape2, bruit ou gains")
    parser.add_argument("--jeu", choices=JEUX, default="cerf",
                        help="matrice utilisée par le tournoi gains : cerf ou chicken")
    args = parser.parse_args()
    if args.tournoi == "gains":
        tournoi_gains(args.jeu)
    else:
        TOURNOIS[args.tournoi]()