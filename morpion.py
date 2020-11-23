#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 17:47:15 2020

@author: maiavignal
"""


#création de liste


def creation_grille(n):
    Liste=[]
    case=[]
    for i in range(n):
        for j in range(n):
            case.append('.')
           
        Liste.append(case)
        case=[]
    print(format_grille(Liste))
    return Liste

def croix(L,ligne,colonne,lettre):
    if L[ligne][colonne]!='.':
        return False
    else:
        L[ligne][colonne]=lettre
    
    return format_grille(L)




def alignement(L,lettre):
    """fonction qui retourne s'il y a un alignement de n éléments à la suite dans la grille"""
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
G=[]

while Etat=='perdant':
    
    n = int(input("Bienvenue dans le super-morpion-2020.\nEntrez le nombre case n x n de la grille:"))
    G=creation_grille(n)
    
    ##premier jeu du joueur 1
    
          
    lettre1=input("Vous serez le joueur 1 .\nIndiquez votre symbole pour cette partie:")
    
    ligne=int(input('''Où souhaitez vous jouer?\nEntrer la ligne ( la première ligne étant d'indice 0):'''))
    colonne=int(input('''Entrer la colonne ( la première colonne étant d'indice 0):'''))
    
    #boucle vérifiant que la case n'est pas déjà prise
    while croix(G,ligne,colonne,lettre1)==False:
        ligne=int(input("Cette case est déjà occupée par votre adversaire.\n Choisissez une autre ligne:"))
        colonne=int(input("Choisissez une autre colonne:"))
        
    croix(G,ligne,colonne,lettre1)

    #premier jeu joueur 2
    
    lettre2=input("Vous serez le joueur 2 .\nIndiquez votre symbole pour cette partie:")

    ligne=int(input('''Où souhaitez vous jouer?\nEntrer la ligne ( la première ligne étant d'indice 0):'''))
    colonne=int(input('''Entrer la colonne ( la première colonne étant d'indice 0):'''))
    
    while croix(G,ligne,colonne,lettre2)==False:
        ligne=int(input("Cette case est déjà occupée par votre adversaire.\n Choisissez une autre ligne:"))
        colonne=int(input("Choisissez une autre colonne:"))
        

    
    croix(G,ligne,colonne,lettre2)
    

    i=2
    
    while alignement(G,lettre1)!=True and alignement(G,lettre2)!=True and i!=n*n:
        
        #joueur 1
        ligne=int(input('''Joueur1 où souhaitez vous jouer?\nEntrer la ligne ( la première ligne étant d'indice 0):'''))
        colonne=int(input('''Entrer la colonne ( la première colonne étant d'indice 0):'''))
    
        while croix(G,ligne,colonne,lettre1)==False:
            ligne=int(input("Cette case est déjà occupée par votre adversaire.\nChoisissez une autre ligne:"))
            colonne=int(input("Choisissez une autre colonne:"))

        
        croix(G,ligne,colonne,lettre1)
        i+=1
        #joueur2
        if i!=n*n and alignement(G,lettre1)!=True:
            
            ligne=int(input('''Joueur 2 où souhaitez vous jouer?\nEntrer la ligne ( la première ligne étant d'indice 0):'''))
            colonne=int(input('''Entrer la colonne ( la première colonne étant d'indice 0):'''))
    
            while  croix(G,ligne,colonne,lettre2)==False:
                ligne=int(input("Cette case est déjà occupée par votre adversaire.\nChoisissez une autre ligne:"))
                colonne=int(input("Choisissez une autre colonne:"))

    
            croix(G,ligne,colonne,lettre2)
        
            i+=1
    Etat='gagnant'
    
if alignement(G,lettre1)==True:
    print("Félicitations Joueur 1, vous avez gagné !")
    
elif alignement(G,lettre2)==True:
    print("Félicitations Joueur 1, vous avez gagné !")

else:
    print("Match nul!\n Qui souhaite prendre sa revanche?")


