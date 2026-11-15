from Jeu.jeu import Config, compare, tournament      
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
#M, ranking = tournament(etape1, Config(noise=0.0))
#print_ranking("Étape 1", ranking)
#print_matrix("Matrice étape 1", M)

# étape 2
#M, ranking = tournament(etape2, Config(noise=0.0))
#print_ranking("Étape 2", ranking)
#print_matrix("Matrice étape 2", M)

# étape 3 - modification 1 : bruit
compare(etape2,
        Config(noise=0.0), Config(noise=0.05),
        "Sans bruit (étape 2)", "Bruit 5 %")