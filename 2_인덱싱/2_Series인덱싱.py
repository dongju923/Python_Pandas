import numpy as np
import pandas as pd
from pandas.core.indexing import _iLocIndexer


s = pd.Series(['a', 'b', 'c', 'd', 'e'], index=[1, 3, 5, 7, 9])
print(s)

print(s[1])
# a
print(s[3])
# b
# print(s[0])   #오류
# Index가 Int64Index일 경우 인덱스 값이 없으면 오류
# Index가 Object일 경우 인덱스 값을 Int64Index로 호출가능
print(s[2:4])
print(s.iloc[1])
# b
# 1 인덱스가 아니라 1번째 인덱스를 반환
print(s.iloc[4])
# e

### reindex(labels=None, index=None, columns=None, axis=None, method=None, copy=True, level=None, fill_value=nan, limit=None, tolerance=None) ###
# 인덱스를 재구성함, 재구성할 인덱스와 기존 인덱스가 다르면 NaN으로 표시
print(s.reindex(range(10)))
# 0~9까지 인덱스를 재구성
print(s.reindex(range(10), method='bfill'))
# 0~9까지 인덱스를 재구성하고 NaN값은 그 전의 값으로 채움
new_index = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(s.reindex(new_index, fill_value=0))
# NaN값은 0으로 채움
