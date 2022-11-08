from random import *
print('Bonjour bienvenue dans pierre feuille ciseau')
nom_joueur = input('Veuillez entrer votre nom')
print('choisissez ce que vous voulez jouer pierre 1 feuille 2 ciseau 3')
choix_joueur = input('Entrez un numéro')
choix_joueur = int(choix_joueur)
print('Vous avez choisi',choix_joueur)
print('lordinateur choisi à son tour')
choix_ordinateur = randint(1,3)
choix_ordinateur = int(choix_ordinateur)
print('lordinateur a choisi',choix_ordinateur)

if (choix_joueur == choix_ordinateur):
    print('égalité')
elif (choix_joueur == 1) and (choix_ordinateur == 3):
    print(nom_joueur,'gagne')
elif (choix_joueur == 3) and (choix_ordinateur == 1):
    print('Ordinateur a gagné')
elif (choix_joueur == 1) and (choix_ordinateur == 2):
    print('Ordinateur gagne')
elif (choix_joueur == 2) and (choix_ordinateur == 1):
    print('Ordinateur gagne')
elif (choix_joueur == 3) and (choix_ordinateur == 2):
    print(nom_joueur,'gagne')
elif(choix_joueur == 2) and (choix_ordinateur == 3):
    print('Ordinateur gagne')


