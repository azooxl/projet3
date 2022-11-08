plateau = [["-","-","-"], ["-","-","-"], ["-","-","-"]]
running = True
def aff_tableau():
    for o in range(len(plateau)):
        for l in range(len(plateau[o])):
            print(plateau[o][l], end=' ')
        print()

def victoire_1():
    if plateau [0][0] == 'X' and plateau [0][1] == 'X' and plateau [0][2] == 'X':
        print(joueur1,'a gagné la partie')
        return running == False
    elif  plateau [1][0] == 'X' and plateau [1][1] == 'X' and plateau [1][2] == 'X':
        print(joueur1,'a gagné la partie')
        return running == False
    elif  plateau [2][0] == 'X' and plateau [2][1] == 'X' and plateau [2][2] == 'X':
        print(joueur1,'a gagné la partie')
        return running == False
    elif  plateau [0][0] == 'X' and plateau [1][0] == 'X' and plateau [2][0] == 'X':
        print(joueur1,'a gagné la partie')
        return running == False
    elif  plateau [0][1] == 'X' and plateau [1][1] == 'X' and plateau [2][1] == 'X':
        print(joueur1,'a gagné la partie')
        return running == False
    elif  plateau [0][2] == 'X' and plateau [1][2] == 'X' and plateau [2][2] == 'X':
        print(joueur1,'a gagné la partie')
        return running == False
    elif  plateau [0][0] == 'X' and plateau [1][1] == 'X' and plateau [2][2] == 'X':
        print(joueur1,'a gagné la partie')
        return running == False
    elif  plateau [0][2] == 'X' and plateau [1][1] == 'X' and plateau [2][0] == 'X':
        print(joueur1,'a gagné la partie')
        return running == False

def victoire_2():
    if plateau [0][0] == 'O' and plateau [0][1] == 'O' and plateau [0][2] == 'O':
        print(joueur2,'a gagné la partie')
        return running == False
    elif  plateau [1][0] == 'O' and plateau [1][1] == 'O' and plateau [1][2] == 'O':
        print(joueur2,'a gagné la partie')
        return running == False
    elif  plateau [2][0] == 'O' and plateau [2][1] == 'O' and plateau [2][2] == 'O':
        print(joueur2,'a gagné la partie')
        return running == False
    elif  plateau [0][0] == 'O' and plateau [1][0] == 'O' and plateau [2][0] == 'O':
        print(joueur2,'a gagné la partie')
        return running == False
    elif  plateau [0][1] == 'O' and plateau [1][1] == 'O' and plateau [2][1] == 'O':
        print(joueur2,'a gagné la partie')
        return running == False
    elif  plateau [0][2] == 'O' and plateau [1][2] == 'O' and plateau [2][2] == 'O':
        print(joueur2,'a gagné la partie')
        return running == False
    elif  plateau [0][0] == 'O' and plateau [1][1] == 'O' and plateau [2][2] == 'O':
        print(joueur2,'a gagné la partie')
        return running == False
    elif  plateau [0][2] == 'O' and plateau [1][1] == 'O' and plateau [2][0] == 'O':
        print(joueur2,'a gagné la partie')
        return running == False
joueur1 = input("Qui est le premier joueur?")
joueur2 = input("Qui est le second joueur?") 

def check1(user):
    play= input(user+" joue (ligne puis colonne séparer par un espace entre les deux chiffres) : ")
    while len(play) > 3 or len(play) < 3 :
        print("Choisir un chiffre entre 1 et 3 pour la ligne et la colonne, les deux séparés d'un espace\n")
        play= input(user+" joue (ligne puis colonne séparés par un espace entre les deux chiffres) : ")
    while play != "1 1" and play != "1 2" and play != "1 3" and play !=  "2 1" and play !=  "2 2" and play !=  "2 3" and play !=  "3 1" and play != "3 2" and play != "3 3":
        print("Choisir deux chiffres compris entre 1 et 3  les deux séparés d'un espace\n")
        play = input(user+" joue (ligne puis colonne) : ")
    return play

while running != False:
            
        aff_tableau()
            
        jeu1, jeu2 = check1(joueur1).split()
        ligne1 = int(jeu1)
        colonne1 = int(jeu2)
        check = 1  
        while check == 1:
            if plateau[ligne1-1][colonne1-1] != "-":
                print("case déjà prise")
                jeu1, jeu2 = check1(joueur1).split()
                ligne1 = int(jeu1)
                colonne1 = int(jeu2)
            else:
                plateau[ligne1-1][colonne1-1] = "X"
                check = 2          
            aff_tableau()
            running = victoire_1()
            if running == False:
                break
            if "-" not in plateau[0][0] and "-" not in plateau[0][1] and "-" not in plateau[0][2] and "-" not in plateau[1][0] and "-" not in plateau[1][1] and "-" not in plateau[1][2] and "-" not in plateau[2][0] and "-" not in plateau[2][1] and "-" not in plateau[2][2]:
                print ("Match nul !")
                break

            jeu3, jeu4 = check1(joueur2).split()
            ligne2 = int(jeu3)
            colonne2 = int(jeu4)
            check = 1  
            while check == 1:
                if plateau[ligne2-1][colonne2-1] != "-":
                    print("ceci a déja été joué\n")
                    play3, play4 = check_input(joueur2).split()
                    ligne2 = int(jeu3)
                    colonne2 = int(jeu4)
                else:
                    plateau[ligne2-1][colonne2-1] = "O"
                    check = 2
            running = victoire_2()
            if running == False:
                break