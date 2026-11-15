# HAI716I-Projet2

### Commandes pour lancer le programme

Toutes les commandes se lancent depuis la racine du projet

## Étape 1 :  les 5 stratégies du cours
ALL-D, RANDOM, TIT-FOT-TAT, TESTER et JOSS

```bash
python3 main.py etape1
```

## Étape 2 :  la population élargie
les 5 stratégies du cours + ALL-C, GRIM, PAVLOV et TF2T

```bash
python3 main.py etape2
```

## Étape 3, modification 1 : bruit
les 9 stratégies, chaque coup inversé avec une probabilité de 5%

```bash
python3 main.py bruit
```


## Étape 3, modification 2 : autres gains
on a 2 matrices différents que celle de prisonnier(celle du cours)

Chasse au cerf, valeurs de la diapositive 76 : C,C > D,C > D,D > C,D
    "Chasse au cerf", {(C, C): (4, 4), (C, D): (0, 3), (D, C): (3, 0), (D, D): (1, 1)}

Poule mouillée, ordre de la diapositive 74 : D,C > C,C > C,D > D,D
    "chicken": "Poule mouillée", {(C, C): (3, 3), (C, D): (1, 4), (D, C): (4, 1), (D, D): (0, 0)}


```bash
python3 main.py gains #(par défault on utilise la chasse au cerf)

python3 main.py gains --jeu cerf

python3 main.py gains --jeu chicken
```

## Aide
affiche les tournois disponibles

```bash
python3 main.py --help
```