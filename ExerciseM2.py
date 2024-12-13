# Exercise M2: Merge DataFrames with index and a column 

# import libraries
from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn
import numpy as np

# load csv 
teamdf = pd.read_csv('teams-cities.csv')

# create geo_df 
geo_df = pd.read_csv('geodata.csv', index_col = ' ')

# merge city df and geo df 

m_df = pd.merge(teamdf, geo_df, left_on='city', right_index=True)

print(m_df)