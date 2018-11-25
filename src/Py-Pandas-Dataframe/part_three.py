import pandas as pd
import numpy as np

#matrix
frame = pd.DataFrame(np.arange(9).reshape((3,3)), index=['a', 'c', 'd'], columns=['O', 'T', 'C'])
print(frame)
#    O  T  C
# a  0  1  2
# c  3  4  5
# d  6  7  8

frame1 = frame.reindex(['a', 'c', 'd', 'e'])
print(frame1)
#     O    T    C
# a  0.0  1.0  2.0
# c  3.0  4.0  5.0
# d  6.0  7.0  8.0
# e  NaN  NaN  NaN

states = ['E', 'T', 'C'] # states
frame2 = frame.reindex(columns=states)    # change the columns by recalling the reindex method.
print(frame2)
#     E  T  C
# a NaN  1  2
# c NaN  4  5
# d NaN  7  8

frame3 = frame.reindex(['a', 'c', 'd', 'e'], method='ffill')
print(frame3)
#     E  T  C
# a NaN  1  2
# c NaN  4  5
# d NaN  7  8

frame4 = frame.ix[['a', 'b', 'c', 'd'], states]
print(frame4)
#     E    T    C
# a NaN  1.0  2.0
# b NaN  NaN  NaN
# c NaN  4.0  5.0
# d NaN  7.0  8.0

