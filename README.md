# Morpion

INTRODUCTION

Comme vous le connaissez déjà surement, ce doux jeu que l'on nomme Morpion est aussi ludique que stratégique et nous plonge dans l'anticipation du jeu de l'adversaire.

En effet, bien qu'il soit généralement composé d'une grille 3x3, nous l'avons voulu modulable par les joueurs, c'est d'ailleurs pourquoi il vous est possible de choisir le nombre de case de votre grille.
De même afin que les joueurs puissent sélectionner leur niveau de difficulté nous avons également inclus la sélection d'un nombre minimal d'alignement (il vous est conseillé de considérer des alignements supérieurs ou égaux à 3).

Nous avons souhaité réaliser un jeu accessible au plus grand nombre, c'est pourquoi un affichage est réalisé directement sur votre terminal, sous forme de grille, rendant la partie plus lisible et intéressante.



EXPLICATION DES FONCTIONS

Le code de notre jeu se compose de 4 fonctions:

La fonction format_grille(L), prend en argument une liste L, dans notre cas une grille, soit une liste de liste, et print chaque ligne de cette liste afin qu'une grille apparaisse dans le terminal.

La fonction creation_grille(n), est la fonction qui crée la grille. Elle prend en argument un entier n ,qui determine le nombre d'élément sur une ligne de la grille de sorte que la grille soit de taille n x n. Elle renvoie une Liste mais elle print une grille grâce à la fonction format_grille(n)

La fonction croix(L,numcase,lettre) modifie la grille remplaçant par le symbole du joueur la case sélectionné par ce dernier. Elle prend en argument une liste L, un numéro de case numcase (de type str) qui correspond au numéro de case où le joueur souhaite jouer et une lettre (de type str) qui correspond au symbole du joueur. Cette fonction renvoie la grille modifiée si la case est libre, sinon elle renvoie False, si elle est occupée ou qu'elle n'existe pas.

La fonction alignement_a(L,lettre,a) permet de déterminer si a symboles sont alignés dans la grille. Elle prend en argument une liste L, une lettre correspondant au symbole du joueur et un entier a qui correspond au nombre d'alignement choisi au début par les joueurs. Elle renvoie True si a symboles sont alignés et False sinon.



BOUCLE DE JEU

Notre boucle de jeu est composée d'une suite de "input" dont les réponses sont stockés dans des variables. Au début état='perdant', puis état='gagnant' si l'un des deux deux joueurs gagne la partie.
La grande boucle while représente la boucle de jeu qui s'arrête s'il y a eu une victoire ou un match nul. On initialise les différents paramètres permettant de créer la grille G, d'un nombre de cases n x n, d'alignements a. Puis on demande son symbole au premier joueur et on le fait jouer. On fait de même pour le second.
La boucle while imbriquée permet de créer la vraie boucle, tant qu'il n'y a aucun alignement elle tourne. Si un joueur souhaite placer sa croix ou son rond à un emplacement déjà occupé ou à une case inexistante, le jeu renvoie un message d'erreur et demande au joueur de choisir une nouvelle case. 

A la fin, le programme vérifie lequel des joueurs a gagné et renvoie un message au vainqueur ou dans le cas contraire, un message indiquant un match nul.


#A ajouter
Les différentes étapes de votre reflexion pour faire le projet

