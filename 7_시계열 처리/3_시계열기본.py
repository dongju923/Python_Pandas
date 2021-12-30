from numpy.core.defchararray import index
import pandas as pd
import numpy as np
from datetime import datetime

from pandas.core.indexes.datetimes import DatetimeIndex, date_range

dates = [datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(
    2020, 1, 4), datetime(2020, 1, 7), datetime(2020, 1, 11), datetime(2020, 1, 15)]
print(dates)

ts = pd.Series(np.random.randn(6), index=dates)
print(ts)

print(ts.index)
print(ts.index[0])
print(ts[ts.index[2]])
print(ts['20200115'])

ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('2017-10-01', periods=1000))
print(ts)

# 2020년의 데이터만 반환
print(ts['2020'])
# 2020년 06의 데이터만 반환
print(ts['2020-06'])
# 2020-06-20이후 데이터만 반환
print(ts[datetime(2020, 6, 20):])
print(ts['2020-06-20':])

tdf = pd.DataFrame(np.random.randn(1000, 4), index=date_range(
    '2017-10-01', periods=1000), columns=['A', 'B', 'C', 'D'])
print(tdf)

# 2020년인 것만 반환
print(tdf['2020'])
# 2020-06인 것만 반환
print(tdf.loc['2020-06'])
# 2020-06-20인 것만 반환
print(tdf.loc['2020-06-20'])
# C칼럼 반환
print(tdf['C'])

ts = pd.Series(np.random.randn(10), index=pd.DatetimeIndex(['2020-01-01', '2020-01-01', '2020-01-02',
               '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05', '2020-01-05', '2020-01-06', '2020-01-07']))
print(ts)

print(ts.index.is_unique)
print(ts['20200101'])
print(ts.groupby(level=0).mean())
print(pd.date_range('20200101', '2020-07-01'))
print(pd.date_range(start='20200101', periods=7))
print(pd.date_range(end='2020-07-01', periods=10))
# 2020-07-01부터 2020-07-07까지 B(주중)만 반환
print(pd.date_range('20200701', '20200707', freq='B'))
