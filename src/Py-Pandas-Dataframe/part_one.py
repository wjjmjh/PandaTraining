import pandas as pd
import numpy as np

data = {'state' : ['A', 'B', 'C', 'D', 'E', 'F'], 'year': [2000, 2001, 2003, 2004, 2005, 2006], 'pop': [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]}
frame = pd.DataFrame(data)
print(frame)
#   state  year  pop
# 0     A  2000  1.1
# 1     B  2001  2.2
# 2     C  2003  3.3
# 3     D  2004  4.4
# 4     E  2005  5.5
# 5     F  2006  6.6

frame1 = pd.DataFrame(data, columns=['state', 'pop', 'year'], index= [0, 1, 2, 3, 4, 5])
print(frame1)
#   state  pop  year
# 0     A  1.1  2000
# 1     B  2.2  2001
# 2     C  3.3  2003
# 3     D  4.4  2004
# 4     E  5.5  2005
# 5     F  6.6  2006

frame1['Debt'] = 16.5
print(frame1)
#   state  pop  year
# 0     A  1.1  2000
# 1     B  2.2  2001
# 2     C  3.3  2003
# 3     D  4.4  2004
# 4     E  5.5  2005
# 5     F  6.6  2006

frame1['Debt'] = np.arange(0, 6)
print(frame1)
#   state  pop  year  Debt
# 0     A  1.1  2000     0
# 1     B  2.2  2001     1
# 2     C  3.3  2003     2
# 3     D  4.4  2004     3
# 4     E  5.5  2005     4
# 5     F  6.6  2006     5

# a combination of series and dataframe

value = pd.Series([-1, -2, -3, -4], index=[0, 1, 2, 3])
frame1['Debt'] = value
print(frame1)
#   state  pop  year  Debt
# 0     A  1.1  2000  -1.0
# 1     B  2.2  2001  -2.0
# 2     C  3.3  2003  -3.0
# 3     D  4.4  2004  -4.0
# 4     E  5.5  2005   NaN
# 5     F  6.6  2006   NaN

frame1['Eastern'] = frame1.state == 'A'
print(frame1)
#   state  pop  year  Debt  Eastern
# 0     A  1.1  2000  -1.0     True
# 1     B  2.2  2001  -2.0    False
# 2     C  3.3  2003  -3.0    False
# 3     D  4.4  2004  -4.0    False
# 4     E  5.5  2005   NaN    False
# 5     F  6.6  2006   NaN    False

data1 = {'state' : {11 : 'A', 22 : 'B', 33 : 'C', 44 : 'D', 55 : 'E', 66 : 'F'}, 'year': {22 : 2000, 33 : 2001},  'pop': {33 : 1.1, 44 : 2.2}}
frame2 = pd.DataFrame(data1)
print(frame2)
#    state    year  pop
# 11     A     NaN  NaN
# 22     B  2000.0  NaN
# 33     C  2001.0  1.1
# 44     D     NaN  2.2
# 55     E     NaN  NaN
# 66     F     NaN  NaN

frame2.T
print(frame2)

print(frame2['state'][ : -1])
# 11    A
# 22    B
# 33    C
# 44    D
# 55    E
print(frame2['year'][ : 2])
# 11       NaN
# 22    2000.0

print(frame2.values)
# [['A' nan nan]
#  ['B' 2000.0 nan]
#  ['C' 2001.0 1.1]
#  ['D' nan 2.2]
#  ['E' nan nan]
#  ['F' nan nan]]

print(22 in frame2.index)
# True





































