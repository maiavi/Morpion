# Morpion


Comme vous le connaissez surement déjà, ce palpitant jeu que l'on nomme Morpion aussi ludique que stratégique, nous plonge dans l'art de l'anticipation depuis notre plus tendre enfance.
Bien qu'il soit généralement composé d'une grille 3x3, le Super Morpion 2020 se veut modulable par les joueurs, c'est donc la raison pour laquelle il vous est possible de choisir le nombre de cases de votre grille dès le début du jeu (pour une grille n x n, 2<n<10 pour faciliter la lecture du jeu ).
De même, pour que les joueurs puissent gérer leur niveau de difficulté nous avons également inclus la sélection d'un nombre minimal d'alignement (il vous est demandé de choisir des alignements égaux ou inférieurs de 1 à la taille d'une ligne ).

Nous avons souhaité réaliser un jeu accessible, c'est pourquoi un affichage sous forme de grille est réalisé directement sur votre terminal. De plus pour les grille de taille 3x3, il est possible d'afficher une interface graphique.




EXPLICATION DES FONCTIONS

Le code du jeu se compose de 5 fonctions:

La fonction format_grille(L), prend en argument une liste L, dans notre cas une grille, soit une liste de liste, et print chaque ligne de cette liste afin qu'une grille apparaisse dans le terminal.

La fonction creation_grille(n), est la fonction qui crée une grille de référence  contenant les numéros des cases dans lesquelles le joueur peut jouer . Elle prend en argument un entier n ,qui détermine le nombre d'élément sur une ligne de la grille de sorte que la grille soit de taille n x n. Cette fonction renvoie une liste de n-liste de n-éléments mais elle print une grille grâce à la fonction format_grille(L).

La fonction grille_vide(n), prend en argument un entier n et crée une grille vide qui sera la grille de jeu. Elle renvoie aussi une liste de n-liste de chacune n-éléments comme creation_grille(n) et apparait sous forme de grille grâce à la fonction format_grille(L).


La fonction croix(L,G,numcase,lettre) modifie la grille L en y supprimant le numéro dans la case correspondante à numcase et modifie la grille G en remplaçant par le symbole du joueur la case correspondante. Elle prend en argument une liste L, une liste G, un numéro de case numcase (de type str) qui correspond au numéro de case où le joueur souhaite jouer et une lettre qui correspond au symbole du joueur. Cette fonction renvoie la grille modifiée si la case est libre, sinon elle renvoie False, c'est à dire si cette case est occupée ou qu'elle n'existe pas.

La fonction alignement_a(L,lettre,a) permet de déterminer si a-symboles sont alignés dans la grille(sur les lignes, les colonnes, les 2 diagonales centrales, et les diagonales supérieure et inférieures au diagonales centrales). Elle prend en argument une liste L, la lettre correspondant au symbole du joueur et un entier a qui correspond au nombre d'alignement choisi au début par les joueurs. Elle renvoie True si a-symboles sont alignés et False sinon. Remarque: a est égal à len(L) ou len(L)-1).





INTERFACE DE JEU

Nous avons créer une interface graphique pour les joueurs, ils peuvent faire le choix de l'utiliser ou de jouer sur le terminal de l'ordinateur. Cette interface est disponible uniquement pour un jeu de taille 3 x 3. 

FONCTIONNEMENT DE L'INTERFACE 

Pour créer cette interface on s'est appuyé sur le module tkinter, notre dispositif est composé en trois grandes parties :

  1) La création de variables globales qui composent les différentes cases, les joueurs, le numéro de tour de jeu et les lignes ;
  
  2) La definition des différentes fonctions auxquelles on va faire appel à : 
  
   La fonction afficher(event) qui a pour but d'afficher les coordonnées de la case sur laquelle la souris a cliqué.
Par la suite, elle permet de créer les croix et les ronds en jouant sur les coordonnées des lignes et des colonnes definies grâces à l'outil dessin.create_line à condition que le tour de jeu soit inférieur à 10.  
La fonction intègre une boucle conditionnelle qui au bout du 5ème tour identifie le perdant et le gagnant en s'appuyant sur les fonctions alignemment(tableau) et vainqueur(a).
                                                                            
                                                                            
   La fonction alignement(tableau) permet d'identifier les différents alignements effectués par nos joueurs (diagonales, colonnes et lignes) et calcule leurs sommes. Lorsque celle-ci est égal à 3 ( c'est-à-dire que trois croix sont alignées), la fonction retourne 1, tandis qu'elle vaut -1 si les ronds sont alignés, 0 sinon.  

   La fonction vainqueur(a) quant à elle prend en argument la somme calculée par la fonction alignement et affiche le vainqueur grâce à l'outil, message.configure (text = 'Joueur x a gagné !'). Lorsque a est égal à zéro on est face à un match nul.

   La fonction reinit() permet de réinitialiser nos variables globales et d'effacer l'ensemble du jeu précédent, dessin.delete(ALL), puis reconstruit une liste composée des lignes et colonnes du jeu.

   
  3) La création de notre fenêtre de jeu : avec affichage d'un message pour les tours des joueurs, construction des boutons "quitter" et "recommencer", création de grilles et colonnes du jeu.





BOUCLE DE JEU

Notre boucle de jeu est composée d'une suite de "input" dont les réponses sont stockés dans des variables. Au début état='perdant', puis état='gagnant' si l'un des deux deux joueurs gagne la partie.
La grande boucle while représente la boucle de jeu qui s'arrête s'il y a eu une victoire ou un match nul. 
On initialise les différents paramètres permettant de créer les grille L (non vide) et G (vide), le nombre de cases n x n, l'alignement minimal a. Puis on demande son nom et son symbole au premier joueur et on le fait jouer. On fait de même pour le second joueur en déduisant du choix de X ou O du joueur 1, le symbole du joueur 2.
La boucle while imbriquée permet de créer la vraie boucle de jeu qui tourne tant qu'il n'y a aucun alignement ou qu'il n'y a pas de match nul. 
Si un joueur souhaite placer sa croix ou son rond à un emplacement déjà occupé ou à une case inexistante, le jeu renvoie un message d'erreur et demande au joueur de choisir une nouvelle case. Un compteur i permet de gérer l'éventualité d'un match nul.

A la fin, le programme vérifie lequel des joueurs a gagné et renvoie un message au vainqueur s'il y a eu une victoire. Sinon, il renvoie un message indiquant un match nul.
Les joueurs ont également la possibilité de rejouer sans avoir à relancer le fichier .py .
