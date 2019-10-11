

def djikstra(maze_map,initial):
    """
    renvois un couple (distance, table de routage)
    """
    route={initial:[0,None]}#table de routage
    aVisiter=[(0,initial)]#pile
    visiter=[]
    while(aVisiter!=[]):#tant que l'algorithme n'est pas fini
            neud=heapq.heappop(aVisiter)[1]

            voisin=maze_map[neud]#on cocmdnsidére touts les voisins
            for (x,y) in voisin:
                longueur=route[neud][0]+voisin[(x,y)]#longueur de la route passant par le sommet précédent
                if not((x,y) in route) or longueur<route[(x,y)][0]:#si rien dans la table de routage ou le chemin déja trouvé est plus grand que le nouveau, on change le chemin
                    route[(x,y)]=[longueur,neud]


                if not((x,y) in visiter) and (not("cheese" in route)):#si le voisin n'a jamais été visiter et on l'ajoute dans le tas
                    heapq.heappush(aVisiter,(longueur,(x,y)))
                    visiter.append((x,y))

    return route
