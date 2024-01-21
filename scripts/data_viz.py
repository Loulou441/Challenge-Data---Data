"""
Script de création des graphiques pour visualiser les données.

Auteur: Manon Tessier
Date: 2023-12-04

Ce script prend les fichiers de données Excel contenant des informations de prix sur les montres, utilise la bibliothèque pandas
pour effectuer le nettoyage et la transformation des données, puis utilise pandas pour générer des graphiques avec matplotlib pour
visualiser les statistiques de prix.

Limitations actuelles :
- Visualisation "à la main" en commentant / décommentant les lignes.
"""

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import StrMethodFormatter

fr_market = pd.read_excel('excel_files/fr_market_data.xlsx')
jap_market = pd.read_excel('excel_files/jap_market_data.xlsx')
uk_market = pd.read_excel('excel_files/uk_market_data.xlsx')
us_market = pd.read_excel('excel_files/us_market_data.xlsx')

#ax = fr_market.hist(by='time scope', column='price')
#ax = fr_market.loc[fr_market['collection']=='RADIOMIR'].hist(by='time scope', column='price')
#ax = fr_market.loc[fr_market['collection']=='LUMINOR'].hist(by='time scope', column='price')
#ax = fr_market.loc[fr_market['collection']=='LUMINOR-DUE'].hist(by='time scope', column='price')
#ax = fr_market.loc[fr_market['collection']=='SUBMERSIBLE'].hist(by='time scope', column='price')

#ax = jap_market.hist(by='time scope', column='price')
#ax = jap_market.loc[jap_market['collection']=='RADIOMIR'].hist(by='time scope', column='price')
#ax = jap_market.loc[jap_market['collection']=='LUMINOR'].hist(by='time scope', column='price')
#ax = jap_market.loc[jap_market['collection']=='LUMINOR-DUE'].hist(by='time scope', column='price')
#ax = jap_market.loc[jap_market['collection']=='SUBMERSIBLE'].hist(by='time scope', column='price')

#ax = uk_market.hist(by='time scope', column='price')
#ax = uk_market.loc[uk_market['collection']=='RADIOMIR'].hist(by='time scope', column='price')
#ax = uk_market.loc[uk_market['collection']=='LUMINOR'].hist(by='time scope', column='price')
#ax = uk_market.loc[uk_market['collection']=='LUMINOR-DUE'].hist(by='time scope', column='price')
#ax = uk_market.loc[uk_market['collection']=='SUBMERSIBLE'].hist(by='time scope', column='price')

#ax = us_market.hist(by='time scope', column='price')
#ax = us_market.loc[us_market['collection']=='RADIOMIR'].hist(by='time scope', column='price')
#ax = us_market.loc[us_market['collection']=='LUMINOR'].hist(by='time scope', column='price')
#ax = us_market.loc[us_market['collection']=='LUMINOR-DUE'].hist(by='time scope', column='price')
ax = us_market.loc[us_market['collection']=='SUBMERSIBLE'].hist(by='time scope', column='price')

for i,x in enumerate(ax):
    # Set x-axis label
    x.set_xlabel("Prix (en $US)", labelpad=20, weight='bold', size=12)

    # Set y-axis label
    x.set_ylabel("Nombre de montres", weight='bold', size=12)

    # Format y-axis label
    x.yaxis.set_major_formatter(StrMethodFormatter('{x:,g}'))
plt.show()
