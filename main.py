from Jeu.jeu import Config, tournament      
from Jeu.strategie.strat_all_d import ALL_D
from Jeu.strategie.strat_joss import JOSS
from Jeu.strategie.strat_random import RANDOM
from Jeu.strategie.strat_tester import TESTER
from Jeu.strategie.strat_tit_for_tat import TIT_FOR_TAT
from Jeu.strategie.strat_pavlov import Pavlov
from Jeu.strategie.strat_grim import Grim
from Jeu.strategie.strat_tf2t import TF2T



M, ranking = tournament([ALL_D, RANDOM, TIT_FOR_TAT, TESTER, JOSS,Pavlov,Grim,TF2T], Config())

for name, total in ranking:
    print(name, total)

for a in M:
    print(a, M[a])