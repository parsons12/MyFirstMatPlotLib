import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().magic('matplotlib notebook')
plt.style.use('seaborn-colorblind')

#read gdp data
dfgdp = pd.read_csv("https://data.michigan.gov/resource/3vb5-jb2s.csv")

#clean the dataframe by sorting and deleting unwanted columns
dfgdp = dfgdp.sort(['year'])
dfgdp.drop(dfgdp.columns[2:5], axis=1, inplace=True)
del dfgdp['highlights']
dfgdp = dfgdp.rename(index=str, columns={"michigan_percapita_realgdp": "MichiganGDP_PerCapita", "us_percapita_realgdp": "USGDP_PerCapita"})

#read income data
dfIncome = pd.read_csv("https://data.michigan.gov/resource/7frj-2rv6.csv")

#clean the dataframe data
dfIncome = dfIncome.sort(['year'])
dfIncome.drop(dfIncome.columns[3:5], axis=1, inplace=True)
dfIncome.drop(dfIncome.index[0:8], inplace=True)
del dfIncome['highlights']
del dfIncome['michigan_percapita_personal_income_pct_change']
del dfIncome['us_percapita_personal_income_pct_change']

dfIncome = dfIncome.rename(index=str, columns={"michigan_percapita_personal_income": "MichiganPersonalINCOME_PerCapita", "us_percapita_personal_income": "USPersonalINCOME_PerCapita"})

#create new dataframes for USA and Michigan
MichiganGDP = dfgdp[(dfgdp['MichiganGDP_PerCapita'] != 0) & (dfgdp['year']!= 1990)]
USGDP = dfgdp[(dfgdp['USGDP_PerCapita'] != 0) & (dfgdp['year']!= 1990)]
MichiganIncome = dfIncome[(dfIncome['MichiganPersonalINCOME_PerCapita'] != 0) & (dfIncome['year']!= 1990)]
USIncome = dfIncome[(dfIncome['USPersonalINCOME_PerCapita'] != 0) & (dfIncome['year']!= 1990)]


#clean the dataframe
del MichiganGDP['USGDP_PerCapita']
del USGDP['MichiganGDP_PerCapita']
del MichiganIncome['USPersonalINCOME_PerCapita']
del USIncome['MichiganPersonalINCOME_PerCapita']
MichiganGDP = MichiganGDP.set_index(['year'])
USGDP = USGDP.set_index(['year'])
MichiganIncome = MichiganIncome.set_index(['year'])
USIncome = USIncome.set_index(['year'])

#create two plots for income and gdp
plt.figure()
ax1 = plt.subplot(121)
plt.plot(MichiganGDP.values, 'g', label = 'Michigan GDP')
plt.plot(USGDP.values, 'r', label = 'US GDP')

plt.xticks(np.arange(20) ,USGDP.index[0:20], rotation = '45')
plt.xlabel('Year')
plt.ylabel('GDP')
plt.title('Michigan GDP VS US GDP Per Year')
plt.legend(loc = 2, frameon = False)
plt.gca().fill_between(range(len(MichiganGDP)), MichiganGDP['MichiganGDP_PerCapita'], USGDP['USGDP_PerCapita'], facecolor = 'khaki', alpha = 0.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

ax2 = plt.subplot(122, sharex = ax1)
plt.plot(MichiganIncome.values, 'g', label = 'Michigan Income')
plt.plot(USIncome.values, 'r', label = 'US income')

plt.xticks(np.arange(20) ,USIncome.index[0:20], rotation = '45')
plt.xlabel('Year')
plt.ylabel('Income ($)')
plt.title('Michigan Median Income VS US Median Income')
plt.legend(loc = 4, frameon = False)
plt.gca().fill_between(range(len(MichiganIncome)), MichiganIncome['MichiganPersonalINCOME_PerCapita'], USIncome['USPersonalINCOME_PerCapita'], facecolor = 'khaki', alpha = 0.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.show()
