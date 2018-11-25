import pandas as pd



print('------------------------------------')
obj = pd.Series([-0.6, 1.1, 2.3, 4.3], index=['d', 'b', 'a', 'c'])
print(obj)
print('------------------------------------')

obj2 = obj.reindex(['b', 'a', 'c', 'd'])
print(obj2)
print('------------------------------------')

obj3 = obj.reindex(['b', 'a', 'c', 'd', 'f', 'g'], fill_value=0.0)
print(obj3)
print('------------------------------------')

# obj4 = pd.Series(['blue', 'green', 'black'], index=[0,2,4])
# obj4.reindex([4, 2, 0])
# print(obj4)

brushFireRisk = pd.Series([34, 23, 12, 23], index = ['Bisbee', 'Douglas', 'Sierra Vista', 'Tombstone'])
print(brushFireRisk)
print('------------------------------------')

brushFireRiskReindexed = brushFireRisk.reindex(['Tombstone', 'Douglas', 'Bisbee', 'Sierra Vista', 'Barley', 'Tucson'])
print(brushFireRiskReindexed)
print('------------------------------------')


# ------------------------------------
# d   -0.6
# b    1.1
# a    2.3
# c    4.3
# dtype: float64
# ------------------------------------
# b    1.1
# a    2.3
# c    4.3
# d   -0.6
# dtype: float64
# ------------------------------------
# b    1.1
# a    2.3
# c    4.3
# d   -0.6
# f    0.0
# g    0.0
# dtype: float64
# ------------------------------------
# Bisbee          34
# Douglas         23
# Sierra Vista    12
# Tombstone       23
# dtype: int64
# ------------------------------------
# Tombstone       23.0
# Douglas         23.0
# Bisbee          34.0
# Sierra Vista    12.0
# Barley           NaN
# Tucson           NaN
# dtype: float64
# ------------------------------------