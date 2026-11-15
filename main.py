import argparse

from Jeu.jeu import Config, compare, print_matrix, print_ranking, tournament      
from Jeu.strategie.strat_all_d import ALL_D
from Jeu.strategie.strat_joss import JOSS
from Jeu.strategie.strat_random import RANDOM
from Jeu.strategie.strat_tester import TESTER
from Jeu.strategie.strat_tit_for_tat import TIT_FOR_TAT
from Jeu.strategie.strat_all_c import ALL_C
from Jeu.strategie.strat_grim import GRIM
from Jeu.strategie.strat_pavlov import PAVLOV
from Jeu.strategie.strat_tf2t import TF2T


etape1 = [ALL_D, RANDOM, TIT_FOR_TAT, TESTER, JOSS]
etape2 = etape1 + [ALL_C, GRIM, PAVLOV, TF2T]

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
    compare(etape2, Config(noise=0.0), Config(noise=0.05), "Sans bruit (étape 2)", "Bruit 5 %")

# étape 3 - modification 2 : autres gains
def tournoi_gains():
    raise NotImplementedError("À compléter : modifier les gains et relancer le tournoi")

TOURNOIS = {
    "etape1": tournoi_etape1,
    "etape2": tournoi_etape2,
    "bruit": tournoi_bruit,
    "gains": tournoi_gains,
}
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tournoi de dilemme du prisonnier itéré (format Axelrod)")
    parser.add_argument("tournoi", choices=TOURNOIS, help="tournoi à lancer : etape1, etape2, bruit ou gains")
    args = parser.parse_args()
    TOURNOIS[args.tournoi]()