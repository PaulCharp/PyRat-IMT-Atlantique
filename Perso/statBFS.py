#In this program we'll make a statistic analysis of our BFS algorithm
#On veut tracer un graphique de l'efficacite de nos algorithmes. Pour ça on trace le temps d'execution divise
#par le nombre de fromage en fonction du nombre de fromage.
#Pour chaque nombre de fromage on fait donc une moyenne sur plusieurs experience et on la plot.
#On doit executer le terminal dans PyRat-master car sinon pyrat ne trouve pas le fichier des ressources
#synchronous permet de calculer le temps que met notre fonction et enleve les temps parasites

import os

def plotGraphCheese():
    for nbCheese in range(1,41):
        os.system("python pyrat.py --rat ../Perso/BFS.py -p" + str(nbCheese)+" -md 0.0 --nodrawing --synchronous --auto_exit")

if __name__ == '__main__':
    plotGraphCheese()
