# /Users/jiahuama/PycharmPrgiy ojects/Py-Pandas-Practice-

import pandas as pd
import numpy as np

matrix = pd.read_csv('/Users/jiahuama/PycharmProjects/Py-Pandas-Practice- /src/Py-Pandas-Series/prac.csv')
matrix2 = pd.read_csv('/Users/jiahuama/PycharmProjects/Py-Pandas-Practice- /src/Py-Pandas-Series/test.csv')

# print(matrix['App'].head())
frame = pd.DataFrame(matrix)
frame2 = pd.DataFrame(matrix2)
# print(frame)
# print(frame.ix[3])
# print(frame.T)
# print(frame2.head())\   id        date  store  item
# 0   0  2018-01-01      1     1
# 1   1  2018-01-02      1     1
# 2   2  2018-01-03      1     1
# 3   3  2018-01-04      1     1
# 4   4  2018-01-05      1     1
# PyDev console: starting.
# print(frame2.values)
print(frame2.loc[:, 'id':'date'])