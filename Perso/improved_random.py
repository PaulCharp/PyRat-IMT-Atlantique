TEAM_NAME = "Random"

##############################################################
# The turn function should always return a move to indicate where to go
# The four possibilities are defined here
##############################################################

MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'

##############################################################
# The preprocessing function is called at the start of a game
# It can be used to perform intensive computations that can be
# used later to move the player in the maze.
# ------------------------------------------------------------
# maze_map : dict(pair(int, int), dict(pair(int, int), int))
# maze_width : int
# maze_height : int
# player_location : pair(int, int)
# opponent_location : pair(int,int)
# pieces_of_cheese : list(pair(int, int))
# time_allowed : float
##############################################################


import random
import copy
import sys

def preprocessing(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, piecesOfCheese, timeAllowed):
    global accessibleMap = copy.deepcopy(mazeMap)
    global conversionDirection = {
        (1,0):'L',
        (-1,0):'R',
        (0,1):'D',
        (0,-1):'U'
    }
    return

def turn(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, playerScore, opponentScore, piecesOfCheese, timeAllowed):
    #On va copier le labyrinthe et on va modifier cette copie pour ne laisser que les arretes que le rat peut emprunter
    if accessibleMap[player_location] == {}:
        sys.exit('[+] End of the game')
    else :
        choice = random.choice(List(accessibleMap[player_location].keys()))
        del accessibleMap[player_location]
        #On a donc la localisation de la case où on veut aller mais pas la direction
        direction = conversionDirection[(player_location[0]-choice[0],player_location[1]-choice[1])]
        return direction
