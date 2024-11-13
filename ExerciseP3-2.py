# Exercise P3-2: Sorting DataFrames

# Import libraries
from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn
import numpy as np

# DataFrame data
d = {'Aug': {'David Bowie': 571, 'The Beatles': 725, 'New Order': 274}, 'Sept': {'David Bowie': 623, 'The Beatles': 518, 'New Order': 492}, 'Nov': {'David Bowie': 409, 'The Beatles': 822, 'New Order': 368}}
# Create DataFrame
df = DataFrame(d)

# Return a DataFrame sorted by artist name
print(df.sort_index())

# Return a DataFrame sorted on Nov. playcounts
print(df.sort_values(by='Nov', ascending=False))