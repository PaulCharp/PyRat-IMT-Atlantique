import random
import numpy as np


MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'


global visiter
global chemin



chemin=[]

def random_move (maze_map,player_location) :
    listeMouvement=[]
    for (x,y) in maze_map[player_location]:
        listeMouvement.append((x,y))
    return deplacer(player_location, random.choice(listeMouvement))



def preprocessing (maze_map, maze_width, maze_height, player_location, opponent_location, pieces_of_cheese, time_allowed) :
    global visiter
    visiter=np.zeros((maze_width,maze_height))
    pass


def deplacer(player_location,location):

    diff=tuple(np.subtract(location, player_location))
    if diff==(-1,0):
        return MOVE_LEFT
    elif diff==(1,0):
        return 'R'
    elif diff==(0,-1):
        return 'D'
    elif diff==(0,1):
        return 'U'


def turn (maze_map, maze_width, maze_height, player_location, opponent_location, player_score, opponent_score, pieces_of_cheese, time_allowed) :
    global visiter
    global chemin
    global track
    visiter[player_location[0]][player_location[1]]=1
    listeNonVu=[]
    for (x,y) in maze_map[player_location]:
        if visiter[x][y]==0:
            listeNonVu.append((x,y))
    if listeNonVu!=[]:
        choix=random.choice(listeNonVu)
        chemin.append(player_location)
        return deplacer(player_location, choix)
    else:
        if chemin==[]:
            return random_move(maze_map,player_location)
        else:
            choix=chemin.pop(-1)
            return deplacer(player_location,choix)


