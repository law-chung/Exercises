# Exercise N1-3: NumPy Arrays slice 

# import numpy 
import numpy as np

# create array a 
m1 = [[1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]]
a = np.array(m1)

# create array a 
m2 = [[1,1,2,2], [3,3,4,4], [5,5,6,6], [7,7,8,8]]
b = np.array(m2)

# store added array in var c 
c = a + b 

# take slice of c and return it 
slice = c[1:3, 1:3]
print(slice)