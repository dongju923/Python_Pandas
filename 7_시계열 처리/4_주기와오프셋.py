"""주기 코드
D: Day : 달력상 일
B: Business Day: 영업일
W: Week: 주
W-MON, W-TUE,...: Weekday: 주
WOW-MON, WOW-2MON,...: WeekOfMonth: 월별 주차와 요일
MS: MonthStart: 월 시작일
BMS: BusinessMonthStart: 영업일 기준 월 시작일
M: MonthEnd: 월 종료일
BM: BusinessMonthEnd: 영업일 기준 월 종료일
QS-JAN, QS-FEB,...: QuarterStart: 분기 시작
BQs-JAN, BQs-FEB,...: BusinessQuarterStart: 영업일 기준 분기 시작
Q-JAN, Q-FEB,...: QuarterEnd: 분기 마지막
AS-JAN, AS-FEB,...: AnnualStart: 연초
BAS-JAN, BAS-FEB,...: BusinessAnnualStart: 영업일 기준 연초
A-JAN, A-FEB,...: AnnualEnd: 연말
BA-JAN, BA-FEB,...: BusinessAnnualEnd: 영업일 기준 연말
H: Hour: 시간
BH: BusinessHour: 영업 시간
T, min: Minute: 분
s: Second: 초
L, ms: MilliSecond: 밀리초
U: MicroSecond: 마이크로초
N: Nanosecond: 나노초
"""
import pandas as pd
import numpy as np

print(pd.timedelta_range(0, periods=12, freq='H'))
print(pd.timedelta_range(0, periods=60, freq='T'))
print(pd.timedelta_range(start='1D', periods=12, freq='D'))
print(pd.timedelta_range(0, periods=10, freq='1H30T'))
print(pd.date_range('2022-01-01', periods=20, freq='B'))
print(pd.date_range('2022-01-11', periods=10, freq='2H'))
