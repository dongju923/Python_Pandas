import pandas as pd
import numpy as np
from datetime import datetime

dates = pd.to_datetime(['12-12-2019', datetime(2020, 1, 1),
                       '2nd of Feb, 2020', '2020-Mar-4', '20200701'])
print(dates)

print(dates.to_period('D'))

# dates에서 dates[0]의 값을 빼고 남은 일수를 반환
print(dates-dates[0])

# 2020-01-01 ~ 2020-02-01까지 D(Day)를 반환
print(pd.date_range('2020-01-01', '2020-02-01', freq='D'))

# 2020-01-01일 부터 기간이 7인 Day를 반환
print(pd.date_range('2020.01.01', periods=7))

# 2020-01-01일 부터 기간이 7인 Month를 반환
print(pd.date_range('2020.1.1', periods=7, freq='M'))

# 2020-01-01일 부터 기간이 7인 Hour를 반환
print(pd.date_range('2020-1-1', periods=7, freq='H'))

# 시게열에서의 None은 데이터의 NaN처럼 NaT로 변환
idx = pd.to_datetime(['2020-1-1 12:00:00', '2020-01-02 00:00:00', None])
print(idx)

print(pd.isnull(idx))
