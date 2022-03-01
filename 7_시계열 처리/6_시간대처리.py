import pandas as pd
import numpy as np
import pytz  # 전세계의 시간대 정보를 모아놓은 올슨 데이터베이스를 활용한 라이브러리

# 국제표준시(UTC)를 기준으로 떨어진 거리만큼 오프셋으로 시간대 처리
# print(pytz.all_timezones)

tz = pytz.timezone('Asia/Seoul')

index = pd.date_range('2022-01-10 10:00', periods=7, freq='B')
ts = pd.Series(np.random.random(len(index)), index=index)
ts_utc = ts.tz_localize('UTC')
print(ts_utc)
print(ts_utc.index)
print(ts_utc.tz_convert('Asia/Seoul'))


ts_seoul = ts.tz_localize('Asia/Seoul')
print(ts_seoul)
print(ts_seoul.tz_convert('UTC'))


stamp = pd.Timestamp('2022-01-10 12:00')
print(stamp)
stamp_utc = stamp.tz_localize('UTC')
print(stamp_utc)
print(stamp_utc.tz_convert("Asia/Seoul"))
