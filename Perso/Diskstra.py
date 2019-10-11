#Here we implement the dijkstra algortihm to reach a piece of chese

##############################################################
# The turn function should always return a move to indicate where to go
# The four possibilities are defined here
##############################################################
#We'll implement our queing structure :
#The idea of
import numpy as np
import sys

class MiniHeap:

    #The most efficient is to use a binary heap tree (un algorithm de tas, on fait un recouvrement en utilisant des structures de tas)
    #Each node will contain both the number of our vertices and the distance between the origin
    #Each node is then (v,d)
    #each node has its child at 2*i+1 and 2*i+2
    #Then each node has its parents at
        #Either (p-1)/2 if p is uneven
        #Nor (p-2)/2 is p is even
    def __init__(self):
        self.heap = []

    def parent(self,key): #Note that the parent key can be found at int((i-1)/2) whatever the case
        if key==0 :# Then it is the root
            return key
        if int(key/2)==key/2 : #if the key is even
            return int((key-2)/2)
        else :
            return int((key-1)/2)

    def insert(self,element):
        key = len(self.heap) #We will insert a new element at the place of len(self.heap)
        self.heap.append(element)
        vertices, distance = element #We depack the information in element
        #Then we compare this element to its parent
        #If it's greater than him we exange them
        #The strictly above is what statisfy the termination, if our element is the root then it is compared to himself and the loop stops
        parent_key = self.parent(key)
        while distance < self.heap[parent_key][1] :
            self.heap[key], self.heap[parent_key] = self.heap[parent_key], self.heap[key]
            #We change our element's position, we have to update the key
            key = parent_key
            #Then we update the parent key
            parent_key = self.parent(key)


    def minSon(self,key):
        #Return the max son of an element
        #Signature key,(child_vertices,distance), return the son with the min distance
        i = key
        if (2*i+1) >= len(self.heap) -1: #our node is already a leaf, we return himself
            return key, self.heap[key]
        elif (2*i+1) == len(self.heap) : #This node has an only child
            return 2*i+1, self.heap[2*i+1]
        else : #This node has two children we have to compare and chose the minimum one
            if self.heap[2*i+1][1]<self.heap[2*i+2][1]: #Then it's our node 2*i+1 which is the shorter
                return 2*i*1, self.heap[2*i+1]
            else :
                return 2*i+2, self.heap[2*i+2]

    def delete(self,key):
        #We delete an element and replace it by the last of our tree and then reorder
        self.heap[key]=self.heap[len(self.heap)-1]
        self.heap.pop()
        #We check that our heap is not empty
        if self.heap==[]:
            return
        #Let's reorder, we consider our element as the root of our local tree
        vertice, distance = self.heap[key]
        sonKey, sonElement = self.minSon(key)
        sonVertice, sonDistance = sonElement #We depack our information
        while sonDistance < distance : #We exchange them to get the minimum at the root of our tree
            self.heap[key], self.heap[sonKey] = self.heap[sonKey], self.heap[key]
            key = sonKey
            sonKey, sonElement = self.minSon(key)
            sonVertice, sonDistance = sonElement #We depack our information

    def sonKeys(self,key):
        #Return the keys of the sons [key_son1,key_son2] if there isn't any child return []
        i = key
        if (2*i+1) >= len(self.heap) -1: #our node is already a leaf, we return empty
            return []
        elif (2*i+1) == len(self.heap) : #This node has an only child
            return [2*i+1]
        else : #This node has two children we have to compare and chose the minimum one
            return [2*i+1,2*i+2]

    def insertOrReplace(self, element):
        # element is composed of ((x,y),distanceToThePlayerLocation)
        if self.heap == []:
            self.insert(element)
            return
        #We have to travel throught our graph to reach the key we may want to replace
        #We'll do an prefix DFS
        #We'll use a stack data structure
        vertice, distance = element #Depack our data
        stack = [0]
        result = False #False if we haven't find our element, true if we had
        while not result and not (stack == []):
            key = stack.pop()
            #We compare our vertices
            if self.heap[key][0]==vertice:
                result = True
            elif distance >= self.heap[key][1]:
                stack += self.sonKeys(key)
            #W try to pop an element out of stack, in case our element we are searching is the last one of our tree, our stack is empty but result = True
            if not(stack==[]) and not result :
                key = stack.pop()
        if result :
            #Then we compare to the one we want to add
            if distance < self.heap[key][1]: #we replace it
                self.delete(key)
                self.insert(element)
        else : #We add it to the tree
            self.insert(element)

    def remove(self):
        #Remove and return the minimum of our heap, which is the first one our liste : the root
        if not self.heap == []:
            ans = self.heap[0]
            self.delete(0)
            return ans
        else:
            return

MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'

moves = None
#On creer une variable globale qui contiendrat toutes nos informations à propos de l'état actuel de nos stratégies de déplacement
class Moves:

    def __init__(self):
        self.conversionDirection = {
            (1,0):'L',
            (-1,0):'R',
            (0,1):'D',
            (0,-1):'U'
        }
        self.path = []

    def dijkstra(self,playerLocation, mazeMap, mazeWidth, mazeHeight, target):
        #We start from our position, for each node we want to associate its distance to the origin
        #We will put this in a tab where each key is a node and the entry the distance compared to the origin
        #This is dynamic programmation. So as to access the minimum in a minimum of time
        #We use the miniHeap queing structure. Each time we visit a summit, we add its neighbour to our heap, if it hasn't been visited yet.
        #Then, we remove the minimum from our tree and so on until we reach the summit we wanted to reach. The correction is that, if we add a
        #summit in our queing structure, its distance from the origin is the minimum one and the sommit remove is a distance d and all the
        #over summit of the graph are at distance /geq d.
        #Dijkstra return the shortest path in the wrong order (right to left)
        distancesTab = np.full((mazeWidth,mazeHeight),np.inf)
        #We create the tab to each vertice we associate its parents to create the routing table
        routingTable = np.full((mazeWidth,mazeHeight), None)
        dejaVu = np.full((mazeWidth, mazeHeight), False)
        actNode = playerLocation
        distance = 0
        heap = MiniHeap()
        heap.insertOrReplace((playerLocation,distance))
        dejaVu[actNode] = True
        distancesTab[playerLocation]=0
        while not heap.heap == [] or actNode == target : #We keep processing as long as the our queing structure is not empty or we havn't reach our target
            (actNode, distance) = heap.remove()
            for ((voisin_x,voisin_y), boue) in mazeMap[actNode].items(): #We check every neighbour
                print("mazeMap.items", mazeMap[actNode].items())
                if distance + boue < distancesTab[voisin_x, voisin_y] : #If the distance found is shorter by this path
                    distancesTab[voisin_x, voisin_y] = distance + boue
                    #Note that if our point is in dejaVu, the distance is already the shortest one
                    #The parent has to be changed then
                    routingTable[voisin_x, voisin_y] = actNode
                if not dejaVu[voisin_x, voisin_y] : #We add it to our queing structure
                    print('ok')
                    heap.insertOrReplace(((voisin_x,voisin_y),distance + boue))
                    dejaVu[voisin_x, voisin_y] = True
            print(heap.heap)
        print(distancesTab)
        print(target)
        sys.exit()

        #We have finally filled our distanceTab, now we'll create the path
        #Back from our target we'll go back to the origin by always choosing the neighbour having the shortest distance.
        path = []
        path.append(target)
        actNode = target
        while not actNode == playerLocation :
            listNeighbour = list(mazeMap[actNode].items())
            nextNode = minimumNeighbour(listNeighbour,distancesTab)
            path.append(nextNode)
            actNode = nextNode
        self.path = path

    def makeAChoice(self, playerLocation, mazeMap, piecesOfCheese, mazeWidth, mazeHeight):
        if self.path == []:
            self.dijkstra(playerLocation, mazeMap, mazeWidth, mazeHeight, piecesOfCheese[0])
        ans = self.pop()
        print(self.conversionDirection[ans - playerLocation])
        return self.conversionDirection[ans - playerLocation]




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
    moves = Moves()
    return

def turn(mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, playerScore, opponentScore, piecesOfCheese, timeAllowed):
    global moves
    return moves.makeAChoice(playerLocation, mazeMap, piecesOfCheese, mazeWidth, mazeHeight)
