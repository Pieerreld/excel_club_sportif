#Créé le 07/01/23, dernière modification le 10/01/23, Le Dreff Pierre
#Return l'histogramme du nombre de femmes et hommes par catégorie

import matplotlib.pyplot as plt
import numpy as np
import nbr_civilite_categorie as ncc
plt.rcParams["figure.figsize"] = (10, 10)
fig, axes = plt.subplots()

axes.set_xlabel('Genre/Catégorie') #label de l'axe des abscisses
axes.set_ylabel('Nombre adhérents') #label de laxe des ordonnées
axes.set_title('Histogramme de la repartition homme / femme par catégorie') #titre du graphique


#axe des x
x = ['mini femme','mini homme','jeune femme','jeune homme','adulte femme','adulte homme']
#tableaux des valeurs de chaque colonne

#largeur des colonnes
width = 0.9

axes.bar(x, ncc.civilite_categorie(), width, align = 'center', color='b', edgecolor='black' )
plt.savefig('../datas/homme_femme_categorie.png')
plt.show()