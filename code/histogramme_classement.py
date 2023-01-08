import matplotlib.pyplot as plt
import nbr_classement
import classement

plt.rcParams["figure.figsize"] = (10, 10)
fig, axes = plt.subplots()

axes.set_xlabel('Genre/Catégorie') #label de l'axe des abscisses
axes.set_ylabel('Nombre adhérents') #label de laxe des ordonnées
axes.set_title('Histogramme de la repartition homme / femme par catégorie') #titre du graphique


#axe des x
x = []
for i in reversed(classement.classement()):
    x.append(i)
#tableaux des valeurs de chaque colonne

#largeur des colonnes
width = 0.9

axes.bar(x, nbr_classement.nbr_par_classement(), width, align = 'center', color='b', edgecolor='black' )
plt.savefig('nbr_par_classement.png')
plt.show()