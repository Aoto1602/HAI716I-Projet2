from Jeu.jeu import Config, tournament      
from Jeu.strategie.strat_all_d import ALL_D
from Jeu.strategie.strat_joss import JOSS
from Jeu.strategie.strat_random import RANDOM
from Jeu.strategie.strat_tester import TESTER
from Jeu.strategie.strat_tit_for_tat import TIT_FOR_TAT


M, ranking = tournament([ALL_D, RANDOM, TIT_FOR_TAT, TESTER, JOSS], Config())

for name, total in ranking:
    print(name, total)

for a in M:
    print(a, M[a])