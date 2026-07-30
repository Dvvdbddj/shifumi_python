import random

def joueur():
    print("1- Pierre")
    print("2- Feuille")
    print("3- Ciseaux")
    player=int(input("entrez votre signe: "))
    return player


def ordinateur():
    ordi=random.randint(1,3)
    return ordi


def combat(signe, ordi):
    if signe==1 and ordi==1:
        resultat=print("égalité")
    elif signe==2 and ordi==2:
         resultat=print("égalité")
    elif signe==3 and ordi==3:
             resultat=print("égalité")
    elif signe==1 and ordi==2:
             resultat=print("defaite")
    elif signe==1 and ordi==3:
             resultat=print("victoire")
    elif signe==2 and ordi==1:
             resultat=print("victoire")
    elif signe==2 and ordi==3:
             resultat=print("defaite")
    elif signe==3 and ordi==1:
             resultat=print("defaite")
    elif signe==3 and ordi==2:
             resultat=print("victoire")
    return resultat


signes = {
    1: "Pierre",
    2: "Feuille",
    3: "Ciseaux"
}


signe=joueur()
ordi=ordinateur()
fin=combat(signe, ordi)


print("Vous avez joué :", signes[signe])
print("L'ordinateur a joué :", signes[ordi])
print(combat(signe, ordi))
