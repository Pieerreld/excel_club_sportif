#Créé le 29/12/22, dernière modification le 10/01/23, Le Dreff Pierre
#Permet de mettre le nom des différentes communes dans une liste sans doublons
#Return le nom des différentes communes

import re
import openpyxl

def ville () :
    workbook = openpyxl.load_workbook('../datas/exportADOC_2022-2023.xlsx', data_only = True)
    titres_onglets = workbook.sheetnames
    onglet1 = workbook[titres_onglets[0]]
        
    colonnes = []
    for r in onglet1['L3':'L272']:
        colonnes.append([cell.value for cell in r])
    #Ajout des villes sans doublons dans la liste ville
    city = []
    for i in (colonnes) :
        if i not in city :
            city.append(i)
    ville = []
    for i in city:
        c = str(i)
        a = re.sub(r"[^a-zA-Z0-9]","",c)
        ville.append(a)
    return ville