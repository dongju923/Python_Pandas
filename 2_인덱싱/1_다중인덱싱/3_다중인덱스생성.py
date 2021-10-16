from os import name
import numpy as np
import pandas as pd

# DataFrame 생성
df = pd.DataFrame(np.random.rand(6, 3), index=[['a', 'a', 'b', 'b', 'c', 'c'], [
                  1, 2, 1, 2, 1, 2]], columns=['c1', 'c2', 'c3'])
print(df)

# array 멀티인덱스 생성
print(pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b', 'c', 'c'], [
    1, 2, 1, 2, 1, 2]]))

# tuple 멀티인덱스 생성
print(pd.MultiIndex.from_tuples(
    [('a', 1), ('a', 2), ('b', 1), ('b', 2), ('c', 1), ('c', 2)]))

# product 멀티인덱스 생성
print(pd.MultiIndex.from_product([['a', 'b', 'c'], [1, 2]]))

# levels, codes 멀티인덱스 생성
print(pd.MultiIndex(levels=[['a', 'b', 'c'], [1, 2]],
      codes=[[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]]))

# 인덱스에 이름 붙이기
df.index.names = ['인덱스', '값']
print(df)

# 인덱스 만들기
idx = pd.MultiIndex.from_product(
    [['a', 'b', 'c'], [1, 2]], names=['name1', 'name2'])
# 칼럼 만들기
cols = pd.MultiIndex.from_product(
    [['c1', 'c2', 'c3'], [1, 2]], names=['col1', 'col2'])
# data 만들기
data = np.round(np.random.randn(6, 6), 2)
# DataFrame생성
mdf = pd.DataFrame(data, index=idx, columns=cols)
print(mdf)

print(mdf['c2', 1])
print(mdf['c3'])
print(mdf.loc['a'])
print(mdf.iloc[1])
