# 11/19/24 In Class exercise with GroupBy

# import libraries
from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn
import numpy as np

# read csv
data = pd.read_csv('groupby_ex_data.csv')

# create df
df = DataFrame(data)

# collapse artists
g = df.groupby(df['uid']).sum()
print(g)

# collapse uids
g2 = df.groupby(df['artist']).sum()
print(g2)
