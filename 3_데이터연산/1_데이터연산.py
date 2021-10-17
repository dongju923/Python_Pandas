import numpy as np
import pandas as pd

s = pd.Series(np.random.randint(0, 10, 5))
print(s)

df = pd.DataFrame(np.random.randint(0, 10, (3, 3)), columns=[
                  'A', 'B', 'C'], index=['a', 'b', 'c'])
print(df)

print(np.exp(s))
print(np.cos(df * np.pi/4))

s1 = pd.Series([1, 3, 5, 7, 9], index=[0, 1, 2, 3, 4])
s2 = pd.Series([2, 4, 6, 8, 10], index=[1, 2, 3, 4, 5])
print(s1)
print(s2)

print(s1+s2)
print(s1.add(s2))
# 인덱스를 기준으로 인덱스가 같은 값만 계산
print(s1.add(s2, fill_value=0))
# NaN값은 0으로 채우고 계산

df1 = pd.DataFrame(np.random.randint(0, 20, (3, 3)), columns=list('ACD'))
df2 = pd.DataFrame(np.random.randint(0, 20, (5, 5)), columns=list('BAECD'))
print(df1)
print(df2)

print(df1+df2)
print(df1.add(df2))
# 인덱스를 기준으로 같은 인덱스끼리 계산

print(df1.mean())
# 각 칼럼의 평균을 구함
avg = df1.unstack().mean()
print(avg)
# 모든 값의 평균을 구함
print(df1.add(df2, fill_value=avg))
# NaN값 대신 avg의 값을 채우고 계산
