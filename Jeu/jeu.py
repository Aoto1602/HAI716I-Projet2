
from dataclasses import dataclass, field
import random

from Jeu.strategie.strat_all_d import ALL_D
from Jeu.strategie.strat_joss import JOSS
from Jeu.strategie.strat_random import RANDOM
from Jeu.strategie.strat_tester import TESTER
from Jeu.strategie.strat_tit_for_tat import TIT_FOR_TAT
from Jeu.strategie.strat_pavlov import PAVLOV
from Jeu.strategie.strat_grim import GRIM
from Jeu.strategie.strat_tf2t import TF2T


C, D = "C", "D"
PD = {(C,C):(3,3), (C,D):(0,5), (D,C):(5,0), (D,D):(2,2)}

Chasse_au_cerf= {("C","C"): (4,4), ("C","D"): (0,3),
             ("D","C"): (3,0), ("D","D"): (1,1)}


classes=[ALL_D,RANDOM,TIT_FOR_TAT,TESTER,JOSS,PAVLOV,GRIM,TF2T]


@dataclass
class Config:
    rounds: int = 200
    games: int = 5
    payoff: dict = field(default_factory=lambda: dict(PD))
    noise: float = 0.0          # bruit
    self_play: bool = False     # contre lui meme

    seed: int = 42

def flip(a): return D if a == C else C

def play_game(s1, s2, n_rounds, cfg, rng):
    s1.reset(); s2.reset()
    h1, h2, sc1, sc2 = [], [], 0, 0
    for _ in range(n_rounds):
        a1 = s1.play(tuple(h1), tuple(h2), rng)   # tuple 防止策略篡改历史; h1,h2 sont des histoires des choix de chacun
        a2 = s2.play(tuple(h2), tuple(h1), rng)
        if rng.random() < cfg.noise: a1 = flip(a1)  # noise pour deranger les stratégie,si le noise a reussi a déranger, alors le choix de stratégie va etre l'inverse
        if rng.random() < cfg.noise: a2 = flip(a2)
        p1, p2 = cfg.payoff[(a1, a2)]
        sc1 += p1; sc2 += p2
        h1.append(a1); h2.append(a2)
    return sc1, sc2

def tournament(classes, cfg):
    names = [c.name for c in classes]
    M = {a: {b: 0.0 for b in names} for a in names}
    for i, A in enumerate(classes):
        for j, B in enumerate(classes):
            if j < i or (i == j and not cfg.self_play):
                continue
            rng = random.Random(f"{cfg.seed}-{A.name}-{B.name}")
            for _ in range(cfg.games):
                s1, s2 = play_game(A(), B(), cfg.rounds, cfg, rng)
                M[A.name][B.name] += s1
                if i != j:
                    M[B.name][A.name] += s2
    totals = {a: sum(M[a].values()) for a in names}
    return M, sorted(totals.items(), key=lambda kv: -kv[1])

# affiche le classement
def print_ranking(title, ranking, ref_ranking=None, score_diff=True):
    nb_opp = len(ranking) - 1                      # nombre d'adversaires par stratégie
    print(f"=== {title} ===")
    if ref_ranking:
        ref_rank = {n: i for i, (n, _) in enumerate(ref_ranking, 1)}
        ref_score = dict(ref_ranking)
    for i, (name, total) in enumerate(ranking, 1):
        line = f"{i}. {name:<12} {total:>7.0f}   moyenne/duel {total / nb_opp:>6.0f}"
        if ref_ranking:
            if name in ref_rank:
                line += f"   rang {ref_rank[name]} -> {i} ({ref_rank[name] - i:+d})"
                if score_diff:
                    line += f"   score {total - ref_score[name]:+.0f}"
            else:
                line += "   nouvelle"
        print(line)
    print()

# affiche la matrice des scores (ligne contre colonne, total sur toutes les parties)
def print_matrix(title, M, ref_M=None):
    names = list(M)
    print(title)
    print(" " * 12 + "".join(f"{n[:7]:>8}" for n in names))
    for a in names:
        cells = []
        for b in names:
            if a == b:
                cells.append(f"{'-':>8}")
            elif ref_M:
                cells.append(f"{M[a][b] - ref_M[a][b]:>+8.0f}")
            else:
                cells.append(f"{M[a][b]:>8.0f}")
        print(f"{a:<12}" + "".join(cells))
    print()

# lance deux tournois sur la même population et affiche la comparaison
def compare(classes, cfg_ref, cfg_new, title_ref, title_new):
    print(f"Protocole : {cfg_new.games} parties x {cfg_new.rounds} tours, "
          f"graine {cfg_new.seed}, contre soi-même {cfg_new.self_play}\n")
    M_ref, r_ref = tournament(classes, cfg_ref)
    M_new, r_new = tournament(classes, cfg_new)
    print_ranking(title_ref, r_ref)
    print_ranking(title_new, r_new, ref_ranking=r_ref)
    print_matrix(f"Matrice {title_ref} (score de la LIGNE contre la COLONNE)", M_ref)
    print_matrix(f"Matrice {title_new} (score de la LIGNE contre la COLONNE)", M_new)
    print_matrix(f"Écart {title_new} - {title_ref}", M_new, ref_M=M_ref)