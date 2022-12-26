import openpyxl

workbook = openpyxl.load_workbook('exportADOC_2022-2023.xlsx', data_only = True)
titres_onglets = workbook.sheetnames
onglet1 = workbook[titres_onglets[0]]

colonnes = []
for column in onglet1.columns:
    colonnes.append([cell.value for cell in column])

#Compte le nombre de noms dans la colone des noms = nombre adhérents
nbr_adherent = onglet1['B3':'B272']
print("Il y a : ",len(nbr_adherent)," adhérents")
#ferme le fichier excel
workbook.close()