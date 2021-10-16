import numpy as np
import pandas as pd

# 인덱스 만들기
idx = pd.MultiIndex.from_product(
    [['a', 'b', 'c'], [1, 2]])
# 칼럼 만들기
cols = pd.MultiIndex.from_product(
    [['c1', 'c2', 'c3'], [1, 2]])
# data 만들기
data = np.round(np.random.randn(6, 6), 2)
# DataFrame생성
mdf = pd.DataFrame(data, index=idx, columns=cols)
print(mdf)

print(mdf['c2', 1])
print(mdf.iloc[:3, :4])
print(mdf.loc[:, ('c2', 1)])

idx_slice = pd.IndexSlice
print(mdf.loc[idx_slice[:, 2], idx_slice[:, 2]])
