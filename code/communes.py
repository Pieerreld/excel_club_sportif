import openpyxl
import operator as op

workbook = openpyxl.load_workbook('/home/etudiant/Documents/exportADOC_2022-2023.xlsx', data_only = True)
titres_onglets = workbook.sheetnames
onglet1 = workbook[titres_onglets[0]]

colonnes = []
for r in onglet1['L3':'L272']:
    colonnes.append([cell.value for cell in r])
#Ajout des villes sans doublons dans la liste ville
ville = []
for i in colonnes :
    if i not in ville :
        ville.append(i)

# x représente le nombre de communes        
x = len(ville)
x = x-1     #position du dernier élément de la liste


for j in colonnes :
    while x >=0 :     #Pour aller jusqu'à l'élément d'id 0 de la liste
       print(f"{ville[x]} est present {op.countOf(colonnes, ville[x])} fois")
       x = x-1


