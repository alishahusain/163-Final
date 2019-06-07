# Final Project

import pandas as pd
import geopandas as gpd

# Load in data
geo_data = gpd.read_file('United States Counties.csv')
food_access = pd.read_excel('access2015.xls', sheet_name='ACCESS')
stores = pd.read_excel('access2015.xls', sheet_name='STORES')
restaurants = pd.read_excel('access2015.xls', sheet_name='RESTAURANTS')
socioecon = pd.read_excel('access2015.xls', sheet_name='SOCIOECONOMIC')
health = pd.read_excel('access2015.xls', sheet_name='HEALTH')
fmarkets = pd.read_excel('access2015.xls', sheet_name='LOCAL')
prices = pd.read_excel('access2015.xls', sheet_name='PRICES_TAXES')
insecurity = pd.read_excel('access2015.xls', sheet_name='INSECURITY')
assistance = pd.read_excel('access2015.xls', sheet_name='ASSISTANCE')

pop_by_county = pd.read_excel('access2015.xls',
                              sheet_name='Supplemental Data - County')
part_by_state = pd.read_excel('access2015.xls',
                              sheet_name='Supplemental Data - State')
exp_per_cap = pd.read_csv('health_exp_per_capita.csv')

# Select rows of interest in food access dataframe
food_access = food_access[['FIPS', 'State', 'County','PCT_LACCESS_POP10',
                           'PCT_LACCESS_LOWI10', 'PCT_LACCESS_CHILD10', 
                           'PCT_LACCESS_SENIORS10', 'PCT_LACCESS_HHNV10']]

# Select rows of interest in stores dataframe
stores = stores[['PCH_GROC_07_12', 'PCH_GROCPTH_07_12', 'PCH_SUPERC_07_12',
                 'SUPERCPTH07', 'SUPERCPTH12', 'PCH_SUPERCPTH_07_12', 
                 'PCH_CONVS_07_12', 'CONVSPTH07', 'CONVSPTH12',
                 'PCH_CONVSPTH_07_12', 'PCH_SPECS_07_12', 'SPECSPTH07',
                 'SPECSPTH12', 'PCH_SPECSPTH_07_12', 'PCH_SNAPS_08_12',
                 'SNAPSPTH08', 'SNAPSPTH12', 'PCH_SNAPSPTH_08_12']]

# Select rows of interest in restaurants dataframe
restaurants = restaurants[['PCH_FFR_07_12', 'FFRPTH07', 'FFRPTH12',
                           'PCH_FFRPTH_07_12', 'PC_FFRSALES02',
                           'PC_FFRSALES07', 'PC_FSRSALES02', 'PC_FSRSALES07']]

# Select rows of interest in assistance dataframe
assistance = assistance[['REDEMP_SNAPS08', 'REDEMP_SNAPS12',
                        'PCH_REDEMP_SNAPS_08_12', 'PCT_SNAP09'
                        'PCT_SNAP14','PCH_SNAP_09_14','PC_SNAPBEN08'
                        'PC_SNAPBEN10','PCH_PC_SNAPBEN_08_10',
                        'SNAP_PART_RATE08', 'SNAP_PART_RATE10']]

#Select rows of interest in insecurity dataframe
insecurity = insecurity[['CH_VLFOODSEC_09_12', 'VLFOODSEC_10_12'
                        'CH_FOODINSEC_09_12', 'FOODINSEC_10_12']]

#Select rows of interest in health dataframe
health = health[['PCT_DIABETES_ADULTS09', 'PCT_DIABETES_ADULTS10',
                'PCT_OBESE_ADULTS09', 'PCT_OBESE_ADULTS10',
                'PCT_OBESE_ADULTS13', 'PCT_OBESE_CHILD08',
                'PCT_OBESE_CHILD11','PCH_OBESE_CHILD_08_11']]

#Select rows of interest in prices dataframe
prices = prices[['MILK_SODA_PRICE10']]

#Select rows of interest in fmarkets dataframe
fmarkets = fmarkets[['FMRKTPTH13', 'PCH_FMRKTPTH_09_13', 
                    'PCT_FMRKT_SNAP13', 'FMRKT_WIC13']]

#Select rows of interest in socioeconomic dataframe
socioecon = socioecon[['POVRATE10', 'PERPOV10']]



# Select rows of interest in participation dataframe

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
