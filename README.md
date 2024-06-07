# SomeDataHarvester
"SomeDataHarvesting" est un outil d'automatisation développé pour extraire des informations spécifiques telles que les adresses e-mail et les détails de formation à partir des noms et prénoms d'étudiants à partir de l'annuaire universitaire.
# Important 
Pour assurer la conformité avec la législation, il est indispensable de solliciter et obtenir le consentement explicite de chaque individu listé avant de procéder à la collecte des données ciblées.
# Contexte de fonctionnement
Cet outil pourrait notamment fonctionner pour l'annuaire de l'Univ Paris 1. Pour le faire fonctionner il faut 5 inputs.
## id et pw
Respectivement l'identifiant et le mot de passe pour se connecter à l'EPI/ENT de l'université en question
## URLbase
Il s'agit de l'URL qui mène directement à l'annuaire, on utilise le fait que la quasi-totalité des URLs de l'annuaire menant à une page d'un membre se forme à partir du nom et prenom
## UrlLoginPage
Il s'agit de l'URL de la page qui mène directement à l'endroit où on peut rentrer l'identifiant et le mot de passe pour se connecter à l'ENT, EPI
## Matrice
Il s'agit d'un document csv composé de 2 colonnes (Nom;Prenom) sur lequel on a dans le meilleur des cas uniquement des noms et prenoms en majuscule et sans accent.
C'est le coeur de l'outil
## Exemple fictif 
on a un TXT.csv avec [[Nom1,Prenom1],[Nom2,Prenom2]] : Matrice = pd.read_csv('path/TXT.csv')
id, pw = MonIdentifiantSecret, MonMotDePasseSecret
URLbase = 'https://annuaire.uneuniversiteaupif.fr/ent/'
(par exemple pour l'Université Paris 2 Panthéon Assas) UrlLoginPage = 'https://cas.u-paris2.fr/cas/login?service=https://ent.u-paris2.fr/uPortal/Login%3FrefUrl%3D%2FuPortal%2Ff%2Fwelcome%2Fnormal%2Frender.uP'
## Puis executer la fonction suivante:
Collection(Matrice,id,pw,URLbase,UrlLoginPage)
Cela fait une itération sur toutes les lignes de la liste d'individus puis si disponible cela enregistre les données puis cela est in fine sauvegardé dans un ficher csv nommé Data
