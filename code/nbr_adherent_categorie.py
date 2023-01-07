import openpyxl

def effectif_categorie() :

    workbook = openpyxl.load_workbook('exportADOC_2022-2023.xlsx', data_only = True)
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