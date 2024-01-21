"""
Script principal d'exécution des fonctions pour créer les stats.

Auteur: Manon Tessier
Date: 2023-12-04

Ce script regroupe tous les scripts précédents et suit 5 étapes:
1) Récupération des données 2021 via le fichier excel
2) Récupération des données 2023 via le scrapper
3) Création des fichiers data à exploiter (un fichier par marché)
4) Création des stats par marché puis par collection 
5) Ecriture en excel des stats par marché = stats globale sur le marché + stats par collection (5 feuilles par fichier)

Limitations actuelles :
- Noms des fichiers généré de manière non dynamique --> écrasement des fichiers à chaque exécution
Points d'amélioration possibles :
- Dynamiser le noms des fichiers avec la date et rangement par dossiers
- Trouver le moyen de faire une boucle pour exécuter les fonctions sur les marchés et les collections. Ici, le nombre de 4 marchés
ne rend pas la tâche trop ardue mais cela peut vite devenir un problème si on prend tous les marchés de la marque par exemple
"""

#Challenge Technique
import pandas as pd
from webscrapper import webscrapper, list_of_pages
from create_files_to_exploit import create_files_to_exploit
from create_data_analysis import create_stats_by_market, create_stats_by_market_and_collection

#Recupération des anciens prix
old_prices = pd.read_excel('excel_files/PANERAI_DATA_122021.xlsx')

#scrapping du site et récupération des données pour les nouveaux prix
##Initialisation du Dataframe
new_prices = pd.DataFrame(columns=['brand','url','image_url','collection','reference','price','currency','country','time scope'])

##Scrapping sur toutes les pages du site
for i in list_of_pages:
    df = webscrapper(i)
    new_prices=pd.concat([new_prices,df])

##Ecriture
new_prices.reset_index(drop=True).to_excel('excel_files/PANERAI_DATA_120423.xlsx')

#mise en forme des données et creation des fichiers data à exploiter
##Récupération nouveau prix
new_prices = pd.read_excel('excel_files/PANERAI_DATA_120423.xlsx')

##Creation des fichiers par marché
fr_market, jap_market, uk_market, us_market = create_files_to_exploit(old_prices, new_prices)

#Creation des stats.
##Création des stats sur chaque marché de manière globale
fr_price_stats = create_stats_by_market(fr_market)
jap_price_stats = create_stats_by_market(jap_market)
uk_price_stats = create_stats_by_market(uk_market)
us_price_stats = create_stats_by_market(us_market)

##Création des stats par marché et par collection
fr_radiomir = create_stats_by_market_and_collection(fr_market,"RADIOMIR")
fr_luminor = create_stats_by_market_and_collection(fr_market,"LUMINOR")
fr_luminor_due = create_stats_by_market_and_collection(fr_market,"LUMINOR-DUE")
fr_submersible = create_stats_by_market_and_collection(fr_market,"SUBMERSIBLE")

jap_radiomir = create_stats_by_market_and_collection(jap_market,"RADIOMIR")
jap_luminor = create_stats_by_market_and_collection(jap_market,"LUMINOR")
jap_luminor_due = create_stats_by_market_and_collection(jap_market,"LUMINOR-DUE")
jap_submersible = create_stats_by_market_and_collection(jap_market,"SUBMERSIBLE")

uk_radiomir = create_stats_by_market_and_collection(uk_market,"RADIOMIR")
uk_luminor = create_stats_by_market_and_collection(uk_market,"LUMINOR")
uk_luminor_due = create_stats_by_market_and_collection(uk_market,"LUMINOR-DUE")
uk_submersible = create_stats_by_market_and_collection(uk_market,"SUBMERSIBLE")

us_radiomir = create_stats_by_market_and_collection(us_market,"RADIOMIR")
us_luminor = create_stats_by_market_and_collection(us_market,"LUMINOR")
us_luminor_due = create_stats_by_market_and_collection(us_market,"LUMINOR-DUE")
us_submersible = create_stats_by_market_and_collection(us_market,"SUBMERSIBLE")

##Ecriture des stats par marché = stats globale sur le marché + stats par collection 
with pd.ExcelWriter('excel_files/fr_market_stats.xlsx') as writer:  
    fr_price_stats.to_excel(writer, sheet_name='Global stats')
    fr_radiomir.to_excel(writer, sheet_name='Radiomir stats')
    fr_luminor.to_excel(writer, sheet_name='Luminor stats')
    fr_luminor_due.to_excel(writer, sheet_name='Luminor-due stats')
    fr_submersible.to_excel(writer, sheet_name='Submersible stats')

with pd.ExcelWriter('excel_files/jap_market_stats.xlsx') as writer:  
    jap_price_stats.to_excel(writer, sheet_name='Global stats')
    jap_radiomir.to_excel(writer, sheet_name='Radiomir stats')
    jap_luminor.to_excel(writer, sheet_name='Luminor stats')
    jap_luminor_due.to_excel(writer, sheet_name='Luminor-due stats')
    jap_submersible.to_excel(writer, sheet_name='Submersible stats')

with pd.ExcelWriter('excel_files/uk_market_stats.xlsx') as writer:  
    uk_price_stats.to_excel(writer, sheet_name='Global stats')
    uk_radiomir.to_excel(writer, sheet_name='Radiomir stats')
    uk_luminor.to_excel(writer, sheet_name='Luminor stats')
    uk_luminor_due.to_excel(writer, sheet_name='Luminor-due stats')
    uk_submersible.to_excel(writer, sheet_name='Submersible stats')

with pd.ExcelWriter('excel_files/us_market_stats.xlsx') as writer:  
    us_price_stats.to_excel(writer, sheet_name='Global stats')
    us_radiomir.to_excel(writer, sheet_name='Radiomir stats')
    us_luminor.to_excel(writer, sheet_name='Luminor stats')
    us_luminor_due.to_excel(writer, sheet_name='Luminor-due stats')
    us_submersible.to_excel(writer, sheet_name='Submersible stats')

""" fr_market.boxplot(by ='time scope', column=['price'], showmeans=True, grid=True)
fr_price_stats.to_excel("excel_files/fr_price_stats.xlsx") """

print('Okay you got it!')
