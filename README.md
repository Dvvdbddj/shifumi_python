# Pierre-Feuille-Ciseaux

Jeu Pierre-Feuille-Ciseaux en Python, jouable en ligne de commande contre l'ordinateur.

##  Description

Ce projet permet à l'utilisateur de choisir un signe (Pierre, Feuille ou Ciseaux), qui est ensuite confronté au choix aléatoire de l'ordinateur. Le résultat de la partie (victoire, défaite ou égalité) est affiché à l'écran.

##  Fonctionnalités

| Fonction | Description | Retour |
|----------|-------------|--------|
| `joueur()` | Demande à l'utilisateur de saisir son signe (1, 2 ou 3) | `int` |
| `ordinateur()` | Génère aléatoirement le signe de l'ordinateur | `int` |
| `combat(signe, ordi)` | Compare les deux signes et détermine le résultat | Résultat affiché |

##  Exécution

Assurez-vous d'avoir **Python 3** installé, puis lancez :

```bash
python3 main.py
```

##  Exemple d'utilisation

```
1- Pierre
2- Feuille
3- Ciseaux
entrez votre signe: 1
Vous avez joué : Pierre
L'ordinateur a joué : Ciseaux
victoire
```

##  Technologies utilisées

- Langage **Python 3**
- Module **random** (bibliothèque standard)
