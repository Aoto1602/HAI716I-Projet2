
from dataclasses import dataclass, field
import random

from Jeu.strategie.strat_all_d import ALL_D
from Jeu.strategie.strat_joss import JOSS
from Jeu.strategie.strat_random import RANDOM
from Jeu.strategie.strat_tester import TESTER
from Jeu.strategie.strat_tit_for_tat import TIT_FOR_TAT
from Jeu.strategie.strat_pavlov import Pavlov
from Jeu.strategie.strat_grim import Grim
from Jeu.strategie.strat_tf2t import TF2T


C, D = "C", "D"
PD = {(C,C):(3,3), (C,D):(0,5), (D,C):(5,0), (D,D):(2,2)}
classes=[ALL_D,RANDOM,TIT_FOR_TAT,TESTER,JOSS,Pavlov,Grim,TF2T]

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

"""
def game_lengths(cfg):
    ///所有对局共用同一组局长，保证公平。
    rng = random.Random(f"{cfg.seed}-lengths")
    if cfg.w is None:
        return [cfg.rounds] * cfg.games
    out = []
    for _ in range(cfg.games):
        n = 1
        while rng.random() < cfg.w: n += 1
        out.append(n)
    return out

"""
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