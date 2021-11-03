"""집계연산 함수
count(): 전체 개수
head(): 앞의 항목 일부 반환
tail(): 뒤의 항목 일부 반환
describe(): Series, DataFrame의 각 컬럼에 대한 요약 통계
min(), max(): 최소값, 최대값
argmin(), argmax(): 최소값과 최대값의 인덱스 위치
idxmin(), idxmax(): 최소값과 최대값의 인덱스 값
mean(): 평균값
median(): 중앙값
std(): 표준편차
var(): 분산
skew(): 왜도값 계산
kurt(): 첨도값 계산
mad(): 절대평균편차
sum(), cumsum(): 전체항목 합, 누적합
prod(), cumprod(): 전체항목 곱, 누적곱
quantile(): 0부터 1까지 분위수 계산
diff(): 1차 산술차 계산
pct_change(): 퍼센트 변화율 계산
corr(): 상관관계
cov(): 공분산
"""
import pandas as pd
import numpy as np
from pandas.core.algorithms import quantile

df = pd.DataFrame([[-1, 1.2, np.nan], [2.4, -5.5, 6.7], [
                  np.nan, np.nan, np.nan], [0.44, -3.5, -6.1]], index=[1, 2, 3, 4], columns=['A', 'B', 'C'])
print(df)

s = pd.Series([5, 4, 9], index=['A', 'B', 'C'])
print(s)

# head(n=5)
print(df.head(2))

# tail(n=5)
print(df.tail(3))

# describe(percentiles=None, include=None, exclude=None, datetime_is_numeric=False)
print(df.describe())

# argmin(axis=None, skipna=True, *args, **kwargs)
print(np.argmin(s))

# argmax(axis=None, skipna=True, *args, **kwargs)
print(np.argmax(s))

# idxmin(axis=0, skipna=True)
print(df.idxmin())

# idxmax(axis=0, skipna=True)
print(df.idxmax())

# std(axis=None, skipna=None, level=None, ddof=1, numeric_only=None, **kwargs)
print(df.std())

# var(axis=None, skipna=None, level=None, ddof=1, numeric_only=None, **kwargs)
print(df.var())

# skew(axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
print(df.skew())

# kurt(axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
print(df.kurt())

# sum(axis=None, skipna=None, level=None, numeric_only=None, min_count=0, **kwargs)
print(df.sum())

# cumsum(axis=None, skipna=True, *args, **kwargs)
print(df.cumsum())

# prod(axis=None, skipna=None, level=None, numeric_only=None, min_count=0, **kwargs)
print(df.prod())

# cumprod(axis=None, skipna=True, *args, **kwargs)
print(df.cumprod())

# quantile(q=0.5, axis=0, numeric_only=True, interpolation='linear')
print(df.quantile())

# diff(periods=1, axis=0)
print(df.diff())

# pct_change(periods=1, fill_method='pad', limit=None, freq=None, **kwargs)
print(df.pct_change())

# corr(method='pearson', min_periods=1)
print(df.corr())

# corrwith(other, axis=0, drop=False, method='pearson')
print(df.corrwith(df.B))

# cov(min_periods=None, ddof=1)
print(df.cov())
