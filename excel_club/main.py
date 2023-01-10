#Créé le 10/01/23, dernière modification le 10/01/23, Le Dreff Pierre
#Lance les 4 programmes créant les graphes en png grâce aux fonctions developppé puis execute la fonction web de site_web pour créer la page web grâce aux données


import site_web
import subprocess
subprocess.run(["python3", "camembert_communes.py"])
subprocess.run(["python3", "camembert_effectif_categorie.py"])
subprocess.run(["python3", "histogramme_civilite.py"])
subprocess.run(["python3", "histogramme_classement.py"])
print(site_web.web())
