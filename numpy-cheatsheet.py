#!/usr/bin/python3

import numpy as np

simple_array = np.array([10, 29, 4, 78, 93, 44])
# --> [10 29  4 78 93 44]

simple_array[2]
# --> 4

simple_array[2:] #Get all values from index 2 to the end of the array
# --> [4, 78, 93, 44] 

simple_array[2:4] # Get all values from index 2 to index 4
# --> [4, 78, 93] 

simple_array[1::2] # From index 1 get all values each 2 positions
# --> [29 78 44]

np.sort(simple_array)
# --> [ 4 10 29 44 78 93]

np.zeros(3)
# --> [0, 0, 0]

np.zeros((2, 3)) # Creates 2 dimmensions array, first param is the columns and the second one is the rows
"""
[[ 0.  0.  0.]
 [ 0.  0.  0.]]
"""

np.linspace(3, 10, 5) # Creates a random array, first parameter is the minimum value, the second one is the max value and the last one is the number of elements.
# --> [  3.     4.75   6.5    8.25  10.  ]

np.array([['x', 'z', 'y'], ['a', 'b', 'c']]) # Two dimmensions array
"""
[['x' 'z' 'y']
 ['a' 'b' 'c']]
"""

headers = [ ('name', 'S10'), ('age', int) ] #S10 meaning string with max lenght of 10 chars. If we set a name with more than 10 chars numpy cuts the name and saves only first 10 chars.
data = [ ('Juan', 40), ('Maria', 12) ]
users = np.array(data, dtype = headers)
np.sort(users, order = 'age')
# --> [('Maria', 12) ('Juan', 40)]

np.arange(5)
# --> [0 1 2 3 4]


np.arange(5, 10) 
# --> [5 6 7 8 9]

np.arange(5, 30, 5)
# --> [5 10 15, 20, 25]

np.full((3, 5), 10)
"""
[[10 10 10 10 10]
 [10 10 10 10 10]
 [10 10 10 10 10]]
"""

np.diag([0, 3, 9, 12])
"""
[[ 0  0  0  0]
 [ 0  3  0  0]
 [ 0  0  9  0]
 [ 0  0  0 12]]
"""
