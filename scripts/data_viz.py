"""
Script for creating graphs to visualize data.

Author: Manon Tessier
Date: 2023-12-04

This script takes Excel data files containing price information on watches, uses the pandas library
library to perform data cleansing and transformation, then uses pandas to generate graphs with matplotlib to
price statistics.

Current limitations:
- Visualization "by hand" by commenting / uncommenting lines.
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
