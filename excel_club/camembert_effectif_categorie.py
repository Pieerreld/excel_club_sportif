#Créé le 29/12/22, dernière modification le 10/01/23, Le Dreff Pierre
#Cré le graphe en camembert de la répartition des adhérents par catégorie en %

import matplotlib.pyplot as plt
import openpyxl
import nbr_adherent_categorie as nbr
plt.rcParams["figure.figsize"] = (10, 10)
nbr.effectif_categorie()

fig, axes = plt.subplots()  # Creation d'un figure avec un seul axe
axes.set_title('Répartition Homme / Femme par catégorie')

labels = ['mini' , 'jeune' , 'adulte']
colors = ['blue', 'red', 'yellowgreen']
relief = True

plt.pie(nbr.effectif_categorie(), labels=labels, colors=colors,
     autopct='%1.1f%%',shadow=relief, startangle=90)

#positionne la legende au mieux
axes.legend(loc='best')

plt.savefig('../datas/effectif_categorie.png')
plt.show()