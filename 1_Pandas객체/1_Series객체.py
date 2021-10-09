import pandas as pd
import numpy as np

s = pd.Series([0, 0.25, 0.5, 0.75, 1.0])
print(s)
# 인덱스와 함께 데이터가 저장
print(s.values)
# 값만 반환
# [0.   0.25 0.5  0.75 1.  ]
print(s.index)
# 인덱스만 반환
# RangeIndex(start=0, stop=5, step=1)
print(s[1])
# 인덱스에 접근 가능
print(s[1:4])
# 슬라이싱으로 접근 가능
# 인덱스와 값이 함께 반환
print(s.index[1])
# 인덱스만 반환된 값에서 인덱스 접근
print(s.values[3])
# 값만 반환된 값에서 인덱스 접근

s = pd.Series([0, 0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd', 'e'])
print(s)
# 인덱스가 a,b,c,d,e로 반환
print(s.index)
# Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
print(s.values)
# [0.   0.25 0.5  0.75 1.  ]
print(s[3])
# 0.75
print(s['d'])
# 0.75
print(s[['c', 'd', 'e']])
# 원하는 인덱스만 접근 가능

print('b' in s)
# True

s = pd.Series([0, 0.25, 0.5, 0.75, 1.0], index=[2, 4, 6, 8, 10])
print(s)
# 인덱스가 2,4,6,8,10으로 반환
print(s[2])
# 0.25
print(s[4])
# 0.25
print(s[2:])
print(s[[2, 4, 6]])
# 2,4,6q번 인덱스와 값만 반환

print(s.unique())
# [0.   0.25 0.5  0.75 1.  ]
# 유일한 값만 반환
print(s.value_counts())
# 값의 개수를 반환
print(s.isin([0, 25, 0.75]))
# 값의 위치를 boolean형태로 반환

population_tuple = {'서울특별시': 9720846, '부산광역시': 3404423, '인천광역시': 2947217}
print(population_tuple)
# {'서울특별시': 9720846, '부산광역시': 3404423, '인천광역시': 2947217}
population = pd.Series(population_tuple)
# 튜플 형태를 Series 형태로 변환
print(population)
print(population['서울특별시'])
print(population['서울특별시':'인천광역시'])
print(population.index)
# Index(['서울특별시', '부산광역시', '인천광역시'], dtype='object')
print(population.values)
# [9720846 3404423 2947217]
