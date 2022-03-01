import numpy as np
import pandas as pd

# None: 파이썬 누락 데이터
a = np.array([1, 2, None, 4, 5])
print(a)
# print(sum(a)) # 에러 발생
# None은 파이썬 객체이고, numpy 연산이 불가능


# NaN: 누락 수치 데이터
a = np.array([1, 2, np.nan, 4, 5])
print(a.dtype)
print(sum(a))
# NaN이 포함된 산술 연산의 결과는 무조건 모두 NaN임
print(np.nanmin(a), np.nanmax(a), np.nanmean(a))

s = pd.Series([1, 2, None, 4, np.nan])
print(s)
# pandas에서 None값은 NaN으로 대체됨


# Null값 처리
"""
isnull(): 누락되거나 NA인 값을 boolean으로 반환
notnull(): 누락되지 않거나 NA가 아닌 값을 boolean으로 반환
dropna(): 누락된 데이터가 있는 축 제외
fillna(): 누락된 값을 대체하거나 ffill()이나 bfill()로 보간메소드 적용
"""
s = pd.Series([1, 2, np.nan, 'string', None])
print(s.isnull())
# isnull()에서 NaN, None은 False로 판단
print(s[s.notnull()])
print(s.dropna())
print(s.fillna(0))
print(s.fillna(method='ffill'))
print(s.fillna(method='bfill'))
