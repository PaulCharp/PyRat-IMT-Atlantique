#In this program we'll make a statistic analysis of our BFS algorithm
#On veut tracer un graphique de l'efficacite de nos algorithmes.
#On va faire varier la dimension de notre labyrinthe. A chaque iteration, on augmente x et y de 1.
#On a donc une augmentation de l'aire en i^2. On trace donc notre échelle des abscisses en échelle logarithmique
#en base 2.

import os
import time
import matplotlib.pyplot as plt

def plotGrapSize():
    #On recupere les donnes
    n = 100
    X = [x**2 for x in range(5,n)]
    T = []
    for size in range(5,n):
        #On fait la moyenne sur 5 valeurs pour lisser la courbe
        for i in range(5):
            som = 0
            t = time.time()
            os.system("python pyrat.py --rat ../Perso/BFS.py -p 1  -md 0.0 --nodrawing --synchronous --auto_exit -x "+ str(size)+" -y "+str(size))
            ti = time.time()-t
            som += ti
        T.append(som/5)
    #On trace ensuite notre graphique en fonction de l'aire du labyrinthe
    plt.plot(X,T)
    plt.title("Temps d'execution de BFS pour trouver un fromage en fonction de l'aire du labyrinthe.")
    plt.xlabel("Aire du labyrinthe (en nombre de case au carré)")
    plt.ylabel("Temps d'execution de l'algorithme (en ms)")
    plt.show()
    return

if __name__ == '__main__':
    plotGrapSize()
