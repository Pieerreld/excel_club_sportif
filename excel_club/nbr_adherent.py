#Créé le 23/12/22, dernière modification le 10/01/23, Le Dreff Pierre
#Importe une colonne (peu importe) dans une liste et compte sa longueur (len) pour connaître le nombre d'adhérent puisqu'il y a une ligne par adhérent

import openpyxl

def nbr_adherent():

    workbook = openpyxl.load_workbook('../datas/exportADOC_2022-2023.xlsx', data_only = True)
    titres_onglets = workbook.sheetnames
    onglet1 = workbook[titres_onglets[0]]
    
    colonnes = []
    for column in onglet1.columns:
        colonnes.append([cell.value for cell in column])
    
    #Compte le nombre de noms dans la colone des noms = nombre adhérents
    nbr = onglet1['B3':'B272']
    
    return len(nbr)
    #ferme le fichier excel
    workbook.close()