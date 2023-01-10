#Créé le 02/01/23, dernière modification le 10/01/23, Le Dreff Pierre
#Convertit la colone des classements dans une liste pour se servir de la liste à fin de compter les répétitions de chaque classements
#Return une liste avec le nom de chaque classement

import re
import openpyxl

def classement () :
    workbook = openpyxl.load_workbook('../datas/exportADOC_2022-2023.xlsx', data_only = True)
    titres_onglets = workbook.sheetnames
    onglet1 = workbook[titres_onglets[0]]
        
    colonnes = []
    for r in onglet1['AB3':'AB272']:
        colonnes.append([cell.value for cell in r])
    #Ajout des classements sans doublons dans la liste clas
    clas = []
    for i in (colonnes) :
        if i not in clas :
            clas.append(i)
    classement = []
    for i in clas:
        c = str(i)
        a = re.sub(r"[^a-zA-Z0-9-/]","",c)
        classement.append(a)
    return classement