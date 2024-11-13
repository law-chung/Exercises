# Exercise P2-1: DataFrame Practice 

# Import libraries
from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn
import numpy as np

# DataFrame data
d = {'Aug': {'David Bowie': 571, 'The Beatles': 725, 'New Order': 274}, 'Sept': {'David Bowie': 623, 'The Beatles': 518, 'New Order': 492}, 'Nov': {'David Bowie': 409, 'The Beatles': 822, 'New Order': 368}}
# Create DataFrame
df = DataFrame(d)
print(df)

# return sept col and total # of plays
s = df['Sept']
print(sum(s))
