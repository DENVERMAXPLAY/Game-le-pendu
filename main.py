#Création d'un jeu : le pendu
import random


def jeu_pendu () :
    # 1er étape
    mot_final = ""
    vies = 6
    mots = ["python", "chat", "chien", "poule", "poisson"]
    lettres_essayees = []
    mot = random.choice(mots)
    list_mot = ['_' for i in range(len(mot))]

    #2ème étape
    while '_' in list_mot and vies > 0 :
        lettre_joueur = input("Entrer une lettre : ").lower()

        if len(lettre_joueur) != 1 or not lettre_joueur.isalpha():
            print("Entrez une seule lettre !")
            continue

        if lettre_joueur in lettres_essayees :
            print("Lettre déjà essayé\n")
            continue

        if lettre_joueur in mot :
            lettres_essayees.append(lettre_joueur)
            print("Vous avez trouvé une lettre !")
            for i in range(len(mot)) :
                if mot[i] == lettre_joueur :
                    list_mot[i] = lettre_joueur
            print("Voici le résultat actuel",' '.join(list_mot))

        else :
            lettres_essayees.append(lettre_joueur)
            print("Cette lettre n'est pas dans le mot à déviner")
            vies -= 1

        print("Il vous reste", vies, "vies.\n")
        print("Lettres essayées :", lettres_essayees)

    #3ème étape
    if vies == 0 and '_' in list_mot :
        print("Vous avez perdu")
    else :
        mot_final = ''.join(list_mot)
        if mot_final == mot :
            print("Vous avez gagné" )
            print("le mot à déviner était :", mot)




jeu_pendu()






