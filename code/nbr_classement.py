import openpyxl
import operator as op
import classement
import re

def nbr_par_classement () :

    workbook = openpyxl.load_workbook('exportADOC_2022-2023.xlsx', data_only = True)
    titres_onglets = workbook.sheetnames
    onglet1 = workbook[titres_onglets[0]]
    
    valeur = []
    nom = []
    colonnes = []
    for r in onglet1['AB3':'AB272']:
        colonnes.append([cell.value for cell in r])
    
    for i in colonnes:
        c = str(i)
        a = re.sub(r"[^a-zA-Z0-9-/]","",c)
        nom.append(a)
        
    classe = []
    for i in classement.classement():
        classe.append(i)
           
    x = len(classe)
    x = x-1     #position du dernier élément de la liste
    
    
    for j in (nom) :
        while x >=0 :     #Pour aller jusqu'à l'élément d'id 0 de la liste
           valeur.append(op.countOf(nom, classe[x]))
           x = x-1
    return valeur


