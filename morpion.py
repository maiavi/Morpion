from tkinter import *

def interfacegraphique():
# Variables globales
    cases=[ [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    player = True                     # True pour les croix, False pour les ronds
    t = 1                              # Numéro du tour de jeu
    lignes = []                          #permet la creation des lignes et colonnes            


    ##Définition des Fonctions ##
    def afficher(event) :
        """ event -> Un événement de la souris
            but de la fonction: Affiche  les coordonnées de la case du clic de souris"""
        global player, cases, t
        l = (event.y-2)//100                    # Ligne du clic
        c = (event.x-2)//100                    # Colonne du clic

        if (t < 10) and (cases[l][c] == 0):
            if player:                              # player == True==croix
                dessin.create_line(100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, fill = 'red')
                dessin.create_line(100*c+8, 100*l+96, 100*c+96, 100*l+8, width = 5, fill = 'red')
                cases[l][c] = 1
                message.configure(text='Tour du joueur 2')

            else:
                dessin.create_oval(100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, outline = 'blue')
                cases[l][c] = -1
                message.configure(text='Tour du joueur 1')

            player = not(player)
            if (t >= 5) and (t <= 9):
                somme = alignement(cases)
                if somme == 1 or somme == -1:
                    t = vainqueur(somme)
                elif t == 9:
                    t = vainqueur(0)
            t += 1


    def alignement(tableau):
        """ tableau-> un tableau format n=3""
            but da la fonction: Calcule les sommes de chaque ligne/colonne/diagonale
                et vérifie leur alignement."""
        sommes = [0,0,0,0,0,0,0,0]            
        # Les lignes :
        sommes[0] = sum(tableau[0])
        sommes[1] = sum(tableau[1])
        sommes[2] = sum(tableau[2])
        # Les colonnes
        sommes[3] = tableau[0][0]+tableau[1][0]+tableau[2][0]
        sommes[4] = tableau[0][1]+tableau[1][1]+tableau[2][1]
        sommes[5] = tableau[0][2]+tableau[1][2]+tableau[2][2]
        # Les diagonales
        sommes[6] = tableau[0][0]+tableau[1][1]+tableau[2][2]
        sommes[7] = tableau[0][2]+tableau[1][1]+tableau[2][0]

        for i in range(8):                     # Parcours des sommes
            if sommes[i] == 3:
                return 1
            elif sommes[i] == -3:
                return -1
        return 0



    def vainqueur(a):
        """indique le vainqueur en modifiant le message."""
        if a == 1:
            message.configure(text = 'Joueur 1 a gagné !')
        elif a == -1:
            message.configure(text = 'Joueur 2 a gagné !')
        elif a == 0:
            message.configure(text = 'Match nul !')
        return 9



    def reinit():
        """on ré-initialise les variables globales."""
        global player, cases, t
        cases = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        player= True          # True pour les croix, False pour les ronds
        t = 1

        message.configure(text='Tour du joueur 1')
        dessin.delete(ALL)      # Efface le jeu précedent 
        lignes = []
        for i in range(4):
            lignes.append(dessin.create_line(0, 100*i+2, 303, 100*i+2, width=3))
            lignes.append(dessin.create_line(100*i+2, 0, 100*i+2, 303, width=3))



    #Fenêtres
    fen = Tk()
    fen.title('Morpion')
    #zones de texte
    message=Label(fen, text='Tour du joueur 1')
    message.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3, sticky = W+E)
    #boutons
    bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
    bouton_quitter.grid(row = 2, column = 1, padx=3, pady=3, sticky = S+W+E)

    bouton_reload = Button(fen, text='Recommencer', command=reinit)
    bouton_reload.grid(row = 2, column = 0, padx=3, pady=3, sticky = S+W+E)

    #Création du canevas
    dessin=Canvas(fen, bg="white", width=301, height=301)
    dessin.grid(row = 1, column = 0, columnspan = 2, padx=5, pady=5)

    dessin.bind('<Button-1>', afficher)
    ## lancement du jeu
    reinit()
    fen.mainloop()     

def format_grille(L):
    """renvoie les éléments de la liste L"""
    for x in L:
        print(x)

#on crée une grille de numéro afin de permettre au joueur de visualiser les cases et leur numéro 
def creation_grille(n):
    """création d'une grille de taille n x n, contenant le numéro des cases"""
    Liste=[]
    case=[]
    c=0 
    for i in range(n):
        for j in range(n):
            c+=1
                #la distinction entre c<=9 et c>9 est réalisé par soucis de lisibilité dans la grille car un nombre à deux chiffres prends la place de deux caractères 
            if c<=9:
                case.append(' '+str(c))
            else:
                case.append(str(c))
        Liste.append(case)
        case=[]
    print(format_grille(Liste))
    return Liste

def grille_vide(n):
    """création d'une seconde grille, vide cette fois-ci, qui est la grille de jeu"""
    case2=[]
    grille=[]
    for i in range(n):
        for j in range(n):
            case2.append('  ')

        grille.append(case2)
        case2=[]
    print(format_grille(grille))
    return grille




def croix(L,G,numcase,lettre):
    """vérifie l'emplacement de la case dans la grille L, vide la case correspondante dans L, et remplit avec le symbole du joueur la case correspondante dans G"""
    n=len(L)
    for i in range(n):
        for j in range(n):
            if L[i][j]==' '+numcase or L[i][j]==numcase:
                L[i][j]='  '
                G[i][j]=' '+lettre
                print(format_grille(L))
                return format_grille(G)
    return False
    

def alignement_a(G,lettre,a):
    """fonction qui retourne s'il y a un alignement de a éléments ou plus dans la grille G de jeu"""
    n=len(G)
    p=0 #le compteur d'alignement 

    #alignement sur ligne
    for i in range(n):
        for j in range(n-1):
            if G[i][j]==' '+lettre and G[i][j]==G[i][j+1]:
                p+=1
        if p+1>=a:
            return True
        else:
            p=0
    
    #alignement sur colonne

    for j in range(n):#colonne
        for i in range(n-1):  #ligne      
            if G[i][j]==' '+lettre and G[i][j]==G[i+1][j]:
                p+=1
        if p+1>=a:
            return True
        else:
            p=0    
            
    #alignement sur diagonale de gauche à droite

    for i, j in zip(range(n-1), range(n-1)):
            if G[i][j]==' '+lettre and G[i][j]==G[i+1][j+1]:
                p+=1
    if p+1>=a:
        return True
    else:
        p=0  


    #alignement sur diagonale au dessus de la diagonale de gauche à droite
    for i, j in zip(range(n-2), range(1,n-1)):
            if G[i][j]==' '+lettre and G[i][j]==G[i+1][j+1]:
                p+=1
    if p+1>=a:
        return True
    else:
        p=0

    #alignement sur diagonale en dessous de la diagonale de gauche à droite
    for i, j in zip(range(1,n-1), range(n-2)):
            if G[i][j]==' '+lettre and G[i][j]==G[i+1][j+1]:
                p+=1
    if p+1>=a:
        return True
    else:
        p=0

    #alignement sur diagonale de droite à gauche


    for i, j in zip(range(0,n), range(n-1,0,-1)): # on réalise une boucle for croissante sur i et une décroissante sur j,; le "zip range" permet d'incrémenter ou de décrémùenter les variables i et j en même temps
        if G[i][j]==' '+lettre and G[i][j]==G[i+1][j-1]:
            p+=1
    if p+1>=a:
        return True
    else:
           p=0 

    #alignement sur diagonale au dessus de la diagonale de droite à gauche
    for i, j in zip(range(0,n-1), range(n-2,0,-1)):
        if G[i][j]==' '+lettre and G[i][j]==G[i+1][j-1]:
            p+=1
    if p+1>=a:
        return True
    else:
           p=0 
   



    #alignement sur diagonale en dessous de la diagonale de droite à gauche
    for i, j in zip(range(1,n), range(n-1,1,-1)):
        if G[i][j]==' '+lettre and G[i][j]==G[i+1][j-1]:
            p+=1
    if p+1>=a:
        return True
    else:
           p=0
     

    return False




        
##boucle de jeu

Etat='perdant'

while Etat=='perdant':

    #initialisation des grilles
    n = int(input("Bienvenue dans le Super Morpion 2020.\nEntrez le nombre de case n que vous souhaitez avoir sur une ligne, de votre grille de taille n x n : n="))

    if n==3:
        réponse=input("Vous souhaitez jouer sur le terminal (T) ou sur l'interface graphique (IG) ? (écrivez T ou IG):")
        if réponse=="IG":
            interfacegraphique()
            Etat='gagnant'

    #jeu sur le terminal
    L=creation_grille(n)
    G=grille_vide(n)
    a=int(input("Quel nombre d'alignement minimal choisissez-vous?(égal à "+str(n)+ " ou à "+str(n-1)+")):"))
    #boucle while au cas où si le joueur sélectionne un alignement autre que a ou a-1
    while a!=int(str(n)) and a!=int(str(n))-1:
        print ("Vous devez sélectionner un nombre d'alignement égal à "+str(n)+" ou "+str(n-1))

        a=int(input("Quel nombre d'alignement minimal choisissez-vous?(égal à "+str(n)+ " ou à "+str(n-1)+")):"))

    #premier jeu du joueur 1
    
    NomJoueur1=input("Vous serez le joueur 1 .\nQuel est votre nom:")
    lettre1=input("Indiquez votre symbole pour cette partie (entrez X ou O):")
    while lettre1!="X" and lettre1!="O":
        lettre1=input("Votre symbole doit être soit X, soit O ( entrez X ou O):")

    numcase=input(NomJoueur1 + ''', indiquez le numéro de la case où vous souhaitez jouer:''')


    #boucle vérifiant que la case n'est pas déjà prise
    while croix(L,G,numcase,lettre1)==False:
            print("Cette case n'existe plus ou pas dans la grille actuelle")

            numcase=input('''Indiquez le numéro de la nouvelle case où vous souhaitez jouer:''')

        

    #premier jeu joueur 2

    #on déduit du symbole du joueur 1 le symbole du joueur 2
    NomJoueur2=input("Vous serez le joueur 2 .\nQuel est votre nom ?")
    if lettre1=='X':
        lettre2='O'
    else:
        lettre2='X'

    
    numcase=input(NomJoueur2+''', indiquez le numéro de la case où vous souhaitez jouer:''')

    while croix(L,G,numcase,lettre2)==False:
        print("Cette case n'existe plus ou pas dans la grille actuelle")

        numcase=input(NomJoueur2+''', indiquez le numéro de la nouvelle case où vous souhaitez jouer:''')

    croix(L,G,numcase,lettre2)
    

    i=2
    
    
    #cette boucle vérifie qu'aucun des deux joueurs n'a gagné et que i, qui est le compteur du nombre de jeux, est différent de la somme de toutes les cases, c'est à dire pas de match nul
    while alignement_a(G,lettre1,a)!=True and alignement_a(G,lettre2,a)!=True and i!=n*n:
        
        #joueur 1
        numcase=input(NomJoueur1+''', indiquez le numéro de la case où vous souhaitez jouer:''')
    
        while croix(L,G,numcase,lettre1)==False:
            print("Cette case n'existe plus ou pas dans la grille actuelle")

            numcase=input(NomJoueur1+''', indiquez le numéro de la nouvelle case où vous souhaitez jouer:''')


        
        croix(L,G,numcase,lettre1)
        i+=1
        #joueur2
        if i!=n*n and alignement_a(G,lettre1,a)!=True:

            numcase=input(NomJoueur2+''', indiquez le numéro de la case où vous souhaitez jouer:''')

            while  croix(L,G,numcase,lettre2)==False:
                print("Cette case n'existe plus ou pas dans la grille actuelle")

                numcase=input(NomJoueur2+''', indiquez le numéro de la case où vous souhaitez jouer:''')

            croix(L,G,numcase,lettre2)
        
            i+=1
    
    if alignement_a(G,lettre1,a)==True:
        print("Félicitations "+NomJoueur1+", vous avez gagné !")
    
    elif alignement_a(G,lettre2,a)==True:
        print("Félicitations "+NomJoueur2+", vous avez gagné !")

    elif i==n*n:
        print("Match nul!")
    
    replay=input("Souhaitez-vous rejouer? (entrez oui ou non) ")
    
    if replay=="non":
        Etat='gagnant'
