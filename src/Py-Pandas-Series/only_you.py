import pandas as pd
import numpy as np


data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)
print(s)
# 0    a
# 1    b
# 2    c
# 3    d

ss = pd.Series(data, index=[100, 101, 102, 103])
print(ss)
# 100    a
# 101    b
# 102    c
# 103    d

Data = {'a':0, 'b':1, 'c':2}
sss = pd.Series(Data)
print(sss)
# a    0
# b    1
# c    2
# dtype: int64

ssss = pd.Series(Data, index=['b', 'c', 'd'])
print(ssss)
# b    1.0
# c    2.0
# d    NaN
# dtype: float64

new = pd.Series(5, index=[1,2,3,4])
print(new)
# 1    5
# 2    5
# 3    5
# 4    5
# dtype: int64

nn = pd.Series([1,2,3,4,5], index=['a', 'b', 'c', 'd', 'e'])
print(nn)
# a    1
# b    2
# c    3
# d    4
# e    5
# dtype: int64
print(nn[0])
#1
print(nn[1])
#2