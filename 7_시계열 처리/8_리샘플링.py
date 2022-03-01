import numpy as np
import pandas as pd

# 리샘플링(Resampling)
# 리샘플링(Resampling): 시계열의 빈도 변환
# 다운샘플링(Downsampling): 상위 빈도 데이터를 하위 빈도 데이터로 집계
# 업샘플링(Upsampling): 하위 빈도 데이터를 상위 빈도 데이터로 집계
# resample()

"""resample() 인자
freq: 리샘플링 빈도
aixs: 리샘플링 축(defalt: 0)
fill_method: 업샘플링시 보간 수행(None, ffill, bfill)
closed: 다운샘플링 시 각 간격의 포함 위치(left, right)
label: 다운샘플링 시 집계된 결과 라벨 결정(left, right)
loffset: 나뉜 그룹의 라벨을 맞추기 위한 오프셋
limit: 보간법을 사용할 때 보간을 적용할 최대 기간
kind: 기간 또는 타임스탬프 집계 구분
convention: 기간을 리샘플링할 때 하위 빈도 기간에서 상위빈도로 변환시 방식(start, end)
"""

dr = pd.date_range('2020-01-01', periods=200, freq='D')
ts = pd.Series(np.random.randn(len(dr)), index=dr)
print(ts)
print(ts.resample('M').mean())
print(ts.resample('M', kind='period').mean())

dr = pd.date_range('2020-01-01', periods=10, freq='T')
ts = pd.Series(np.arange(10), index=dr)
print(ts)
print(ts.resample('2T', closed='left').sum())
print(ts.resample('2T', closed='right').sum())
print(ts.resample('2T', closed='right', label='right').sum())
print(ts.resample('2T', closed='right', label='right', loffset='-1s').sum())
print(ts.resample('2T').ohlc())

df = pd.DataFrame(np.random.randn(10, 4), index=pd.date_range(
    '2020-10-01', periods=10, freq='M'), columns=(['c1', 'c2', 'c3', 'c4']))
print(df)
print(df.resample('Y').asfreq())
print(df.resample('W-FRI').asfreq())
print(df.resample('H').asfreq())
print(df.resample('H').ffill())
print(df.resample('H').ffill(limit=2))
