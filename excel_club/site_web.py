#Créé le 10/01/23, dernière modification le 10/01/23, Le Dreff Pierre
#Fonction qui ouvre ou cré le fichier index.html dans le quel est écrit le script permettant d'afficher les données du club sportif

import nbr_adherent
import webbrowser

def web():
    resultat = nbr_adherent.nbr_adherent()
    with open("../html/index.html","w") as fic:
        fic.write("""
                  <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Données</title>
        <link href="main.css" rel="stylesheet">
    </head>
    <body>
        <header>
            <h1>Données tirées du document excel</h1>
        </header>
        <artcile>
            <p>Le nombre d'adhérent est : {}.</p>
        </article>
        <article>
            <img src="../datas/effectif_categorie.png">
        </article>
        <article>
            <img src="../datas/repartition_communes.png" style="width:100%;">
        </article>
        <article>
            <img src="../datas/homme_femme_categorie.png">
        </article>
        <article>
            <img src="../datas/nbr_par_classement.png">
        </article>
    
    </body>
    </html>
                  """.format(resultat))
                  
    with open("../html/main.css","w") as fic:
        fic.write("""
    
    h1{
       text-align: center;
       margin-bottom: 5vh;
       }     
    
    p{
      margin-bottom:5vh;
      }         
    
    article {
      box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;
      width: 100%; /* chaque article occupe 50% de la largeur de la page */
      margin-bottom: 5vh ; /* centre chaque article horizontalement */
      border: 1px solid black; /* ajoute une bordure autour de chaque article */
      text-align: center; /* centre le texte à l'intérieur de chaque article */
    }
    
    article img {
      display: block; /* place l'image en bloc pour qu'elle occupe toute la largeur de l'article */
      margin: 0 auto; /* centre l'image horizontalement */
    }
    
            """)
    return webbrowser.open_new_tab("../html/index.html")