import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(1, 10).reshape(3, 3),
                  index=list('abc'), columns=list("ABC"))
print(df)

# .iloc: 행번호로 선택하는 방법
print(df.iloc[0])
# 첫 번째 행
print(df.iloc[1])
# 두 번째 행
print(df.iloc[2])
# 세 번째 행
print(df.iloc[:, 0])
# 첫 번째 열
print(df.iloc[:, 1])
# 두 번째 열
print(df.iloc[:, 2])
# 세 번째 열

# .loc: label이나 조건표현으로 선택하는 방법
print(df.loc['a'])
# a행만 선택
print(df.loc['b'])
# b행만 선택
print(df.loc['c'])
# c행만 선택
print(df.loc[['a', 'b'], ['A', 'B', 'C']])
# a,b행과 A,B,C열 동시선택
print(df.loc['a':'c', 'A':'C'])
# 모든 행과 열 동시선택
