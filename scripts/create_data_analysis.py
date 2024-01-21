"""
Script de création des statistiques sur les prix des montres.

Auteur: Manon Tessier
Date: 2023-12-04

La fonction create_stats_by_market prend en entrée un dataframe contenant les données sur les montres d'un certain marché et donne
en sortie un autre dataframe contenant des statistiques telles que la moyenne des prix, le prix médian, le prix max... en 2021 et en 2023.
La fonction create_stats_by_market_and_collection fait strictement la même chose mais en filtrant en plus sur une collection particulière.

Points d'amélioration possibles :
- Les deux fonctions peuvent être regroupées en 1 seule en mettant une valeur à collection en entrée et un if... pour filtrer le dataframe 
derrière
"""

import pandas as pd

def create_stats_by_market(df):
    df_old = df.loc[df['time scope']=='December 2021']
    df_new = df.loc[df['time scope']=='December 2023']
    df_price_stats = pd.DataFrame({'December 2021':[len(df_old['price']),
                                                    df_old['price'].mean(), 
                                                    df_old['price'].median(),
                                                    df_old['price'].min(), 
                                                    df_old['price'].max(),
                                                    df_old['price'].max()-df_old['price'].min(),
                                                    df_old['price'].std()],
                                   'December 2023':[len(df_new['price']),
                                                    df_new['price'].mean(), 
                                                    df_new['price'].median(),
                                                    df_new['price'].min(),
                                                    df_new['price'].max(),
                                                    df_new["price"].max()-df_new["price"].min(),
                                                    df_new['price'].std()]}
                                ,index=["Nombre d'articles","Moyenne", "Mediane", "Minimum","Maximum", "Plage", "Ecart-type"])
    return df_price_stats

def create_stats_by_market_and_collection(df, collection):
    df = df.loc[(df['collection']==collection)]
    df_old_collection = df.loc[(df['time scope']=='December 2021')]
    df_new_collection = df.loc[(df['time scope']=='December 2023')]
    df_price_stats_collection = pd.DataFrame({'December 2021':[len(df_old_collection['price']),
                                                               df_old_collection['price'].mean(), 
                                                               df_old_collection['price'].median(),
                                                               df_old_collection['price'].min(), 
                                                               df_old_collection['price'].max(),
                                                               df_old_collection['price'].max()-df_old_collection['price'].min(),
                                                               df_old_collection['price'].std()],
                                              'December 2023':[len(df_new_collection["price"]),
                                                               df_new_collection['price'].mean(), 
                                                               df_new_collection['price'].median(),
                                                               df_new_collection['price'].min(),
                                                               df_new_collection['price'].max(),
                                                               df_new_collection['price'].max()-df_new_collection['price'].min(),
                                                               df_new_collection['price'].std()]}
                                            ,index=["Nombre d'articles","Moyenne", "Mediane", "Minimum","Maximum", "Plage", "Ecart-type"])
    return df_price_stats_collection
