#Créé le 26/12/22, dernière modification le 10/01/23, Le Dreff Pierre
#Compte dans la liste des âges le nombre de personne dans la tranche d'âge donné et incremente le compteur correspondant
#Return une liste de trois nombre, le premier correspond au nombre de personnes dans la catégorie mini, le second dans la catégorie jeune puis le derniere dans la catégorie adulte


import openpyxl

def effectif_categorie() :

    workbook = openpyxl.load_workbook('../datas/exportADOC_2022-2023.xlsx', data_only = True)
    titres_onglets = workbook.sheetnames
    onglet1 = workbook[titres_onglets[0]]
    
    colonnes = []
    for r in onglet1['F3':'F272']:
        colonnes.append([cell.value for cell in r])
        
    mini = 0
    adulte = 0
    jeune = 0
    a = [7]
    b = [18]
    for i in colonnes :
        if i < a :
            mini +=1
        elif i >= b :
            adulte +=1
        else :
            jeune +=1
    effectif = []
    effectif.append(mini)
    effectif.append(jeune)
    effectif.append(adulte)
    return effectif
    #ferme le fichier excel
    workbook.close()