import re
import openpyxl

def classement () :
    workbook = openpyxl.load_workbook('exportADOC_2022-2023.xlsx', data_only = True)
    titres_onglets = workbook.sheetnames
    onglet1 = workbook[titres_onglets[0]]
        
    colonnes = []
    for r in onglet1['AB3':'AB272']:
        colonnes.append([cell.value for cell in r])
    #Ajout des villes sans doublons dans la liste ville
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