"""
Script to recover key data from the Panerai.com website

Author: Manon Tessier
Date: 2023-12-04

The webcrapper function takes as input a url and returns as output a dataframe containing data on watches 
watches (name, price...) from a certain country and a certain collection.

Current limitations :
- the chrome driver only works with chrome version 114 and earlier.
- the lists of sites to visit and watches not to include are not dynamic --> manual change required
Possible improvements :
- Use the Panerai.com home page to fetch the home pages of the countries concerned, and dynamically scroll down to fetch the urls of the countries concerned. 
dynamically scroll down to fetch collection urls
"""

#importing libraries to scrap
from selenium import webdriver

from bs4 import BeautifulSoup
import pandas as pd

#Getting all the pages to visit
list_of_pages = ['https://www.panerai.com/fr/fr/collections/watch-collection/radiomir.html', 
                 'https://www.panerai.com/fr/fr/collections/watch-collection/luminor.html', 
                 'https://www.panerai.com/fr/fr/collections/watch-collection/luminor-due.html',
                 'https://www.panerai.com/fr/fr/collections/watch-collection/submersible.html',
                 'https://www.panerai.com/gb/en/collections/watch-collection/radiomir.html',
                 'https://www.panerai.com/gb/en/collections/watch-collection/luminor.html',
                 'https://www.panerai.com/gb/en/collections/watch-collection/luminor-due.html',
                 'https://www.panerai.com/gb/en/collections/watch-collection/submersible.html',
                 'https://www.panerai.com/jp/ja/collections/watch-collection/radiomir.html',
                 'https://www.panerai.com/jp/ja/collections/watch-collection/luminor.html',
                 'https://www.panerai.com/jp/ja/collections/watch-collection/luminor-due.html',
                 'https://www.panerai.com/jp/ja/collections/watch-collection/submersible.html',
                 'https://www.panerai.com/us/en/collections/watch-collection/radiomir.html',
                 'https://www.panerai.com/us/en/collections/watch-collection/luminor.html',
                 'https://www.panerai.com/us/en/collections/watch-collection/luminor-due.html',
                 'https://www.panerai.com/us/en/collections/watch-collection/submersible.html'
                 ]

def webscrapper(url):
    df=pd.DataFrame()
    driver = webdriver.Chrome()
    driver.get(url)

    response = driver.page_source
    soup = BeautifulSoup(response, 'html.parser')
    products = soup.find_all("li", "pan-prod-ref-collection-item-v2 three-grid-item is-sellable-true")+soup.find_all("li", "pan-prod-ref-collection-item-v2 three-grid-item is-sellable-false")
    base_url = "https://www.panerai.com"
    banned_urls = ["https://www.panerai.com/jp/ja/collections/watch-collection/radiomir/pam01432-radiomir-annual-calendar-platinumtech-experience.html",
                   "https://www.panerai.com/jp/ja/collections/watch-collection/radiomir/pam01363-radiomir-annual-calendar-goldtech.html"]
    for product in products: 
        url = base_url+product.a['href']
        image_url = base_url+product.img["data-src"]
        if url not in banned_urls:
            product_data = eval(product.a['data-tracking-product'])
            collection = product_data["collection"].upper()
            reference = product_data["id"]
            price = product_data["price"]
            currency = product_data["currency"]
            country = "France" if currency=="EUR" else "UK" if currency=="GBP" else "USA" if currency == "USD" else "Japan"

            #ajout de la ligne dans df
            new_line = pd.DataFrame({'brand':'Panerai', 
                                    'url':url, 
                                    'image_url':image_url, 
                                    'collection':collection, 
                                    'reference':reference, 
                                    'price':price,
                                    'currency':currency,
                                    'country':country,
                                    'time scope':'December 2023'},
                                    index=[0]
                                    )
        df = pd.concat([df, new_line], ignore_index=True)
    return df

