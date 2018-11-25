import pandas as pd
import numpy as np

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df2 = pd.DataFrame({'key': ['b', 'b', 'a'], 'data2': range(3)})
print(df1)
print(df2)
df3 = pd.merge(df1, df2)
print(df3)
list2 = [1,2,3,4,5,6]
print(list2[:-2])


def addone(x):
    return x + 1


print(addone(2))

