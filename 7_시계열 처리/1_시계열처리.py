import pandas as pd
import numpy as np

# 인덱스를 날짜로 사용이 가능
idx = pd.DatetimeIndex(
    ['2019-01-01', '2020-01-01', '2020-02-01', '2020-09-01'])
s = pd.Series([0, 1, 2, 3], index=idx)
print(s)

# 슬라이싱 가능
print(s['2020-01-01':])
print(s[:'2020-01-01'])

# 년도만 설정 가능
print(s['2019'])
