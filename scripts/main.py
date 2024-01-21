"""
Main script for executing functions to create stats.

Author: Manon Tessier
Date: 2023-12-04

This script combines all the previous scripts and follows 5 steps:
1) 2021 data retrieval via excel file
2) Retrieve 2023 data via scrapper
3) Creation of data files to be used (one file per market)
4) Create stats by market, then by collection 
5) Write stats per market in Excel = overall market stats + stats per collection (5 sheets per file)

Current limitations :
- Non-dynamically generated file names --> files overwritten on each run
Possible areas for improvement :
- Dynamize file names with date and sort by folder
- Find a way to loop the execution of functions on markets and collections. Here, the number of 4 markets
doesn't make the task too arduous, but it can quickly become a problem if you take all the brand's markets, for example.
"""

#Technical challenge
import pandas as pd
from webscrapper import webscrapper, list_of_pages
from create_files_to_exploit import create_files_to_exploit
from create_data_analysis import create_stats_by_market, create_stats_by_market_and_collection

#Getting 2021 data
old_prices = pd.read_excel('excel_files/PANERAI_DATA_122021.xlsx')

#website scrapping and data recovery for new prices
##Dataframe init
new_prices = pd.DataFrame(columns=['brand','url','image_url','collection','reference','price','currency','country','time scope'])

##Scrapping on all site pages
for i in list_of_pages:
    df = webscrapper(i)
    new_prices=pd.concat([new_prices,df])

##writing
new_prices.reset_index(drop=True).to_excel('excel_files/PANERAI_DATA_120423.xlsx')

#data formatting and creation of data files for processing
##Recovering new prices
new_prices = pd.read_excel('excel_files/PANERAI_DATA_120423.xlsx')

##Creating files by market
fr_market, jap_market, uk_market, us_market = create_files_to_exploit(old_prices, new_prices)

#Create stats
##Global creation of stats for each market.
fr_price_stats = create_stats_by_market(fr_market)
jap_price_stats = create_stats_by_market(jap_market)
uk_price_stats = create_stats_by_market(uk_market)
us_price_stats = create_stats_by_market(us_market)

##Create stats by market and collection
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

##Stats by market = overall market stats + stats by collection
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
