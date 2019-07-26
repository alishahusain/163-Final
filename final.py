
# Final Project

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from shapely import wkt
import matplotlib.pyplot

# Load in data
geo_data = gpd.read_file('countiesFormatV2.csv')
obesity_data = pd.read_excel('obesity_final.xls')
obesity_data = obesity_data.dropna()
health_costs = pd.read_excel('Residence_all_tables.xls', sheet_name='Table 25 Medicaid')
health_costs = health_costs.dropna()

food_access = pd.read_excel('access2015.xls', sheet_name='ACCESS')
food_access = food_access.dropna()
stores = pd.read_excel('access2015.xls', sheet_name='STORES')
stores = stores.dropna()
restaurants = pd.read_excel('access2015.xls', sheet_name='RESTAURANTS')
restaurants = restaurants.dropna()
assistance = pd.read_excel('access2015.xls', sheet_name='ASSISTANCE')
insecurity = pd.read_excel('access2015.xls', sheet_name='INSECURITY')
insecurity = insecurity.dropna()
health = pd.read_excel('access2015.xls', sheet_name='HEALTH')
health = health.dropna()
prices = pd.read_excel('access2015.xls', sheet_name='PRICES_TAXES')
fmarkets = pd.read_excel('access2015.xls', sheet_name='LOCAL')
fmarkets = fmarkets.dropna()
socioecon = pd.read_excel('access2015.xls', sheet_name='SOCIOECONOMIC')
exp_per_cap = pd.read_csv('health_exp_per_capita.csv')

# Select rows of interest in food access dataframe
health_costs = health_costs[['Region/state of residence', 'Abbrev', 'Average']]


food_access = food_access[['FIPS', 'State', 'County', 'PCT_LACCESS_POP10',
                           'PCT_LACCESS_LOWI10', 'PCT_LACCESS_CHILD10',
                           'PCT_LACCESS_SENIORS10', 'PCT_LACCESS_HHNV10']]

# Select rows of interest in stores dataframe
stores = stores[['FIPS', 'State', 'County', 'PCH_GROC_07_12', 'GROCPTH12',
                 'PCH_GROCPTH_07_12', 'PCH_SUPERC_07_12', 'SUPERCPTH07',
                 'SUPERCPTH12', 'PCH_SUPERCPTH_07_12',
                 'PCH_CONVS_07_12', 'CONVSPTH07', 'CONVSPTH12',
                 'PCH_CONVSPTH_07_12', 'PCH_SPECS_07_12', 'SPECSPTH07',
                 'SPECSPTH12', 'PCH_SPECSPTH_07_12', 'PCH_SNAPS_08_12',
                 'SNAPSPTH08', 'SNAPSPTH12', 'PCH_SNAPSPTH_08_12']]

# Select rows of interest in restaurants dataframe
restaurants = restaurants[['FIPS', 'State', 'County',
                           'PCH_FFR_07_12', 'FFRPTH07', 'FFRPTH12',
                           'PCH_FFRPTH_07_12', 'PC_FFRSALES02',
                           'PC_FFRSALES07', 'PC_FSRSALES02', 'PC_FSRSALES07']]

# Select rows of interest in assistance dataframe
assistance = assistance[['FIPS', 'State', 'County',
                        'REDEMP_SNAPS08', 'REDEMP_SNAPS12',
                         'PCH_REDEMP_SNAPS_08_12', 'PCT_SNAP09',
                         'PCT_SNAP14', 'PCH_SNAP_09_14', 'PC_SNAPBEN08',
                         'PC_SNAPBEN10', 'PCH_PC_SNAPBEN_08_10',
                         'SNAP_PART_RATE08', 'SNAP_PART_RATE10']]

# Select rows of interest in insecurity dataframe
insecurity = insecurity[['FIPS', 'State', 'County',
                         'CH_VLFOODSEC_09_12', 'VLFOODSEC_10_12',
                         'CH_FOODINSEC_09_12', 'FOODINSEC_10_12']]

# Select rows of interest in health dataframe
health = health[['FIPS', 'State', 'County',
                 'PCT_DIABETES_ADULTS09', 'PCT_DIABETES_ADULTS10',
                 'PCT_OBESE_ADULTS09', 'PCT_OBESE_ADULTS10',
                 'PCT_OBESE_ADULTS13', 'PCT_OBESE_CHILD08',
                 'PCT_OBESE_CHILD11', 'PCH_OBESE_CHILD_08_11']]


# merge by state - if state in access match state in expenses, add column in
# access, so that  healthcosts['expenses'] = healthdata['Average']


# Select rows of interest in prices dataframe
prices = prices[['FIPS', 'State', 'County', 'MILK_SODA_PRICE10']]

