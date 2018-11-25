import pandas as pd
import numpy as np


obj = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
print(obj)

newjob = obj.drop('c')
print(newjob)

newjob2 = obj.drop(['c', 'd'])
print(newjob2)    


























