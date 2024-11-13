# Exercise P3-1: Summ and desc. statistics functions with DataFrames

# Import libraries
from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn
import numpy as np

# DataFrame data
d = {'Aug': {'David Bowie': 571, 'The Beatles': 725, 'New Order': 274}, 'Sept': {'David Bowie': 623, 'The Beatles': 518, 'New Order': 492}, 'Nov': {'David Bowie': 409, 'The Beatles': 822, 'New Order': 368}}
# Create DataFrame
df = DataFrame(d)

# Total play count for Aug
print(df.Aug.sum())

# Total play count for The Beatles
s = df.loc['The Beatles'].sum()
print(s)

# Return artist w/ most plays of the month
s2 = df.idxmax()
print(s2)

# Which month did each artist have the most plays in 
for i in df.Aug.keys():
    print(df.loc[i].idxmax())