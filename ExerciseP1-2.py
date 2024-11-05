# P1-2 Series practice

# Import libraries
from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn
import numpy as np

ind = ['Britney Spears', 'Depeche Mode', 'Lady Gaga']

aug_vals = [190, 274, 344]

sept_vals = [123, 497, 273]

# aug plays series
aug_plays = Series(aug_vals, index = ind)

# sept plays series
sept_plays = Series(sept_vals, index = ind)

avg_plays = (aug_plays + sept_plays) / 2

print(avg_plays)