import numpy as np
import pandas as pd

s = pd.Series(np.random.randint(1, 10, 5), index=list("ADBCE"))
print(s)

print(s.sort_index())
# 인덱스 기준으로 정렬
print(s.sort_values())
# 값 기준으로 정렬

df = pd.DataFrame(np.random.randint(1, 50, (4, 4)), index=[
                  2, 4, 1, 3], columns=list("BCDA"))
print(df)

print(df.sort_index())
# 인덱스 기준으로 정렬
print(df.sort_index(axis=1))
# 칼럼 기준으로 정렬
print(df.sort_values(by='A'))
# A 칼럼 기준으로 정렬
print(df.sort_values(by=['A', 'C']))
# A 칼럼 정렬후 C 칼럼 정렬
