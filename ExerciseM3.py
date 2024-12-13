# Exercise M3: Merge to filter DF while joining them 

# import libraries 
from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn
import numpy as np 

# load dataframes
city_df = pd.read_csv('teams-cities.csv')
geo_df = pd.read_csv('geodata.csv', index_col = ' ')

# pdmerge and filter to create df with only EDT timezone

edt_df = pd.merge(city_df, geo_df[geo_df.timezone=='EDT'], left_on='city', right_index=True)

print(edt_df)