#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 17:47:15 2020

@author: maiavignal
"""

#on crée une grille de numéro afin de permettre au joueur de visualiser les cases et leur numéro 
def creation_grille(n):
    Liste=[]
    case=[]
    c=0  
    for i in range(n):
        for j in range(n):
            c+=1
            #la distinction entre c<=9 et c>9 est réalisé par soucis de lisibilité dans la grille car un nombre à deux chiffres prends la place de deux caractères, 
            if c<=9:
                case.append(' '+str(c))
            else:
                case.append(str(c))
        Liste.append(case)
        case=[]
    print(format_grille(Liste))
    return Liste
#création d'une seconde grille, vide cette fois-ci, qui est la grille de jeu
def grille_vide(n):
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
    """vérifie l'emplacement de la case dans la grille L, vide la case correspondante de L, et remplit avec le symbole du joueur la case correspondante dans G"""
    n=len(L)
    for i in range(n):
        for j in range(n):
            if L[i][j]==' '+numcase or L[i][j]==numcase:
                L[i][j]='  '
                G[i][j]=' '+lettre
                print(format_grille(L))
                return format_grille(G)
    return False
    

def alignement_a(L,lettre,a):
    """fonction qui retourne s'il y a un alignement de a éléments dans la grille G"""
    n=len(L)
    p=0
    #alignement sur ligne
    for i in range(n):
        for j in range(n-1):
            if L[i][j]==' '+lettre and L[i][j]==L[i][j+1]:
                p+=1
        if p+1>=a:
            return True
        else:
            p=0
    #alignement sur colonne


    for j in range(n):#colonne
        for i in range(n-1):  #ligne      
            if L[i][j]==' '+lettre and L[i][j]==L[i+1][j]:
                p+=1
        if p+1>=a:
            return True
        else:
            p=0    
            
    #alignement sur diagonale haut gauche bas droite
            
    for i in range(n-1):
        for j in range(n-1):
            if L[i][j]==' '+lettre and L[i][j]==L[i+1][j+1]:
                p+=1
    if p+1>=a:
        return True
    else:
        p=0   
    
    #alignement sur diagonale haut gauche bas droite

    
    for i, j in zip(range(0,n-1), range(a,n-1)):
            if L[i][n-j]==' '+lettre and L[i][n-j]==L[i+1][n-j-1]:
                p+=1
    if p+1>=a:
        return True
    else:
        p=0 

    return False



def format_grille(L):
    for x in L:
        print(x)
        
##boucle de jeu

Etat='perdant'

while Etat=='perdant':
    
    n = int(input("Bienvenue dans le super-morpion-2020.\nEntrez le nombre case n x n de la grille:"))
    L=creation_grille(n)
    G=grille_vide(n)
    a=int(input("Quel nombre d'alignement minimal choisissez-vous?(inférieur ou égal à "+str(n)+"):"))
    ##premier jeu du joueur 1
    
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


