#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 17:47:15 2020

@author: maiavignal
"""

#sélection des case par numéro
#création de liste


def creation_grille(n):
    Liste=[]
    case=[]
    c=0
    for i in range(n):
        for j in range(n):
            c+=1
            if c<=9:
                case.append(' '+str(c))
            else:
                case.append(str(c))
        Liste.append(case)
        case=[]
    print(format_grille(Liste))
    return Liste

# def croix2(L,ligne,colonne,lettre):
#     n=len(L)
#     if L[ligne][colonne]!='.':
#         print("Cette case est déjà occupée par votre adversaire.")
#         return False
#     elif ligne>=n or colonne>=n:
#         print("Cette case n'existe pas dans la grille actuelle")
#         return False
#     else:
#         L[ligne][colonne]=lettre
    
#     return format_grille(L)

def croix(L,numcase,lettre):
    n=len(L)
    for i in range(n):
        for j in range(n):
            if L[i][j]==' '+numcase or L[i][j]==numcase:
                L[i][j]=' '+lettre
                return format_grille(L)
            
    return False
    

def alignement_a(L,lettre,a):
    """fonction qui retourne s'il y a un alignement de a éléments dans la grille"""
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

    #breakpoint()

    for j in range(n):#colonne
        for i in range(n-1):  #ligne      
            if L[i][j]==' '+lettre and L[i][j]==L[i+1][j]:
                p+=1
        if p+1>=a:
            return True
        else:
            p=0    
            
    #alignement sur diagonale haut gauche bas droite
            
    for i in range(n):
        if L[i][i]==' '+lettre and L[i][i]==L[i+1][i+1]:
            p+=1
    if p+1>=a:
        return True
    else:
        p=0   
    #alignement sur diagonale haut gauche bas droite

                
    for i, j in zip(range(n), range(1,n+1)):
        if L[i][n-j]==' '+lettre:
            p+=1
    if p+1>=a:
        return True
    else:
        p=0    
    return False

def alignement(L,lettre):
    """fonction qui retourne s'il y a un alignement de n éléments dans la grille"""
    n=len(L)
    p=0
    #alignement sur ligne
    for i in range(n):
        for x in L[i]:
            if x==lettre:
                p+=1
        if p==n:
            return True
        else:
            p=0
    #alignement sur colonne

    #breakpoint()

    for j in range(n):#colonne
        for i in range(n):  #ligne      
            if L[i][j]==lettre:
                p+=1
        if p==n:
            return True
        else:
            p=0    
            
    #alignement sur diagonale haut gauche bas droite
            
    for i in range(n):
        if L[i][i]==lettre  :
            p+=1
    if p==n:
        return True
    else:
        p=0   
    #alignement sur diagonale haut gauche bas droite

                
    for i, j in zip(range(n), range(1,n+1)):
        if L[i][n-j]==lettre:
            p+=1
    if p==n:
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
    G=creation_grille(n)
    
    a=int(input("Quel nombre d'alignement minimal choisissez-vous?:"))
    ##premier jeu du joueur 1
    
          
    lettre1=input("Vous serez le joueur 1 .\nIndiquez votre symbole pour cette partie:")
    numcase=input('''Indiquez le numéro de la case où vous souhaitez jouer:''')


    #boucle vérifiant que la case n'est pas déjà prise
    while croix(G,numcase,lettre1)==False:
            print("Cette case n'existe plus ou pas dans la grille actuelle")

            numcase=input('''Indiquez le numéro de la nouvelle case où vous souhaitez jouer:''')

        
    #croix(G,numcase,lettre1)

    #premier jeu joueur 2
    
    lettre2=input("Vous serez le joueur 2 .\nIndiquez votre symbole pour cette partie:")
    numcase=input('''Indiquez le numéro de la case où vous souhaitez jouer:''')

    
    while croix(G,numcase,lettre2)==False:
        print("Cette case n'existe plus ou pas dans la grille actuelle")

        numcase=input('''Indiquez le numéro de la nouvelle case où vous souhaitez jouer:''')

        

    
    croix(G,numcase,lettre2)
    

    i=2
    
    while alignement_a(G,lettre1,a)!=True and alignement_a(G,lettre2,a)!=True and i!=n*n:
        
        #joueur 1
        numcase=input('''Indiquez le numéro de la case où vous souhaitez jouer:''')
    
        while croix(G,numcase,lettre1)==False:
            print("Cette case n'existe plus ou pas dans la grille actuelle")

            numcase=input('''Indiquez le numéro de la nouvelle case où vous souhaitez jouer:''')


        
        croix(G,numcase,lettre1)
        i+=1
        #joueur2
        if i!=n*n and alignement_a(G,lettre1,a)!=True:

            numcase=input('''Indiquez le numéro de la case où vous souhaitez jouer:''')

            while  croix(G,numcase,lettre2)==False:
                print("Cette case n'existe plus ou pas dans la grille actuelle")

                numcase=input('''Indiquez le numéro de la case où vous souhaitez jouer:''')

            croix(G,numcase,lettre2)
        
            i+=1
    Etat='gagnant'
    
if alignement_a(G,lettre1,a)==True:
    print("Félicitations Joueur 1, vous avez gagné !")
    
elif alignement_a(G,lettre2,a)==True:
    print("Félicitations Joueur 1, vous avez gagné !")

else:
    print("Match nul!\n Qui souhaite prendre sa revanche?")


