# Morpion

INTRODUCTION

Comme vous le connaissez déjà surement, ce doux jeu que l'on nomme Morpion, qui s'apprend dès le plus jeune âge à la récréation ou dans les salles de cours pour les moins concentrés, est aussi ludique que stratégique et nous plonge dans l'anticipation du jeu de l'adversaire.

En effet,bien qu'il soit généralement composé d'une grille 3x3, nous l'avons voulu modelable au goût des joueurs, c'est d'ailleurs pourquoi il vous est possible de choisir le nombre de case de votre grille.
De même afin que les joueurs puissent sélectionner leur niveau de difficulté nous avons également inclus la sélection d'un nombre minimal d'alignement (il vous est conseillé de considérer des alignements supérieurs ou égaux à 3).

Nous avons souhaité réaliser un jeu accessible au plus grand nombre, c'est pourquoi un affichage est réalisé directement sur votre terminal, sous forme de grille, rendant la partie plus lisible et intéressante.



EXPLICATION DES FONCTIONS

Le code de notre jeu se compose de 4 fonctions:

La fonction format_grille(L), prend en argument une liste L, dans notre cas une grille, soit une liste de liste, et print chaque ligne de cette liste afin qu'une grille apparaisse dans le terminal.

La fonction creation_grille(n), est la fonction qui crée la grille. Elle prend en argument un entier n ,qui determine le nombre d'élément sur une ligne de la grille de sorte que la grille soit de taille n x n. Elle renvoie une Liste mais elle print une grille grâce à la fonction format_grille(n)

La fonction croix(L,numcase,lettre) modifie la grille remplaçant par le symbole du joueur la case sélectionné par ce dernier. Elle prend en argument une liste L, un numéro de case numcase (de type str) qui correspond au numéro de case où le joueur souhaite jouer et une lettre (de type str) qui correspond au symbole du joueur. Cette fonction renvoie la grille modifiée si la case est libre, sinon elle renvoie False, si elle est occupée ou qu'elle n'existe pas.

La fonction alignement_a(L,lettre,a) permet de déterminer si a symboles sont alignés dans la grille. Elle prend en argument une liste L, une lettre correspondant au symbole du joueur et un entier a qui correspond au nombre d'alignement choisi au début par les joueurs. Elle renvoie True si a symboles sont alignés et False sinon.



BOUCLE DE JEU



Les différentes étapes de votre reflexion pour faire le projet
L'explication de chaque fonction(Plus global, seulement :- quels sont les arguments - qu'est-ce qu'elle renvoie)
Votre boucle de jeu etc

