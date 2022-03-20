#!/usr/bin/python3

import pandas as pd

# Series (1D)
# DataFrames (2D)
# Panels (3D)

series = pd.Series([5, 10, 73, 12]) # Its like an array
"""
0     5
1    10
2    73
3    12
dtype: int64
"""

series[2]
# --> 73

lst = pd.DataFrame(['Hola', 'mundo', 'robotico']) 
"""

          0
0      Hola
1     mundo
2  robotico
"""

data = { 
    'name': ['Juan', 'Ana', 'Jose'], 
    'age': [10, 34, 77], 
    'country': ['ESP', 'MX', 'CO']
}
users = pd.DataFrame(data)
"""
   name  age country
0  Juan   10     ESP
1   Ana   34      MX
2  Jose   77      CO
"""

users[['name', 'country']]
"""
   name country
0  Juan     ESP
1   Ana      MX
2  Jose      CO
"""

songs = pd.read_csv('./data/canciones-2018.csv')
"""
                       id                               name       artists  danceability  energy  ...  liveness  valence    tempo  duration_ms  time_signature
0   6DCZcSspjsKoFjzjrWoCd                         God's Plan         Drake         0.754   0.449  ...    0.5520   0.3570   77.169     198973.0             4.0
1   3ee8Jmje8o58CHK66QrVC                               SAD!  XXXTENTACION         0.740   0.613  ...    0.1230   0.4730   75.023     166606.0             4.0
..                    ...                                ...           ...           ...     ...  ...       ...      ...      ...          ...             ...
99  3EPXxR3ImUwfayaurPi3c                         Be Alright    Dean Lewis         0.553   0.586  ...    0.0813   0.4430  126.684     196373.0             4.0

[100 rows x 16 columns]
"""

songs.head(5) # Print first 5 elements
songs.tail(5) # Print last 5 elements

artist = songs.artists
artist[5]
# --> 'Post Malone'

songs.iloc[5] # Gets detailed information of specific row
"""
id                  7dt6x5M1jzdTEt8oCbisT
name                           Better Now
artists                       Post Malone
danceability                         0.68
energy                              0.563
key                                    10
loudness                           -5.843
mode                                    1
speechiness                        0.0454
acousticness                        0.354
instrumentalness                        0
liveness                            0.136
valence                             0.374
tempo                             145.028
duration_ms                        231267
time_signature                          4
Name: 5, dtype: object
"""

songs.shape # Gets the size of the structure (number of rows and number of columns)
# --> (100, 16) 

songs.columns # Gets de columns and types

songs['tempo'].describe()
"""
count    100.000000
mean     119.904180
std       28.795984
min       64.934000
25%       95.730750
50%      120.116000
75%      140.022750
max      198.075000
Name: tempo, dtype: float64
"""

songs.sort_index(axis = 0, ascending = False) # Orders the structure. axis = The axis along which to sort. The value 0 identifies the rows, and 1 identifies the columns.
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html

