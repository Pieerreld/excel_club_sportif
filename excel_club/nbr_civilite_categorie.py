#Créé le 7/01/23, dernière modification le 10/01/23, Le Dreff Pierre
#Reprend le même principe que nbr_adherent_categorie.py mais le compteur d'âge existe en deux version (homme ou femme) pose donc une condition pour connaitre la version à incrémenter
#Return une liste de nombres dans le même ordre que nbr_adhrent_categorie mais par deux pour une catégorie, le premier correspondant aux femmes et le second aux hommes

import openpyxl

def civilite_categorie():

    workbook = openpyxl.load_workbook('../datas/exportADOC_2022-2023.xlsx', data_only = True)
    titres_onglets = workbook.sheetnames
    onglet1 = workbook[titres_onglets[0]]
    
    colonnes = []
    for r in onglet1['F3':'F272']:
        colonnes.append([cell.value for cell in r])
        
    civilite = []
    for r in onglet1['D3':'D272']:
        civilite.append([cell.value for cell in r])
    
    nbr =[]
    mini_homme = 0
    mini_femme = 0
    adulte_homme = 0
    adulte_femme = 0
    jeune_homme = 0
    jeune_femme = 0
    a = [7]
    b = [18]
    c = ['Monsieur']
    for j,i in zip(colonnes,civilite)  :
        if j < a :
            if i == c :
                mini_homme +=1
            else :
                mini_femme +=1
        elif j >= b :
            if i == c :
                adulte_homme +=1
            else :
                adulte_femme +=1
        else :
            if i == c :
                jeune_homme +=1
            else :
                jeune_femme +=1

    nbr.append(mini_femme)
    nbr.append(mini_homme)
    nbr.append(jeune_femme)
    nbr.append(jeune_homme)
    nbr.append(adulte_femme)
    nbr.append(adulte_homme)

    return nbr

#ferme le fichier excel
    workbook.close()