# Select rows of interest in fmarkets dataframe
fmarkets = fmarkets[['FIPS', 'State', 'County',
                     'FMRKTPTH13', 'PCH_FMRKTPTH_09_13',
                     'PCT_FMRKT_SNAP13', 'FMRKT_WIC13']]

# Select rows of interest in socioeconomic dataframe
socioecon = socioecon[['FIPS', 'State', 'County', 'POVRATE10', 'PERPOV10']]


# Select rows of interest for the health expenditure data
exp_per_cap = exp_per_cap[['Item', 'Group', 'Region_Name', 'State_Name',
                           'Y2010', 'Y2011', 'Y2012', 'Y2013', 'Y2014',
                           'Average_Annual_Percent_Growth']]
exp_per_cap = exp_per_cap.rename(index=str,
                                 columns={'Item': 'type_care',
                                          'Y2010': 'H_EXP2010',
                                          'Y2011': 'H_EXP2011',
                                          'Y2012': 'H_EXP2012',
                                          'Y2013': 'H_EXP2013',
                                          'Y2014': 'H_EXP2014'})

# Join data frames with geometry information

geo_data['GEO_ID'] = geo_data['GEO_ID'].astype(str)
food_access['FIPS'] = food_access['FIPS'].astype(str)
stores['FIPS'] = stores['FIPS'].astype(str)
restaurants['FIPS'] = restaurants['FIPS'].astype(str)
insecurity['FIPS'] = insecurity['FIPS'].astype(str)
health['FIPS'] = health['FIPS'].astype(str)
fmarkets['FIPS'] = fmarkets['FIPS'].astype(str)
obesity_data['FIPS Codes'] = obesity_data['FIPS Codes'].astype(str)
obesity_data['FIPS Codes'] = obesity_data['FIPS Codes'].astype(str)
obesity_data['State'] = obesity_data['State'].astype(str)
health_costs['Abbrev'] = health_costs['Abbrev'].astype(str)


merged = geo_data.merge(food_access, left_on='GEO_ID',
                        right_on='FIPS', how='inner')

stores_merged = geo_data.merge(stores, left_on='GEO_ID', 
                                right_on='FIPS', how='inner')

rest_merged = geo_data.merge(restaurants, left_on='GEO_ID', 
                                right_on='FIPS', how='inner')                                

insec_merged = geo_data.merge(insecurity, left_on='GEO_ID', 
                                right_on='FIPS', how='inner')   

health_merged = geo_data.merge(health, left_on='GEO_ID', 
                                right_on='FIPS', how='inner')  

fmarkets_merged = geo_data.merge(fmarkets, left_on='GEO_ID', 
                                right_on='FIPS', how='inner') 


obesity_merged = geo_data.merge(obesity_data, left_on='GEO_ID', 
                                right_on='FIPS Codes', how='inner') 


health_costs = obesity_merged.merge(health_costs, left_on='State', 
                            right_on='Region/state of residence', how='inner')


# Converting all the quantitative data to be mapped to numeric values so 
# they map properly
merged['PCT_LACCESS_HHNV10'] = merged['PCT_LACCESS_HHNV10'].apply(pd.to_numeric)
stores_merged['SNAPSPTH12'] = stores_merged['SNAPSPTH12'].apply(pd.to_numeric)
rest_merged['PC_FFRSALES07'] = rest_merged['PC_FFRSALES07'].apply(pd.to_numeric)
insec_merged['VLFOODSEC_10_12'] = insec_merged['VLFOODSEC_10_12'].apply(pd.to_numeric)
health_merged['PCT_DIABETES_ADULTS10'] = health_merged['PCT_DIABETES_ADULTS10'].apply(pd.to_numeric)
fmarkets_merged['FMRKTPTH13'] = fmarkets_merged['FMRKTPTH13'].apply(pd.to_numeric)
obesity_merged['percent13'] = obesity_merged['percent13'].apply(pd.to_numeric)
health_costs['Average'] = health_costs['Average'].apply(pd.to_numeric)
stores_merged['SNAPSPTH08'] = stores_merged['SNAPSPTH08'].apply(pd.to_numeric)

fig, ax = plt.subplots(figsize=(20,10))
ax.set_ylim([18, 75])
ax.set_xlim([-170, -65])
# plt.set_cmap('Purples')
geo_data.plot(figsize=(20,10), color='696969', ax=ax)
stores_merged.plot(column='SNAPSPTH08', legend=True, ax=ax)
ax.set(title="SNAP-authorized stores per 1000 pop, 2008")
plt.savefig('SNAP-authorized stores per 1000 pop 2008.png', dpi=300)




