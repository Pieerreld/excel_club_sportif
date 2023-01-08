import matplotlib.pyplot as plt
import ville
import communes

ville.ville()
communes.nbr_par_commune()
plt.rcParams["figure.figsize"] = (40, 40)
fig, axes = plt.subplots()  # Creation d'un figure avec un seul axe
axes.set_title('Répartition par commune')

labels = []
for i in reversed (ville.ville()):
    labels.append(i)
colors = ['blue','black','green','red','yellow','grey','pink','orange','brown','purple']
relief = True

plt.pie(communes.nbr_par_commune(), labels=labels, colors=colors,
     autopct='%1.1f%%',shadow=relief, startangle=90)
for value in communes.nbr_par_commune():
    plt.text(0,0 ,str(value),ha='center', va='center')

#positionne la legende au mieux
plt.legend(labels, bbox_to_anchor=(1,0), loc="right", 
                          bbox_transform=plt.gcf().transFigure)

plt.savefig('repartition_communes.png')
plt.show()