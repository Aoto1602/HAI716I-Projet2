# check.py / un test sur les codes existent
import random
from Jeu.jeu import Config, play_game         
from Jeu.strategie.strat_tit_for_tat import TIT_FOR_TAT        
from Jeu.strategie.strat_all_d import ALL_D               

cfg = Config()
s1, s2 = play_game(TIT_FOR_TAT(), ALL_D(), 10, cfg, random.Random(0))
print(s1, s2)
assert (s1, s2) == (18, 23), "Résultat différent du cours (diapo 67)"
print("OK")