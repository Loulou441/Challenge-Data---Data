"""
Script for creating watch price statistics.

Author: Manon Tessier
Date: 2023-12-04

The create_stats_by_market function takes as input a dataframe containing data on watches in a certain market, and gives as output
as output another dataframe containing statistics such as average price, median price, max price... in 2021 and 2023.
The create_stats_by_market_and_collection function does strictly the same thing, but with additional filtering on a particular collection.

Possible points for improvement:
- The two functions can be combined into 1 by setting a collection value as input and an if... to filter the dataframe 
behind
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
