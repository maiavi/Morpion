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
    if n<3:
        return
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
    p=0
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
            
    #alignement sur diagonale haut gauche bas droite
            
    for i in range(n-1):
        for j in range(n-1):
            if G[i][j]==' '+lettre and G[i][j]==G[i+1][j+1]:
                p+=1
    if p+1>=a:
        return True
    else:
        p=0   
    
    #alignement sur diagonale haut gauche bas droite

    
    for i, j in zip(range(0,n-1), range(a,n-1)):
            if G[i][n-j]==' '+lettre and G[i][n-j]==G[i+1][n-j-1]:
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
    L=creation_grille(n)
    G=grille_vide(n)
    a=int(input("Quel nombre d'alignement minimal choisissez-vous?(inférieur ou égal à "+str(n)+"):"))
    
    #premier jeu du joueur 1
    
    NomJoueur1=input("Vous serez le joueur 1 .\nQuel est votre nom:")
    lettre1=input("Indiquez votre symbole pour cette partie (X ou O):")
    numcase=input('''Indiquez le numéro de la case où vous souhaitez jouer:''')


    #boucle vérifiant que la case n'est pas déjà prise
    while croix(L,G,numcase,lettre1)==False:
            print("Cette case n'existe plus ou pas dans la grille actuelle")

            numcase=input('''Indiquez le numéro de la nouvelle case où vous souhaitez jouer:''')

        
    #croix(G,numcase,lettre1)

    #premier jeu joueur 2
    NomJoueur2=input("Vous serez le joueur 2 .\nQuel est votre nom ?")
    if lettre1=='X':
        lettre2='O'
    else:
        lettre2='X'

    #lettre2=input("Indiquez votre symbole pour cette partie (X ou O):")
    
    numcase=input('''Indiquez le numéro de la case où vous souhaitez jouer:''')

    
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
    Etat='gagnant'
    
if alignement_a(G,lettre1,a)==True:
    print("Félicitations "+NomJoueur1+", vous avez gagné !")
    
elif alignement_a(G,lettre2,a)==True:
    print("Félicitations "+NomJoueur2+", vous avez gagné !")

else:
    print("Match nul!")
