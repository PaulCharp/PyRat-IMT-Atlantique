TEAM_NAME = "Orange"

##############################################################
# The turn function should always return a move to indicate where to go
# The four possibilities are defined here
##############################################################
#On lance le programme avec python PyRat.py --rat ../Perso/BFS.py -p 1 -md 0.0

MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'


import random
import sys
import numpy as np

#On definit une structure de queue

class Queue:

    def __init__(self):
        self.q = []

    def isEmpty(self):
        if self.q == [] :
            return True
        else :
            return False

    def pop(self):
        return self.q.pop()

    def push(self,a):
        self.q = [a]+self.q

#On creer une variable globale qui contiendrat toutes nos informations à propos de l'état actuel de nos stratégies de déplacement
class Moves:

    def __init__(self,maze_map):
        self.routingTable = {}
        indexKeys = [*maze_map]
        for key in indexKeys :
            self.routingTable[key]= None
        self.path = [] #Une pile qui contient le chemin qu'il reste a parcourir
        self.conversionDirection = {
            (1,0):'L',
            (-1,0):'R',
            (0,1):'D',
            (0,-1):'U'
        }

    def BFS(self, playerLocation, maze_map, pieces_of_cheese):
        #On commence la parcours en largeur de la position actuelle. On ajoute l'ensemble des sommets voisins dans la Queue
        queue = Queue()
        dejaVu = [] # la liste des sommets deja Vu
        queue.push(playerLocation)
        queue.q = [*maze_map[queue.pop()]]+queue.q #On ajoute l'ensemble des voisins a la Queue
        pos = playerLocation #La position que l'on regarde actuellement (pas forcément celle sur laquelle on est)
        while pos not in pieces_of_cheese :
            #On ajoute l'ensemble des voisins pas encore parcouru dans la Queue
            voisins = [*maze_map[pos]]
            for vois in voisins:
                if vois not in dejaVu:
                    dejaVu.append(vois)
                    queue.push(vois)
                    self.routingTable[vois]=pos
            if not queue.isEmpty():
                pos = queue.pop()
            else :
                #No more cheese in the labyrinth
                sys.exit('There is no more cheese in the lab')
                #En principe le jeu s'arrete tout seul
        #La position est donc dans les pieces_of_cheese
        #On va donc y aller, on renvoit la position target
        print(self.routingTable)
        return pos


    def makePath(self,playerLocation, maze_map,target): #retourne le chemin vers une cible donnee en utilisant routingTable
        #On deduit un chemin de la routingTable c'est une pile, on commence par la position où on veut aller
        #On parcours le dictionnaire routingTable
        pos = target
        while pos != playerLocation:
            self.path.append(self.conversionDirection[tuple(np.subtract(self.routingTable[pos],pos))]) #c'est toujours la position precedente - la target
            pos = self.routingTable[pos] #On prend la position parent

    def makeAChoice(self, playerLocation, maze_map, pieces_of_cheese):
        #C'est ici qu'on fait un choix pour chaque tour, ou bien on continue a chercher des fromages, ou bien on avance
        if self.path == []: #alors on cherche un autre fromage
            target = self.BFS(playerLocation, maze_map, pieces_of_cheese)
            #On a remplit le routingTable et on la target. On génère donc le chemin
            self.makePath(playerLocation, maze_map, target)
        #Ensuite on effectue un mouvement, on depile notre path
        return self.path.pop()


#On initialise nos variables globales
moves = None

##############################################################
# The preprocessing function is called at the start of a game
# It can be used to perform intensive computations that can be
# used later to move the player in the maze.
# ------------------------------------------------------------
# mazeMap : dict(pair(int, int), dict(pair(int, int), int))
# mazeWidth : int
# mazeHeight : int
# playerLocation : pair(int, int)
# opponentLocation : pair(int,int)
# piecesOfCheese : list(pair(int, int))
# timeAllowed : float
##############################################################

def preprocessing(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, piecesOfCheese, timeAllowed):
    global moves
    moves = Moves(mazeMap)
    return

def turn(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, playerScore, opponentScore, piecesOfCheese, timeAllowed):
    global moves
    return moves.makeAChoice(playerLocation, mazeMap, piecesOfCheese)
